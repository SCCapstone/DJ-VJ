"""
setup.py is used similar as a makefile in c. It complies .pyx files into
.so files (on mac) (.pyd files on windows) that are used for importing into
.py files

To build:
$ python setup.py build_ext --inplace
"""

from distutils.core import setup, Extension
from Cython.Build import cythonize

extensions = Extension("djvj.chord_detection.chromagram", [
    "djvj/chord_detection/chromagram.pyx"],)

setup(

    ext_modules=cythonize(extensions)
)
