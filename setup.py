#!/usr/bin/env python

from distutils.core import setup

setup(
    name="JMBG Validator",
    version="1.0",
    description="Validira i ispisuje osnovne podatke o JMBGu",
    author="Ivica Kolenkaš",
    url="https://github.com/ivica-k",
    packages=["jmbg_validator"],
    license="MPL2.0",
    package_dir={"jmbg_validator": "jmbg_validator"},
    entry_points={
        "console_scripts": ["jmbg-validator=jmbg_validator.main:cli"],
    },
)
