from setuptools import find_packages, setup

setup(
    name='django-simplewiki',
    version='0.1',
    description='A simple Wiki application for Django.',
    author='Berker Peksag',
    author_email='berker.peksag@gmail.com',
    url='https://github.com/berkerpeksag/django-simplewiki',
    packages=find_packages(),
    zip_safe=False,
    license='Mozilla Public License, v. 2.0',
    keywords='django, wiki',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    ],
)
