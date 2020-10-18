"""
A Better HomeBrew Package Search

Usage: brewls [keyword]

"""

from setuptools import setup

setup(name='rename',
      version='0.1',
      description='Python - rename multiple files via modification rules',
      url='http://github.com/kkatayama/rename',
      author='Teddy',
      author_email='katayama@udel.edu',
      license='MIT',
      packages=['rename'],
      python_requires='>=3',
      scripts=['bin/rename'],
      zip_safe=False)
