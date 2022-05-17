#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pylsd',
    version='1.1',
    description='pylsd is the python bindings for LSD - Line Segment Detector',
    long_description=long_description,
    author='Tejas M R',
    author_email='totejasmr@gmail.com',
    license='BSD',
    keywords="LSD",
    url='https://github.com/tezz-io/pylsd',
    packages=['pylsd', 'pylsd.bindings', 'pylsd.lib'],
    package_dir={'pylsd.lib': 'pylsd/lib'},
    package_data={'pylsd.lib': [
        'darwin/*.dylib', 'win32/x86/*.dll', 'win32/x64/*.dll', 'linux/*.so', 'linux_arm/*so']},
)
