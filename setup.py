import re
import ast
from codecs import open
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('jsonconfig/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='jsonconfig-tool',
    python_requires='>=2.7',
    version=version,
    description='Configuration made easy: JSON, encrypted, envvars, etc.',
    long_description=readme,
    license='MIT',
    author='Brian Peterson',
    author_email='bpeterso2000@yahoo.com',
    keywords='config configuration json encryption passwords simple easy',
    url='http://github.com/json-transformations/jsonconfig',
    packages=['jsonconfig'],
    classifiers=[
         'License :: OSI Approved :: MIT License',
         'Intended Audience :: Developers',
         'Topic :: Software Development',
         'Topic :: Utilities',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'click>=6.7',
        'python-box>=3.1.1',
        'keyring>=12.0.1',
        'pywin32-ctypes>=0.1.2; platform_system="Windows"',
        'dbus-python>=1.2.4; platform_system=="Linux"',
    ],
)
