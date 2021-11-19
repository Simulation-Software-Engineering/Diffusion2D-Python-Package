from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: European Union Public Licence 1.1 (EUPL 1.1)",
        "Operating System :: Unix",
    ],
    name="schumaaxdiffusion2D",
    version="0.0.2",
    author="Axel Schumacher",
    description="A super small solver for the diffusion equation",
    url="https://github.com/Simulation-Software-Engineering/Lecture-Material/tree/main/building-and-packaging/material",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    
    
)
