import shelve

#!/usr/bin/env python

PROJECT = 'ezpy'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=0.1,

    description='Scaffolding tool for the Python/C API',
    long_description=long_description,

    author='',
    author_email='',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'ezpy = main:main'
        ],
        'ezpy': [
            'generate = ezpy:Generate',
            'extend = ezpy:Extend'
        ],
    },

    zip_safe=False,
)

db = shelve.open('build/lib/format_string')
try: 
    db['s'] = ['const char *']
    db['s#'] = ['const char *', 'int ']
    db['s*'] = ['Py_buffer ']
    db['z'] = ['const char *']
    db['z#'] = ['const char *, int ']
    db['z*'] = ['Py_buffer ']
    db['u'] = ['Py_UNICODE *']
    db['u#'] = ['Py_UNICODE *', 'int ']
    db['es'] = ['const char *encoding', 'char **buffer']
    db['et'] = ['const char *encoding', 'char **buffer']
    db['es#'] = ['const char *encoding', 'char **buffer', 'int *buffer_length']
    db['et#'] = ['const char *encoding', 'char **buffer', 'int *buffer_length']
    db['b'] = ['unsigned char ']
    db['B'] = ['unsigned char ']
    db['h'] = ['short int ']
    db['H'] = ['unsigned short int ']
    db['i'] = ['int ']
    db['I'] = ['unsigned int ']
    db['l'] = ['long int ']
    db['k'] = ['unsigned long ']
    db['L'] = ['PY_LONG_LONG ']
    db['K'] = ['unsigned PY_LONG_LONG ']
    db['n'] = ['Py_ssize_t ']
    db['c'] = ['char ']
    db['f'] = ['float ']
    db['d'] = ['double ']
    db['D'] = ['Py_complex ']
    db['O'] = ['PyObject *']
    db['O!'] = ['typeobject ', 'PyObject *']
    db['O&'] = ['converter', 'anything']
    db['S'] = ['PyStringObject *']
    db['U'] = ['PyUnicodeObject *']
    db['t#'] = ['char *', 'int ']
    db['w'] = ['char *']
    db['w#'] = ['char *', 'Py_ssize_t ']
    db['w*'] = ['Py_buffer ']
    db['(items)'] = ['matching-items']
finally: 
    db.close()
