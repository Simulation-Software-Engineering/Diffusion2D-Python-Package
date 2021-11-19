from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="haagjndiffusion2D",
    version="0.0.4",
    author="Jonathan Haag",
    description="A 2D diffusion equation solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonahaag/Diffusion2D-Python-Package",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["NumPy", "Matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)

# "License :: OSI Approved :: CC-BY-4.0",