#!/usr/bin/env python
from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(
    name='django-admin-actions',
    description='Display Django admin custom actions in change list, change form or per row in change list.',
    short_description='Display Django admin custom actions in change list, change form or per row in change list.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.1',
    url='http://github.com/lukasvinclav/django-admin-actions',
    packages=[
        'admin_actions',
    ],
    include_package_data=True,
    install_requires=('django', ),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
    ],
    keywords="django admin actions"
)
