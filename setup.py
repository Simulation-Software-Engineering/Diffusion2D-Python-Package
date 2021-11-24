from setuptools import setup
import setuptools

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name="hauschmxdiffusion2D",
    version="0.0.2",
    author="Max Hausch",
    description="Diffusion simulation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Simulation-Software-Engineering",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=["matplotlib", "numpy"],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Common Public License",
        "Operating System :: Unix",
    ],
)
