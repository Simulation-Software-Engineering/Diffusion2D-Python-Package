from setuptools import setup
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="hornektediffusion2D",
    version="0.0.4",
    author="Timothée Hornek",
    description="simple package for diffusion computation",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Simulation-Software-Engineering/Diffusion2D-Python-Package",
    packages=setuptools.find_packages(where='src'),
    package_dir={"": "src"},
    #packages=setuptools.find_packages(where="./src/hornektediffusion2D/"),
    #packages=setuptools.find_packages(include=['src/hornektediffusion2D']),
    python_requires=">=3.6",
    install_requires=["numpy", "matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent"
        #"License :: OSI Approved :: CC"
    ]
)
