# -*- coding: utf-8 -*-
from pathlib import Path
from setuptools import find_packages, setup


setup(
    name='email-validate',
    version='1.0.2',
    packages=find_packages(exclude=['tests']),
    install_requires=['dnspython~=2.0', 'idna~=3.0', 'filelock~=3.0'],
    author='CPILab',
    author_email='hello@containerpi.com',
    description=('Email validator with regex, blacklisted domains and SMTP checking.'),
    long_description=Path(__file__).parent.joinpath('README.md').read_text(),
    long_description_content_type='text/x-rst',
    keywords='email validation verification mx verify',
    url='https://github.com/containerpi/email_validate',
    license='MIT')
