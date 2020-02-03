"""
    Flask-TinyMce
    @Time    : 2020/2/1 11:29
    @Author  : wumao
    @Email   : kanhebei@dingtalk.com

    pip install Flask_TinyMce

    from flask_tinymce import TinyMce


    tiny_mce = Tinymce(app)

    or

    tiny_mce = Tinymce()
    tiny_mce.init_app(app)



"""
from setuptools import setup


setup(
    name='Flask-TinyMce',
    version='0.1.4',
    url='https://github.com/kanhebei/flask-tinymce',
    license='MIT',
    author='WuMao',
    author_email='kanhebei@dingtalk.com',
    description='flask tinymce',
    long_description=__doc__,
    packages=['flask_tinymce'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'WTForms'
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