#from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name="CoffeeFlavors",
    version="0.0.1",
    author='Zuzanna Klyszejko',
    author_email='zklyszejko@gmail.com',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    packages=find_packages(),
    long_description=open('README.md').read(),
    description="Code for automatic tagging for coffee reviews",
    url='https://github.com/zuzannna/CoffeeFlavors',
    keywords='nlp tagging matching nltk spacy coffee',
    include_package_data=True
)