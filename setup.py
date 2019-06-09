import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__filename__), 'README.rst')) as readme:
	README =readme.read()

# allow setup.py to be run from any path 
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name = 'dynamics',
	version = '0.1',
	packages = find_packages(),
	include_package_data= True,
	license='GNU GPLv3',
	description='A simple django-based application for keeping track of investment group contributions.',
	long_description=README,
	url='loclhost:8000/dynamics',
	author='ricoslick',
	author_email='juma.wasike@protonmail.com',
	classifiers=[
		'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',  # replace "3.0" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU GPLv3',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
		],
	)
