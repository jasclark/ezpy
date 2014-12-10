import re

class ConfigurationParser:

    # Parses configuration file, throws Error if unsuccessful
    def parse(self, file_name):
        config_file = open(file_name)
        internal_config = {'name':None, 'functions':[]}

        name_re = re.compile('^name\s*:\s*([a-zA-Z0-9_.]+)$')
        function_re = re.compile('^function\s*:\s*([a-zA-Z_]+[a-zA-Z0-9_]*)$')
        arg_re = re.compile('^(\S+)\s*:\s*([a-zA-Z_]+[a-zA-Z0-9_]*)$')

        line = config_file.readline()

        while line:
            line = line.rstrip()
            print line
            name_match = name_re.match(line)
            if name_match:
                internal_config['name'] = name_match.group(1)

            # Match function name "function : hello"
            function_match = function_re.match(line)
            if function_match:
                new_function = {'name':function_match.group(1), 'arguments':[]}

                while True:
                    line = config_file.readline().rstrip()
                    print line
                    # Match datatype to argument name "int : arg1"
                    arg_match = arg_re.match(line)
                    if arg_match:
                        type_name_pair = {'type':arg_match.group(1), 'name':arg_match.group(2)}
                        new_function['arguments'].append(type_name_pair)
                    else:
                        break

                internal_config['functions'].append(new_function)
            else:
                line = config_file.readline()

        return internal_config

if __name__ == '__main__':
    parser = ConfigurationParser()
    print(parser.parse('tests/test.config'))








