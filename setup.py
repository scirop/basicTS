from setuptools import setup, find_packages
import os

f = open(os.path.join(os.path.dirname(__file__), 'readme.md'))
readme = f.read()
f.close()

setup(
    name='basicTS',
    version='0.0.0.1',
    description='Basic Time-Series functions',
    long_description=readme,
    author='Swarup Sahoo',
    author_email='swarupsahoo@utexas.edu',
    url='https://github.com/scirop/basicTS',
    packages=find_packages(),
    install_requires=[
        'numpy'
    ],
    license='BSD License',
    platforms=["any"],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
