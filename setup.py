from setuptools import find_packages, setup

with open('requirements.txt') as fobj:
    install_requires = fobj.read().splitlines()

setup(
    name='django-simplewiki',
    version='0.1',
    description='A simple Wiki application for Django.',
    author='Berker Peksag',
    author_email='berker.peksag@gmail.com',
    url='https://github.com/berkerpeksag/django-simplewiki',
    packages=find_packages(),
    install_requires=install_requires,
    license='Mozilla Public License, v. 2.0',
    keywords='django wiki',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    ],
)
