# @Time    : 2020/2/2 16:04
# @Author  : wumao
# @Email   : kanhebei@dingtalk.com

from setuptools import setup

setup(
    name='Flask-TinyMce',
    version='1.0',
    url='http://example.com/flask-sqlite3/',
    license='MIT',
    author='WuMao',
    author_email='kanhebei@dingtalk.com',
    description='flask tinymce',
    long_description=__doc__,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
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