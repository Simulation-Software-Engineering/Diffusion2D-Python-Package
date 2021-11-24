from setuptools import setup
import setuptools

setup(
    name="diffusion2d",
    version="0.0.1",
    author="Max Hausch",
    description="Diffusion simulation",
    url="package-website-url",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=["matplotlib", "numpy"]
)
