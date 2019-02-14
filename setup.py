"""
setup.py is used similar as a makefile in c. It complies .pyx files into
.so files (on mac) (.pyd files on windows) that are used for importing into
.py files

To build:
$ python setup.py build_ext --inplace
"""


from distutils import setup
from Cython.Build import cythonize

setup(
    ext_module=cythonize("chords.pyx")
)
