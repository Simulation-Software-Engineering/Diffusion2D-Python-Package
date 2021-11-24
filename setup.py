from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="anagnoesdiffusion2D",
    version="0.0.2",
    author="anagnoes",
    description="A small description",
    url="https://github.com/Simulation-Software-Engineering/Diffusion2D-Python-Package",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["pip",
     "build",
     "Twine",
     "NumPy" ,
     "Matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)