#!/usr/bin/env python

from setuptools import setup, find_packages

pkg = 'w7min'

_c_scripts = ['w7min=w7min.w7min:main']

setup(name='w7min',
      version='0.1',
      description='The scientific 7 minute workout',
      url='http://github.com/cjbayesian/7min',
      author='Corey Chivers',
      author_email='corey.chivers@mail.mcgill.ca',
      license='MIT',
      package_dir={pkg: pkg},
      package_data={pkg: ['data/*']},
      entry_points={'console_scripts':_c_scripts},
      packages=find_packages(),
      )


