from setuptools import setup

setup(
    name='fixture_generator',
    version='0.0.2',
    packages=['fixture_generator'],
    url='https://github.com/Rhathe/Fixture_Generator',
    license='MIT',
    author='Ramon Sandoval',
    description='SqlAlchemy Fixture Generator',
    long_description='SqlAlchemy Fixture Generator',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ],

    install_requires=[
        'future >= 0.14.3, < 0.16',
        'SQLAlchemy',
    ],
)
