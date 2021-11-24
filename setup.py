from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="chalapaidiffusion2d",
    version="0.0.3",
    author="Andrei Chalapco",
    description="Small simulation software",
    url="https://github.com/Simulation-Software-Engineering/Diffusion2D-Python-Package",
    package_dir={"": "src"},
    packages=["chalapaidiffusion2d"],
    python_requires=">=3.6",
    install_requires=['numpy', 'matplotlib'],
    long_description=long_description,
    long_description_content_type="text/markdown",

    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ]
)
