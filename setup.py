#!/usr/bin/env python

from distutils.core import setup

setup(name='f1pystats',
      version='1.0',
      description='Python Example Package',
      author='alec-kr',
      author_email='akramdhan02@gmail.com',
      packages=['f1pystats'],
      install_requires=[
          'requests', 'pandas'
      ]
     )
