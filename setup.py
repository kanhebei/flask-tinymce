# -*- coding: utf-8 -*-
"""
Flask-TinyMCE
--------------
TinyMCE integration for Flask
Features:
* 1
* 2
* 3
* 4
* 5
* 6
"""

import re
import os

from setuptools import setup


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)

def read(fname):
    return open(fpath(fname), encoding='utf-8').read()

file_text = read(fpath('flask_tinymce/__init__.py'))

def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval

setup(
    name='Flask-TinyMCE',
    version=grep('__VERSION__'),
    url='https://github.com/kanhebei/flask-tinymce',
    license='MIT',
    author=grep('__AUTHOR__'),
    author_email=grep('__EMAIL__'),
    description='Flask-TinyMCE',
    long_description=__doc__,
    packages=['flask_tinymce'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)