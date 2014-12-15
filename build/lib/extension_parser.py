import shelve
import re
class ExtensionParser:

    # Parses extension configuration file, throws Error if unsuccessful
    def parse(self,file_name):
        EXTENSION_DB = 'build/lib/extension.db'
        extension_file = open(file_name)
        # extension_dict = {'include':None, 
        #                     'data_type':None,
        #                     'num_vars':None, 
        #                     'format_string': None, 
        #                     'format_string_args': None,
        #                     'code': None,
        #                     'init': None
        #                      }
        extension_dict= {}

        # TODO: Parse stuff and put it in the DB
        include_re = re.compile('^include\s*:\s*([a-zA-Z_]+[a-zA-Z0-9_]+[^0-9_]*)$')
        dataType_re = re.compile('^data_type\s*:\s*([a-zA-Z_]+[a-zA-Z0-9_]*)$')
        numVars_re = re.compile('^num_vars\s*:\s*([a-zA-Z0-9_]*)$')
        formatString_re = re.compile('^format_string\s*:\s*([a-zA-Z0-9_]+[^0-9_]*)$')
        formatStringArgs_re = re.compile('^format_string_args\s*:\s*([^0-9_]+[a-zA-Z0-9_]+[^0-9_]+[a-zA-Z0-9_]*)$')
        init_re = re.compile('^init\s*:\s*([a-zA-Z_]+[a-zA-Z0-9_]+[^0-9_]*)$')
        code_re = re.compile('^code\s*:\s*')
        includeDirs_re = re.compile('^include_dirs*:\s*([a-zA-Z0-9_]+[^0-9_]+[a-zA-Z0-9_]+[^0-9_]*)$')
        setupImport_re = re.compile('^setup_import*:\s*([a-zA-Z0-9_]+[^0-9_]+[a-zA-Z0-9_]+[^0-9_]*)$')

        line = extension_file.readline()
        while line: 
            line = line.replace(' ', '')
            line = line.rstrip()
            print line
            include_match = include_re.match(line) 
            if include_match:
                # print("include_match")
                # print(include_match)
                includes = include_match.group(1)
                include = includes.split(',')
                extension_dict['include'] = include

            dataType_match = dataType_re.match(line)
            if dataType_match: 
                print("DATATYPE_MATCH")
                print(dataType_match)
                #extension_dict['data_type'] = dataType_match.group(1)
                data_type = dataType_match.group(1)

            numVars_match = numVars_re.match(line)
            if numVars_match:
                extension_dict['num_vars'] = numVars_match.group(1)

            formatString_match = formatString_re.match(line)
            if formatString_match:
                extension_dict['format_string'] = formatString_match.group(1)

            # append arguments to a list 
            formatStringArgs_match = formatStringArgs_re.match(line)
            if formatStringArgs_match:
                print("Argument 1???")
                args = formatStringArgs_match.group(1)
                names = args.split(',')
                extension_dict['format_string_args'] = names
                # extension_dict['format_string_args'][0] = numVars_match.group(1)
                # extension_dict['format_string_args'][1] = numVars_match_group(2)
                print("What is in format_string_arg")
                print(extension_dict['format_string_args'])

            init_match = init_re.match(line)
            if init_match:
                extension_dict['init'] = init_match.group(1)

            includeDirs_match = includeDirs_re.match(line)
            if includeDirs_match:
                includeDirs = includeDirs_match.group(1)
                includeDir = includeDirs.split(',')
                extension_dict['include_dirs'] = includeDir

            setupImport_match = setupImport_re.match(line)
            if setupImport_match:
                imports = setupImport_match.group(1)
                importList = imports.split(',')
                extension_dict['setup_import'] = importList

            # put "code" parsing in the dictionary
            code_match = code_re.match(line)
            if code_match:
                print 'here'
                code_segment = ''
                line = extension_file.readline()
                while line:
                    code_segment += line
                    line = extension_file.readline()
                extension_dict['code'] = code_segment
                print("Where are you code?")
                print(extension_dict['code'])
            line = extension_file.readline()

        print("extension_dict")
        print(extension_dict)
        # Write out to database
        db = shelve.open(EXTENSION_DB)
        try:
            db[data_type] = extension_dict
        finally:
            db.close()

        


