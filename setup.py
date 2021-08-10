# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 10:07:52 2021

@author: rockl
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="app-pkg-rockl",
    version="1.0.0",
    author= "Justin Paoli",
    author_email="justinpaolipbi@gmail.com",
    description="testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/apptest",
    project_urls={
        "YouTube Downloader": "https://github.com/pypa/apptest/test",
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
    )