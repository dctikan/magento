#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    Magento API

    :copyright: (c) 2010 by Sharoon Thomas.
    :copyright: (c) 2010-2013 by Openlabs Technologies & Consulting (P) LTD
    :license: AGPLv3, see LICENSE for more details

'''
import os
from setuptools import setup

exec(open(os.path.join('magento', 'version.py')).read())

setup(
    name = 'magento',
    version=VERSION,
    url='https://github.com/openlabs/magento/',
    license='GNU Affero General Public License v3',
    author='Sharoon Thomas, Openlabs Technologies',
    author_email='info@openlabs.co.in',
    description='Magento Core API Client',
    long_description=open('README.rst').read(),
    packages=['magento'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'suds-jurko',
    ],
    classifiers=[
        'Development Status :: 6 - Mature',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

