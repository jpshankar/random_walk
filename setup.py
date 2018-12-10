from setuptools import setup, find_packages

setup(
    name='randomWalk',
    version='1.1.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Implementation of RandomWalk',
    long_description=open('README.txt').read(),
    url='https://github.com/jpshankar/random_walk',
    author='Javas Shankar',
    author_email='javasshankar@gmail.com',
	setup_requires=['pytest-runner'],
	tests_require=['pytest']
)
