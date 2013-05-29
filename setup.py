import os, sys

__version__ = "0.1.0"

from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='EmbedCore',
      version=__version__,
      description="A Python implementation of various embedded routines.",
      long_description=read('README.md'),
      keywords="Raspberry Pi python",
      author='Carl J. Nobile',
      author_email='carl.nobile@gmail.com',
      maintainer='Carl J. Nobile',
      maintainer_email='carl.nobile@gmail.com',
      url='https://github.com/cnobile2012/embedcore',
      license='',
      classifiers=[
          "Intended Audience :: Developers",
          "License :: OSI Approved",
          "Natural Language :: English",
          "Programming Language :: Python :: 2.7",
          "Topic :: Software Development :: Libraries :: Python Modules :: Embedded",
          ],
      download_url="https://github.com/cnobile2012/embedcore/archive/master.zip",
      platforms=["Linux",],
      py_modules=['board.__init__',
                  'board.rpi.__init__', 'board.rpi.raspberry_pi',],
      #data_files=[('board/tests',)
      #           ],
      zip_safe=True
      )
