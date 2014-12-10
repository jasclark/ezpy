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