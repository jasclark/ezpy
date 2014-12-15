import shelve
import re
from subprocess import call

class CodeGenerator:
    def __init__(self, config):
        self.config = config
        self.uniquenum = 0

    def uniqueid(self):
        ret = self.uniquenum
        self.uniquenum += 1
        return 'a' + str(ret)

    # Separate functionality into different functions and call them here?
    # Outputs file
    def generate(self):
        # May be missing steps...
        # Create a .c file with the name
        output_file_name = self.config['name'] + '.c'
        f = open(output_file_name, 'w')

        EXTENSION_DB_PATH = 'build/lib/extension.db'
        extension_db = shelve.open(EXTENSION_DB_PATH)
        # Include statements
        file_cache = ''
        for function in self.config['functions']:
            # preprocess args
            for arg in function['arguments']:
                print 'arg'
                print arg
                if arg['type'] in extension_db:
                    extension = extension_db[arg['type']]
                    if 'init' not in self.config:
                        self.config['init'] = []
                    if extension['init'] not in self.config['init']:
                        self.config['init'].append(extension['init'])
                    if 'include' not in self.config:
                        self.config['include'] = []
                    if extension['include'] not in self.config['include']:
                        self.config['include'].append(extension['include'])
                    arg['type'] = extension['format_string']
                    arg['extension_var_name'] = arg['name']
                    arg['name'] = extension['format_string_args']
                    extension_code = extension['code']
                    for idx, format_string_arg in enumerate(extension['format_string_args']):
                        if format_string_arg[0] == '%':
                            uniqueid = self.uniqueid()
                            # Replace anywhere this variable arises with this uniqueid
                            extension_code = extension_code.replace(format_string_arg, uniqueid)
                            print 'name before'
                            print arg['name']
                            arg['name'][idx] = uniqueid
                            print 'name aftr'
                            print arg['name']
                    name_match_re = re.compile('%name(\d+)')
                    matches = name_match_re.findall(extension_code)
                    for match in matches:
                        arg_num = int(match) - 1
                        extension_code = extension_code.replace("%name"+match, arg['extension_var_name'][arg_num])
                    if 'extension_code' not in function:
                        function['extension_code'] = ''
                    function['extension_code'] += extension_code
         

        # For each function:
            new_func = self.generate_function_block(function)
            # Create function signature with name
            new_func = new_func.replace('FUNCTION_NAME', function['name'])
            # Instantiate variables
            new_func = new_func.replace('VARIABLE_INIT', self.generate_variable_instantiations(function))
            # Construct format string
            new_func = new_func.replace('FORMAT_STRING', wrap_quotes(self.generate_format_string(function)))
            # Generate arguments
            new_func = new_func.replace('ARGUMENTS', self.generate_arguments(function))
            # Do decrementing to objects
            new_func = new_func.replace('DECREMENT_REFERENCES', self.generate_decrement(function))
            # Generate return statement
            new_func = new_func.replace('RETURN_STATEMENT', self.generate_return_statement(function))
            # Generate extension code segment
            if 'extension_code' in function:
                new_func = new_func.replace('EXTENSION_CODE', '\n' + function['extension_code'])
            else: 
                new_func = new_func.replace('EXTENSION_CODE', '')

            # Write out function
            file_cache += new_func

        # Create my methods struct
        f.write(self.generate_include())
        f.write(file_cache)
        f.write(self.generate_mymethods())
        # Create intialization function for the module
        f.write(self.generate_initialization())
        
        f.close()

        # Indent the output c file using indent command. Built into Unix.
        call(["indent", '-di1', output_file_name])
        call(["rm", output_file_name + ".BAK"])
        return

    def generate_function_block(self, function):
        return """
        static PyObject* FUNCTION_NAME(PyObject *dummy, PyObject *args)
        {
            VARIABLE_INIT

            if (!PyArg_ParseTuple(args, FORMAT_STRING,ARGUMENTS)) return NULL;
            EXTENSION_CODE

            /** Write your code here */

            /** End code */

            DECREMENT_REFERENCES

            RETURN_STATEMENT
        }
        """

    def generate_format_string(self, function):
        args = function['arguments'] 
        format_string = ''
        for arg in args:
            format_string += arg['type']
        return format_string

    def generate_variable_instantiations(self, function):
        args = function['arguments']
        var_inst = ''
        db = shelve.open('build/lib/format_string', flag='r')
        for arg in args:
            print 'arg'
            print arg
            key = str(arg['type'])
            boolean = db.has_key(key)
            print boolean
            if db.has_key(key):
                value = db[key]
                print 'value'
                print value
                for idx, data_type in enumerate(value):
                    if data_type != 'SKIP':
                        var_inst += value[idx] + arg['name'][idx]
                        print 'data type ' + data_type
                        if key == 'O' or key == 'O!' or key == 'O&':
                            var_inst += ' = NULL;\n'
                        else:
                            var_inst += ';\n' 
            else:
                print ('Error: unsupported type ' + key)
                break
        db.close()
        print var_inst
        return var_inst

    def generate_arguments(self, function):
        args = ''
        for arg in function['arguments']:
            for name in arg['name']:
                args += ' &' + name + ','
        return args[:-1]

    def generate_decrement(self, function): 
        decrement_string = ''
        for arg in function['arguments']:
            data_type = arg['type']
            if data_type == 'O' or data_type == 'O!' or data_type == 'O&':
                for name in arg['name']:
                    new_decrement = "Py_XDECREF(VARIABLE);\n"
                    new_decrement = new_decrement.replace('VARIABLE', name)
                    decrement_string += new_decrement
                for name in arg['extension_var_name']:
                    new_decrement = "Py_XDECREF(VARIABLE);\n"
                    new_decrement = new_decrement.replace('VARIABLE', name)
                    decrement_string += new_decrement  

        return decrement_string

    def generate_return_statement(self, function):
        if 'return' in function:
            pybuild_string = """return Py_BuildValue("FORMAT_STRING", /* Put your return values here. */);"""
            pybuild_string = pybuild_string.replace("FORMAT_STRING", function['return'])
            return pybuild_string
        else:
            default_none_return = "Py_RETURN_NONE;"
            return default_none_return

    def generate_mymethods(self):
        mymethods_struct = """
        static struct PyMethodDef mymethods[] = {
            METHODS
            {NULL, NULL, 0, NULL} /* Sentinel - marks the end of the structure*/
        };"""

        method_defs = ""

        for function in self.config['functions']:
            new_def = """{PY_FUNCTION_NAME, FUNCTION_NAME, METH_VARARGS, "Doc string"},\n"""
            new_def = new_def.replace('PY_FUNCTION_NAME', wrap_quotes(function['name']))
            new_def = new_def.replace('FUNCTION_NAME', function['name'])
            method_defs += new_def

        mymethods_struct = mymethods_struct.replace('METHODS', method_defs)
        return mymethods_struct

    def generate_initialization(self):
        init_func = """\n
        PyMODINIT_FUNC
            initMODULE_NAME(void)
            {
                (void)Py_InitModule(MODULE_NAME, mymethods);
                EXTENSION_INIT
            }
        """

        init_func = init_func.replace('MODULE_NAME', self.config['name'], 1)
        init_func = init_func.replace('MODULE_NAME', wrap_quotes(self.config['name']), 1)
        init_extension_code = ''
        if 'init' in self.config:
            for init in self.config['init']:
                init_extension_code += init + '\n'
            init_func = init_func.replace('EXTENSION_INIT', init_extension_code)
        else:
            init_func = init_func.replace('EXTENSION_INIT', '')

        return init_func

    def generate_include(self):
        include = "#include \"Python.h\"\n"
        if 'include' in self.config:
            for include_file in self.config['include']:
                include += "#include \"" + include_file + "\"\n"
        return include

def wrap_quotes(string):
    return '\"' + string + '\"'





