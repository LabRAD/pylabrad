"""LabRAD interface for python

LabRAD is a system for quickly and easily building distributed
instrument control and data analysis applications.  pylabrad
provides a python interface to LabRAD.
"""

classifications = """\
Development Status :: 4 - Beta
Environment :: Console
Environment :: Web Environment
Intended Audience :: Science/Research
License :: OSI Approved :: GNU General Public License (GPL)
Operating System :: OS Independent
Programming Language :: Python
Topic :: Scientific/Engineering"""

import numpy as np
import os
from setuptools import setup, find_packages, Extension

doclines = __doc__.split('\n')

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    requirements = f.readlines()

setup(
    name='pylabrad',
    author='Matthew Neeley',
    author_email='mneeley@gmail.com',
    license='http://www.gnu.org/licenses/gpl-2.0.html',
    platforms=['ANY'],

    url='https://github.com/labrad/pylabrad/',
    download_url='',

    description=doclines[0],
    long_description='\n'.join(doclines[2:]),
    classifiers=classifications.split('\n'),

    setup_requires=['setuptools_scm'],
    use_scm_version={
        'write_to': 'labrad/version.py'
    },

    install_requires=requirements,
    provides=['labrad'],
    packages=find_packages(),
    include_dirs = [np.get_include()],
    package_data={
        'labrad': ['LICENSE.txt'],
        'labrad.node': ['*.ini'],
    },
    scripts=[],
    ext_modules=[Extension("fastunits.unitarray", 
                             sources = ["fastunits/unitarray.c"])]
)
