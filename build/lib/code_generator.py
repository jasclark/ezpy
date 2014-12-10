class CodeGenerator:
    def __init__(self, config):
        self.config = config

    # Separate functionality into different functions and call them here?
    # Outputs file
    def generate(self):
        # May be missing steps...
        # Create a .c file with the name
        f = open(self.config['name'], 'w')

        # Include statements

        # For each function:

            # Create function signature with name

            # Instantiate variables

            # Construct format string

            # Construct ParseTuple function

            # Insert 'code begins/ends' demarcations

            # Do decrementing to objects

        # Create my methods struct
        f.write(self.generate_mymethods())
        # Create intialization function for the module
        f.write(self.generate_initialization())
        
        f.close()
        return

    def generate_function_block(self, function):
        """
        /**FUNCTION NAME **/ (PyObject *dummy, PyObject *args)
        {
            /**VARIABLE INITIALIZATION **/

            if (!PyArg_ParseTuple(args, /**FORMAT STRING**/, /**ARGUMENTS*/)) return NULL;
        }
        """
        pass

    def generate_format_string(self, function):
        args = function['arguments'] 
        format_string = ''
        for arg in args:
            format_string += arg['datatype']
        return format_string
    
    def generate_variable_instantiations(self, function):
        pass

    def generate_parse_tuple(self, function):
        pass

    def generate_decrement(self, function):
        pass

    def generate_mymethods(self):
        mymethods_struct = """
        static struct PyMethodDef mymethods[] = {
            ^METHODS^
            { "multiply", multiply_cfunc, METH_VARARGS, "Doc string"},
            {NULL, NULL, 0, NULL} /* Sentinel - marks the end of the structure*/
        };
        """

        method_defs = ""

        for function in self.config['functions']:
            new_def = "{^MODULE_NAME^, ^FUNCTION_NAME^, METH_VARARGS, "Doc string"},\n"
            new_def.replace('^MODULE_NAME^', self.config['name'])
            new_def.replace('^FUNCTION_NAME^', function['name'])
            method_defs += new_def

        mymethods_struct.replace('^METHODS^', method_defs)
        return mymethods_struct

    def generate_initialization(self):
        init_func = """PyMODINIT_FUNC
            initmatrix_multiply(void)
            {
                (void)Py_InitModule(^MODULE_NAME^, mymethods);
                import_array();
            }
        """

        init_func.replace('^MODULE_NAME^', self.config['name'])
        return init_func





