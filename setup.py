#!/usr/bin/env python3

import os
from setuptools import setup

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="R400ForVN",
    version="0.0.1",
    author="Raphaël Margueron",
    author_email="raphael.margueron@gmail.com",
    description=(
        "Remap Logitech R400 controller inputs for stardard visual novel keys"),
    license="",
    keywords="",
    install_requires=requirements,
    url="https://github.com/TheRaphael0000/R400ForVN",
    packages_data={"main.py"},
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    entry_points={
        'console_scripts': [
            'R400ForVN=main:main'
        ]
    }
)
