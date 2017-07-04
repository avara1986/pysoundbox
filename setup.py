# -*- coding: utf-8 -*-
# Copyright (c) 2017 by Alberto Vara <a.vara.1986@gmail.com>
import os
from setuptools import setup, find_packages


def read(file):
    return open(os.path.join(os.path.dirname(__file__), file))


setup(
    name="Pysoundbox",
    version="0.0.1",
    author="Alberto Vara",
    author_email="a.vara.1986@gmail.com",
    description="Sound box in python",
    long_description=(read('README.md').read() + '\n\n' + read('CHANGES.rst').read()),
    classifiers=[
        "Development Status :: 1 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5"
        "Programming Language :: Python :: 3.6"
    ],
    license="MIT",
    platforms=["any"],
    keywords="python, sounds",
    url='https://github.com/avara1986/pysoundbox.git',
    test_suite='nose.collector',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pysoundbox = main'
        ]
    },
    zip_safe=True,
)
