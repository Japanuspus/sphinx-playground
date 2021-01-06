from setuptools import setup, find_packages

setup(
    name="my_project",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    version="0.0",
)