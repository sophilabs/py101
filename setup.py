#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    name='py101',
    version='0.0.2',
    description='Learn Python Basics from the command line.',
    long_description=readme + '\n\n' + history,
    author='Sophilabs',
    author_email='hi@sophilabs.co',
    url='https://github.com/sophilabs/py101',
    packages=['py101'],
    entry_points={
        'console_scripts': [
            'py101=py101:Story.begin'
        ]
    },
    include_package_data=True,
    install_requires=[
        'story>=1.2.3'
    ],
    python_requires='!=2, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    license='MIT license',
    zip_safe=False,
    keywords='py101',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=[]
)
