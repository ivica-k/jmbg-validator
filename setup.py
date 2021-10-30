#!/usr/bin/env python

__version__ = "1.0.0"

from distutils.core import setup
import setuptools

setup(
    name="JMBG Validator",
    version=__version__,
    description="Validira i ispisuje osnovne podatke o JMBGu. EN: Validates and displays basic UMCN data.",
    author="Ivica Kolenkaš",
    url="https://github.com/ivica-k",
    python_requires=">=3.7",
    packages=["jmbg_validator"],
    license="MPL2.0",
    setup_requires=["wheel"],
    package_dir={"jmbg_validator": "jmbg_validator"},
    entry_points={
        "console_scripts": ["jmbg-validator=jmbg_validator.main:cli"],
    },
)
