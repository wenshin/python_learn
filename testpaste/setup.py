from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='testpaste',
      version=version,
      description="Test the paster tool usage",
      long_description="""\
Hei it is work""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='test, pastescript',
      author='wenshin',
      author_email='wenshin2011@gmail.com',
      url='www.knownsec.com',
      license='Apache 2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
