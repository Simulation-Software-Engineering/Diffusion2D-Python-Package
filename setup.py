from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="geldnens_diffusion2D",
    version="0.0.1",
    author="Nicolas Geldner",
    description="Simple practice package demonstrating 2D heat diffusion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Simulation-Software-Engineering/Diffusion2D-Python-Package",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["numpy", "matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
    ],
)
