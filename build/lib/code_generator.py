import shelve

class CodeGenerator:
    def __init__(self, config):
        self.config = config

    # Separate functionality into different functions and call them here?
    # Outputs file
    def generate(self):
        # May be missing steps...
        # Create a .c file with the name
        f = open(self.config['name'] + '.c', 'w')

        # Include statements

        for function in self.config['functions']:
        # For each function:
            new_func = self.generate_function_block(function)
            # Create function signature with name
            new_func = new_func.replace('FUNCTION_NAME', self.config['name'])
            # Instantiate variables
            new_func = new_func.replace('VARIABLE_INIT', self.generate_variable_instantiations(function))
            # Construct format string
            new_func = new_func.replace('FORMAT_STRING', wrap_quotes(self.generate_format_string(function)))
            # Construct ParseTuple function

            # Insert 'code begins/ends' demarcations

            # Do decrementing to objects

            # Write out function
            f.write(new_func)

        # Create my methods struct
        f.write(self.generate_mymethods())
        # Create intialization function for the module
        f.write(self.generate_initialization())
        
        f.close()
        return

    def generate_function_block(self, function):
        return """
        FUNCTION_NAME(PyObject *dummy, PyObject *args)
        {
            VARIABLE_INIT

            if (!PyArg_ParseTuple(args, FORMAT_STRING, ARGUMENTS)) return NULL;
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
        db = shelve.open('format_string')
        for arg in args:
            try:
                var_inst += '*' +  db[arg['type']] + '=null,' 
            finally:
                print("ERROR: Unsupported data-type")
                db.close()

    def generate_parse_tuple(self, function):
        pass

    def generate_decrement(self, function):
        pass

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
        init_func = """
        PyMODINIT_FUNC
            initMODULE_NAME(void)
            {
                (void)Py_InitModule(MODULE_NAME, mymethods);
                import_array();
            }
        """

        init_func = init_func.replace('MODULE_NAME', self.config['name'], 1)
        init_func = init_func.replace('MODULE_NAME', wrap_quotes(self.config['name']), 1)

        return init_func


def wrap_quotes(string):
    return '\"' + string + '\"'





