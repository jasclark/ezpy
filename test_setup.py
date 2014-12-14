
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from distutils.core import setup, Extension

ext_modules = [ Extension('test', sources = ['test.c']) ]

setup(
        name = 'test',
        version = '1.0',
        include_dirs = [],
        ext_modules = ext_modules
      )
