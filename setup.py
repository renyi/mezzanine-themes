#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='mezzanine-themes',
    version='0.3',
    description='Mezzanine CMS themes',
    long_description=open('README.md').read(),
    author='Renyi Khor',
    author_email='renyi.ace@gmail.com',
    url='https://github.com/renyi/mezzanine-themes',
    packages=find_packages(),
    include_package_data = True,
    # install_requires=['mezzanine'],
)
