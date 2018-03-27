import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

setup(
    name = "kitchen-sink-logger",
    version = "0.0.9",
    author = "Troy Larson",
    author_email = "troylar@gmail.com",
    description = ("Easily log everything, including the kitchen sink, if that's your thing"),
    license = "MIT",
    keywords = "logging",
    url = "http://packages.python.org/kitchen-sink-logger",
    packages=find_packages(),
    long_description='here',
    classifiers=[
        'License :: OSI Approved :: MIT License'
    ],
)
