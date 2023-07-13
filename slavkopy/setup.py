from distutils.core import setup

setup(name='slavkopy',
    version='1.4',
    description='slavko.boy',
    author='slavko.boy',
    author_email='hello.slavko.melnyk@gmail.com',
    # url='https://www.python.org/sigs/distutils-sig/',
    packages=['slavkopy'],
    package_dir={'slavkopy': 'src/slavkopy'},
    package_data={'slavkopy': ['data/*.dat']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',

        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Communications :: Email',
    ],
    )
