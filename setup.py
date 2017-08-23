import re
import ast
from setuptools import setup

requirements = ['click==6.7', 'python-box==3.0.1', 'keyring==10.4.0']
test_requirements = ['flake8', 'pytest-cov', 'sphinx']

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('jsonconfig/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='jsonconfig-tool',
    version=version,
    author='Brian Peterson',
    author_email='bpeterso2000@yahoo.com',
    keywords='config configuration json encryption passwords simple easy',
    url='http://github.com/json-transformations/jsonconfig',
    packages=['jsonconfig'],
    description='Configuration made easy: JSON, encrypted, environ vars, etc.',
    classifiers=['License :: OSI Approved :: MIT License',
                 'Topic :: Software Development',
                 'Topic :: Utilities',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 3',
                 'Environment :: Win32 (MS Windows)',
                 'Environment :: MacOS X',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 ],
    install_requires=requirements,
    tests_require=test_requirements
)
