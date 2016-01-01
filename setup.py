from setuptools import setup

setup(
    name='selenium-extra-api',
    version='0.0.1',
    descritption='selenium-extra-api add method to the existing API.',
    long_description=open('README.rst').read(),
    author='Pierre Verkest',
    author_email='pverkest@anybox.fr',
    url='https://github.com/petrus-v/selenium-extra-api',
    packages=['selenium_extra'],
    install_requires=[
        'selenium',
        'pyyaml',
    ],
    license='Mozilla Public License 2.0 (MPL 2.0)',
    keywords='nose selenium CI',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7']
)
