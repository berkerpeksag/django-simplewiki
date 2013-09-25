from distutils.core import setup


setup(
    name='django-simplewiki',
    version='0.1-dev',
    description='A simple Wiki application for Django.',
    long_description='',
    author='Berker Peksag',
    author_email='berker.peksag@gmail.com',
    url='https://github.com/berkerpeksag/django-simplewiki',
    packages=['simplewiki'],
    platforms='any',
    license='Mozilla Public License, v. 2.0',
    keywords='django wiki',
    classifiers=(
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    ),
)
