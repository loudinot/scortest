# -*- coding: utf-8 -*-
import os
from distutils.core import setup
from setuptools import find_packages

here = os.path.dirname(__file__)
packages = find_packages(where=here)
package_dir = {k: os.path.join(here, k.replace(".", "/")) for k in packages}


setup(name='scoretest',
      version='0.1',
      description="first try",
      author='Xavier Dupré',
      author_email='xadupre@microsoft.com',
      url='https://github.com/xadupre/scortest',
      packages=packages,
      package_dir=package_dir)
