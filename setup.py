'''This file is used during installation of the package'''

#!/usr/bin/env python

import setuptools

setuptools.setup(name='f1pystats',
      version='1.0',
      description='Python Example Package',
      author='alec-kr',
      author_email='akramdhan02@gmail.com',
      packages=['f1pystats'],
      install_requires=[
          'requests', 'pandas'
      ]
)
