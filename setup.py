# -*- coding: utf-8 -*-

'''
setup for ifxuser

Created on  2018-12-21

@author: Aaron Kitzmiller <aaron_kitzmiller@harvard.edu>
@copyright: 2018 The Presidents and Fellows of Harvard College. All rights reserved.
@license: GPL v2.0
'''

import re
from setuptools import setup, find_packages


def getVersion():
    """
    Retrieve the version number from the __init__ file
    """
    version = '0.0.0'
    with open('ifxurls/__init__.py', 'r') as f:
        contents = f.read().strip()

    m = re.search(r"__version__ = '([\d\.]+)'", contents)
    if m:
        version = m.group(1)
    return version


setup(
    name="ifxurls",
    version=getVersion(),
    author='Aaron Kitzmiller <aaron_kitzmiller@harvard.edu>',
    author_email='aaron_kitzmiller@harvard.edu',
    description='User model for Informatics applications',
    license='LICENSE',
    include_package_data=True,
    url='https://github.com/harvardinformatics/ifxurls',
    packages=find_packages(),
    long_description='URLs for FAS Informatics services',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    entry_points={
        'console_scripts': [
            'getIfxUrl=ifxurls.urls:main',
        ]
    },
)
