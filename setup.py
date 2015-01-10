# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


version = '0.2dev'

long_description = (
    read('README.rst')
    + '\n' +
    read('docs/CREDITS.txt')
    + '\n' +
    read('docs/TODO.txt')
    + '\n' +
    read('docs/HISTORY.txt')
    )

setup(name='mr.inquisition',
      version=version,
      description="A package to help with exploring a Plone site.",
      long_description=long_description,
      classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Mark van Lent',
      author_email='mark@vlent.nl',
      url='https://github.com/collective/mr.inquisition',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['mr'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target=plone
      """,
      )