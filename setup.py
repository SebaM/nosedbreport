"""                                                                                                                                                                                                         
setup.py for nosedbreport
 
 
"""
__author__ = "Ali-Akber Saifee"
__email__ = "ali@mig33global.com"
__copyright__ = "Copyright 2011, ProjectGoth"

from setuptools import setup, find_packages

setup(
    name='NoseDBResult',
    version='0.1',
    description='Nose plugin for recording test results to a database',
    long_description=open('README.rst').read(),
    entry_points = {
        'nose.plugins.0.10': [
            'nosedbreport = nosedbreport:NoseDBReporter']
        },
    install_requires = ['sphinx.ext.autodoc','sphinx.ext.inheritance_diagram', 'sphinx.ext.viewcode'],
    packages = ['nosedbreport'],
)

