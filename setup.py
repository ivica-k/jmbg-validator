#!/usr/bin/env python

__version__ = "0.0.1"

from distutils.core import setup

setup(
    name="JMBG Validator",
    version=__version__,
    description="Validira i ispisuje osnovne podatke o JMBGu. EN: Validates and displays basic UMCN data.",
    author="Ivica Kolenkaš",
    url="https://github.com/ivica-k",
    packages=["jmbg_validator"],
    license="MPL2.0",
    package_dir={"jmbg_validator": "jmbg_validator"},
    entry_points={
        "console_scripts": ["jmbg-validator=jmbg_validator.main:cli"],
    },
)
