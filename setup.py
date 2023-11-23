#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Maximillian Weil",
    author_email='maximillian.weil@vub.be',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python package to select data from scatter plots. The goal is to use specific selected data to train Machine Learning models.",
    entry_points={
        'console_scripts': [
            'data_selector=data_selector.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='data_selector',
    name='data_selector',
    packages=find_packages(include=['data_selector', 'data_selector.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/WEILMAX/data_selector',
    version='0.1.0',
    zip_safe=False,
)
