#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import (setup, find_packages)

__version__ = '0.0.1'
__author__ = 'Agus Makmun (Summon Agus)'
__email__ = 'summon.agus@gmail.com'

setup(
    name='django-object-cloner',
    version=__version__,
    packages=find_packages(exclude=["*demo"]),
    include_package_data=True,
    zip_safe=False,
    description='Django Object Cloner',
    url='https://github.com/agusmakmun/django-object-cloner',
    download_url='https://github.com/agusmakmun/django-object-cloner/tarball/v%s' % __version__,
    keywords=['django object cloner', 'django cloner'],
    long_description=open('README.rst').read(),
    license='MIT',
    author=__author__,
    author_email=__email__,
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
    ]
)
