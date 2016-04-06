from setuptools import setup, find_packages
from makeappmessages import __version__

github_url = ''
long_desc = open('README.md').read()

setup(
	name='django-makeappmessages',
	version='.'.join(str(v) for v in __version__),
	description='Create local message files for any app inside project directory',
	long_description=long_desc,
	url=github_url,
	author='Anton Evstigneev',
	author_email='kshatra.9@gmail.com',
	packages=find_packages(),
	include_package_data=True,
	license='MIT License',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Environment :: Web Environment',
		'Framework :: Django',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Software Development :: Libraries :: Python Modules'
	],
	#package_data={'makeappmessages': ['management/commands/makeappmessages.py']},
)
