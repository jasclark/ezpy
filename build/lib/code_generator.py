import shelve

class CodeGenerator:
    def __init__(self, config):
        self.config = config

    # Separate functionality into different functions and call them here?
    # Outputs file
    def generate(self):
        # May be missing steps...
        # Create a .c file with the name

        # Include statements

        # For each function:

            # Create function signature with name

            # Instantiate variables

            # Construct format string

            # Construct ParseTuple function

            # Insert 'code begins/ends' demarcations

            # Do decrementing to objects

        # Create my methods struct

        # Create intialization function for the module

        pass

    def generate_function_block(self, function):
        """
        /**FUNCTION NAME **/ (PyObject *dummy, PyObject *args)
        {
            /**VARIABLE INITIALIZATION **/

            if (!PyArg_ParseTuple(args, /**FORMAT STRING**/, /**ARGUMENTS*/)) return NULL;
        }
        """
}
        pass

    def generate_format_string(self, function):
        args = function['arguments'] 
        format_string = ''
        for arg in args:
            format_string += arg['datatype']
        return format_string

    def generate_variable_instantiations(self, function):
        args = function['arguments']
        var_inst = ''
        db = shelve.open('format_string.db')
        for arg in args:
            try:
                var_inst += '*' +  db[arg['name']] + '=null,' 
            finally:
                print("ERROR: Unsupported data-type")
                db.close()

    def generate_parse_tuple(self, function):
        pass

    def generate_decrement(self, function):
        pass

    def generate_mymethods(self):
        pass

    def generate_initialization(self):
        pass



