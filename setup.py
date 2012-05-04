try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
def read(fname):
    return open(fname).read()

setup(
    name = "clui",
    version = "1.0",
    author = "Luis Naranjo",
    author_email = "luisnaranjo733@hotmail.com",
    description = ("A customizable command line user interface."),
    license = "GNU GPL3",
    url = "https://github.com/doubledubba/clui",
    keywords = "CLUI clui ui command line user interface",
    #entry_points = {
    #'console_scripts': ['skel = skel:main']
    #},
    py_modules = ['clui'],
    scripts = ['clui.py'],
    platforms = 'any',
    #long_description=read('docs/index.rst'),
    #packages=['skeleton'],
    #include_package_data = True,
    #package_data = {
    #    'skeleton': ['docs','setup.py'],
    #}
)
