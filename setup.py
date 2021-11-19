from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="chinhalidiffusion2D",
    version="0.0.1",
    author="Chin-Han Lai",
    description="A 2D diffusion solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chlai1012/Diffusion2D-Python-Package.git",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["NumPy","Matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: Microsoft :: Windows",
    ],
)