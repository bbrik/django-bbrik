# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import bbrik


setup(
    name='django-bbrik',
    version=bbrik.__version__,
    author=u'Bernardo Brik',
    author_email='bernardobrik@gmail.com',
    url='http://bitbucket.org/bruno/django-geoportail',
    description='Basic library used in all projects',
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(),
)
