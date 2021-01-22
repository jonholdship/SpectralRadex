import setuptools  # this is the "magic" import
from numpy.distutils.core import setup, Extension
from numpy.distutils import exec_command
from glob import glob
import os
with open("README.md", "r") as fh:
    long_description = fh.read()

DATA_DIR="src/spectralradex/radex/data/"

#exec_command.exec_command( "make python", execute_in='src/radex_src/', use_shell=True)
if not os.getenv('READTHEDOCS'):
    radexwrap = Extension(name = 'radexwrap',
                     sources = ['src/radex_src/'+x for x in ['types.f90','commondata.f90','slatec.f90',
                     'solver.f90','background.f90','io.f90','wrap.f90','radexwrap.pyf']])
    ext_mods=[radexwrap]
else:
    ext_mods=[]

setup(
    name="spectralradex", # Replace with your own username
    version="0.0.2",
    author="Jonathan Holdship",
    author_email="jonholdship@gmail.com",
    description="A package for RADEX and spectral modelling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonholdship/spectralradex",
    ext_modules = ext_mods,
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    data_files=[("spectralradex/radex/data",glob(DATA_DIR))],
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['numpy','pandas']
)