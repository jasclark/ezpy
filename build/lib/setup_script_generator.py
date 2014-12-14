class SetupScriptGenerator:
    def generate(self, config):
        script_string = """
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from distutils.core import setup, Extension

ext_modules = [ Extension('MODULE_NAME', sources = ['MODULE_NAME.c']) ]

setup(
        name = 'MODULE_NAME',
        version = '1.0',
        include_dirs = [],
        ext_modules = ext_modules
      )
"""

        script_string = script_string.replace('MODULE_NAME', config['name'])

        script = open(config['name'] + '_setup.py', 'w')
        script.write(script_string)


