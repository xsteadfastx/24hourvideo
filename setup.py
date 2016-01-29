"""
24hourvideo
-----------

A copy of `24 Hour Psycho`_ by Douglas Gordon written in Python.

.. _24 Hour Psycho: https://en.wikipedia.org/wiki/24_Hour_Psycho

"""


from setuptools import setup
import ast
import re


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('twentyfourhourvideo/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='24hourvideo',
    version=version,
    url='https://github.com/xsteadfastx/24hourvideo',
    license='MIT',
    author='Marvin Steadfast',
    author_email='marvin@xsteadfastx.org',
    description='Play videos 24 hour long',
    long_description=__doc__,
    packages=['twentyfourhourvideo'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            '24hourvideo = twentyfourhourvideo.cli:cli'
        ]
    }
)
