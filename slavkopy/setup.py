try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='slavkopy',
    version='1.6',
    description='slavko.boy',
    author='slavko.boy',
    author_email='hello.slavko.melnyk@gmail.com',
    url='https://github.com/slavkomelnyk/slavkopy',
    packages=['slavkopy'],
    package_dir={'slavkopy': 'src/slavkopy'},
    package_data={'slavkopy': ['data/*.dat']},
    classifiers=[
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Topic :: Communications :: Email',
    ],
    install_requires=[
        'setuptools',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
