# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyencrypt',
    version='0.0.4',
    description='Simple file encryptor using python',
    long_description=readme,
    author='Christian Paling',
    author_email='christian.paling@googlemail.com',
    url='https://github.com/bakku/pyencrypt',
    license=license,
    packages=['pyencrypt'],
    install_requires=['pycrypto'],
    entry_points={
        'console_scripts': [
            'pyencrypt = pyencrypt.__main__:main'
        ]
    }
)
