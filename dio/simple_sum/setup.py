from setuptools import setup, find_packages

with open("README.md") as f:
    page_description = f.read()


with open("requirements.txt") as f:
    requirements = f.read()


setup(
    name="simple_sum",
    version="0.0.1",
    author="joaooliveira247",
    description="simple sum package",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joaooliveira247/challenges/tree/main/dio/simple_sum",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.10",
)
