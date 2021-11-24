from setuptools import setup
import setuptools

setup(
    name="kroenekmdiffusion2D",
    version="0.0.1",
    author="kroenekm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kimkroener/Diffusion2D-Python-Package",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["matplotlib.pyplot", "numpy"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent"
    ]
)