import re
import os
import sys

from setuptools import setup


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)

def read(fname):
    return open(fpath(fname)).read()

def desc():
    info = read('README.md')
    try:
        return info + '\n\n' + read('doc/changelog.rst')
    except IOError:
        return info

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
    long_description=desc(),
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