#!/usr/bin/env python

__version__ = "1.0.1"

from distutils.core import setup
import setuptools

setup(
    name="JMBG Validator",
    version=__version__,
    description="Validira i ispisuje osnovne podatke o JMBGu. EN: Validates and displays basic UMCN data.",
    author="Ivica Kolenkaš",
    author_email="ivica.kolenkas@gmail.com",
    url="https://github.com/ivica-k/jmbg-validator",
    python_requires=">=3.7",
    packages=["jmbg_validator"],
    license="MPL2.0",
    setup_requires=["wheel"],
    package_dir={"jmbg_validator": "jmbg_validator"},
    entry_points={
        "console_scripts": ["jmbg-validator=jmbg_validator.main:cli"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
