from setuptools import setup
import setuptools

setup(
    name="strackardiffusion2D",
    version="0.0.2",
    author="Alexander Strack",
    description="diffusion computation in 2D",
    url="https://github.com/Simulation-Software-Engineering/Diffusion2D-Python-Package",
    packages=setuptools.find_packages(where='src'),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=["numpy", "matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent"
    ]
)
