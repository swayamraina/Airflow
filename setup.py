
# This file contains the setup instructions for 
# the project.
#
# @author  Swayam Raina


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="airflow",
    version="0.0.1",
    author="Swayam Raina",
    author_email="swayamraina@gmail.com",
    description="A CLI for server utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swayamraina/airflow",
    packages=setuptools.find_packages(),
    classifiers=(
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)