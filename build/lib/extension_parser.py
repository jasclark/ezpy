import shelve

class ExtensionParser:

    CONVERSION_DB = 'conversion.db'

    # Parses extension configuration file, throws Error if unsuccessful
    def parse(file_name):
        extension_file = open(file_name)
        
        # TODO: Parse stuff and put it in the DB

        # For now...
        data_type = None
        conversion_function = None

        # Write out to database
        db = shelve.open(CONVERSION_DB)
        try:
            db[data_type] = conversion_function
        finally:
            db.close()

        


