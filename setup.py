import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="camelcase",
    version="5.3.1",
    description="Convert strings to camelCase",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/donkeyDau/camelcase",
    author="donkeyDau",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["camelcase"],
    include_package_data=False,
    install_requires=[],
)
