class SetupScriptGenerator:
    def generate(self, config):
        script_string = """
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from distutils.core import setup, Extension
SETUP_IMPORTS

ext_modules = [ Extension('MODULE_NAME', sources = ['MODULE_NAME.c']) ]

setup(
        name = 'MODULE_NAME',
        version = '1.0',
        include_dirs = [DIRS],
        ext_modules = ext_modules
      )
"""
        include_dirs = ''
        for include_dir in config['include_dirs']:
            include_dirs += include_dir + ', '

        setup_imports = ''
        for setup_import in config['setup_import']:
            setup_imports += setup_import

        script_string = script_string.replace('MODULE_NAME', config['name'])
        script_string = script_string.replace('DIRS', include_dirs)
        script_string = script_string.replace('SETUP_IMPORTS', setup_imports)

        script = open(config['name'] + '_setup.py', 'w')
        script.write(script_string)



