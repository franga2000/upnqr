#!/bin/env python3
from setuptools import setup

setup(
    name="upnqr",
    version="0.1.0",
    description="",
    long_description="",
    url="https://github.com/franga2000/upnqr",
    author="Miha Frangež",
    author_email="miha.frangez@gmail.com",
    license="GPLv3",
    packages=["upnqr"],
    install_requires=[
        'pydantic',
        'qrcodegen',
        'Pillow',
    ],
)

