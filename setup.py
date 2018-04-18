#!/usr/bin/env python

from setuptools import setup

setup(name='tap-zendesk',
      version='0.0.1',
      description='Singer.io tap for extracting data from the Zendesk API',
      author='Stitch',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_zendesk'],
      install_requires=[
          'singer-python==5.0.15',
          'zenpy==2.0.0',
      ],
      entry_points='''
          [console_scripts]
          tap-zendesk=tap_zendesk:main
      ''',
      packages=['tap_zendesk'],
      package_data = {
          'tap_zendesk/schemas': [
            "tickets.json"
          ]
      },
      include_package_data=True,
)
