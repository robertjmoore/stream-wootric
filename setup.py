#!/usr/bin/env python

from setuptools import setup, find_packages
import os.path

setup(name='stream-wootric',
      version='0.0.1',
      description='Streams wootric data',
      author='Stitch',
      url='https://github.com/robertjmoore/stream-wootric',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['stream_wootric'],
      install_requires=['stitchstream-python>=0.4.2',
                        'requests==2.12.4'],
      entry_points='''
          [console_scripts]
          stream-wootric=stream_wootric:main
      '''
)
