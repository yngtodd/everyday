#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


setup(
    name='everyday',
    version='0.0.1',
    description="Goal calendar based on Simone Giertz's Everyday Calendar.",
    author='Todd Young',
    author_email='youngmt1@ornl.gov',
    url='https://github.com/yngtodd/everyday',
    packages=[
        'everyday',
    ],
    package_dir={'everyday': 'everyday'},
    include_package_data=True,
    install_requires=[
        'terminaltables',
    ],
    license='MIT',
    zip_safe=False,
    keywords='everyday',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
