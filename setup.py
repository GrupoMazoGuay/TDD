# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Verificacion y Desarrollo',
    long_description=readme,
    author='Enrique Sanchez',
    author_email='enrique.sanchez@u-tad.live.com',
    packages=find_packages(exclude=('tests', 'docs'))
)