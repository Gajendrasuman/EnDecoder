from setuptools import setup, find_packages
import codecs
import os


VERSION = '2.0.2'
DESCRIPTION = 'This package is used to encrypt or decrypt the data'

# Setting up
setup(
    name="EnDecoder",
    version=VERSION,
    author="GS Tech",
    author_email="Gajendrasuman868@gmail.com",
    description=DESCRIPTION,
    url="https://github.com/Gajendrasuman/EnDecoder",
    license="MIT"
    packages=find_packages(),
    install_requires=[],
    keywords=['encrypt','decrypt'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
