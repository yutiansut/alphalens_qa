#!/usr/bin/env python
from setuptools import setup, find_packages
import sys

long_description = ''

if 'upload' in sys.argv:
    with open('README.rst') as f:
        long_description = f.read()

install_reqs = [
    'matplotlib>=1.4.0',
    'numpy>=1.9.1',
    'pandas>=0.18.0',
    'scipy>=0.14.0',
    'seaborn>=0.6.0',
    'statsmodels>=0.6.1',
    'IPython>=3.2.3',
    'empyrical>=0.5.0',
]

extra_reqs = {
    'test': [
        "nose>=1.3.7",
        "parameterized>=0.5.0",
        "tox>=2.3.1",
        "flake8>=3.7.9",
    ],
}

if __name__ == "__main__":
    setup(
        name='alphalens_qa',
        version='0.2.0',
        #cmdclass=versioneer.get_cmdclass(),
        description='Performance analysis of predictive (alpha) stock factors',
        packages=find_packages(include='alphalens.*'),
        url='https://github.com/yutiansut/alphalens',
        install_requires=install_reqs,
        extras_require=extra_reqs,
    )
