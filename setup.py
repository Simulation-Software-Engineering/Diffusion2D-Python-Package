from setuptools import setup
import setuptools

setup(
    name="chalapaidiffusion2d",
    version="0.0.1",
    author="Andrei Chalapco",
    description="Small simulation software",
    url="https://github.com/Simulation-Software-Engineering/Diffusion2D-Python-Package",
    package_dir={"": "src"},
    packages=["chalapaidiffusion2d"],
    python_requires=">=3.6",
    install_requires=['numpy', 'matplotlib'],

    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ]
)
