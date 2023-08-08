from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['my-command=my_module.main:cli'],
    },
)
