from setuptools import setup
import setuptools

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name="diffusion2d",
    version="0.0.1",
    author="Max Hausch",
    description="Diffusion simulation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="package-website-url",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=["matplotlib", "numpy"]
)
