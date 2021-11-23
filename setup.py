from setuptools import setup
import setuptools

setup(
    name="altawemddiffusion2D",
    version="0.0.6",
    author="Mohamad Altaweel",
    description="A small description",
    classifiers=[
        "Programming Language :: Python :: 3.6",
    ],
    url="https://github.com/Simulation-Software-Engineering/Diffusion2D-Python-Package",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["numpy","matplotlib"]
)