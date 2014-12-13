import re

class ConfigurationParser:

    # Creates an internal dictionary representation of the config file:
    # {
    #     'name' : 'function_name',
    #     'functions' : [
    #                     {
    #                         'name':'function1',
    #                         'arguments': [
    #                             {'type':'O!', 'name':['arg1', 'arg2']},
    #                             {'type':'s', 'name':['arg2']},
    #                         ] 
    #                     },
    #                     {
    #                         'name':'function2',
    #                         'arguments': [
    #                             {'type':'int', 'name':'arg3'},
    #                             {'type':'string', 'name':'arg4'},
    #                         ] 
    #                     },
    #                 ]
    # }

    def parse(self, file_name):
        config_file = open(file_name)
        internal_config = {'name':None, 'functions':[]}

        name_re = re.compile('^name\s*:\s*([a-zA-Z0-9_.]+)$')
        function_re = re.compile('^function\s*:\s*([a-zA-Z_]+[a-zA-Z0-9_]*)$')
        arg_re = re.compile('^(\S+)\s*:\s*([a-zA-Z_]+[a-zA-Z0-9_,]*)$')
        return_re = re.compile('^return:(\S+)$')

        line = config_file.readline()

        while line:
            line = line.replace(' ', '')
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
                    line = line.replace(' ', '')
                  
                    return_match = return_re.match(line)
                    if return_match:
                        print 'returned'
                        new_function['return'] = return_match.group(1)
                        break

                    arg_match = arg_re.match(line)
                    if arg_match:
                        names = arg_match.group(2).split(',')
                        type_name_pair = {'type':arg_match.group(1), 'name':names}
                        new_function['arguments'].append(type_name_pair)

                    else:
                        break

                internal_config['functions'].append(new_function)
            else:
                line = config_file.readline()
        print internal_config
        return internal_config








