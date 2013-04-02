#!/usr/bin/env python
from setuptools import setup, find_packages

NAME = 'mezzanine-themes'

VERSION = '1.0'

DESCRIPTION = """
Mezzanine CMS themes and plugins.
"""

setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    version=VERSION,
    author='Renyi Khor',
    author_email='renyi.ace@gmail.com',
    url='https://github.com/renyi/mezzanine-themes',
    packages=find_packages(),
    include_package_data = True,
    zip_safe=False,
    # install_requires=['mezzanine'],
)
