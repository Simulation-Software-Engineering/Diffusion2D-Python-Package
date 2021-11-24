# Diffusion2D-Python-Package

## Instructions for students

Please follow the instructions in [exercise_python_packaging_text.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/exercise_python_packaging_text.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description

This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. 

## Installing the package

One can install the pakage by running 'pip install -i https://test.pypi.org/simple/ pereirrndiffusion2d'

### Using pip3 to install from PyPI

One can just use the command cited above to install from PyPI.

### Required dependencies

The following tools are needed: pip, NumPy, Matplotlib, build and Twine

## Running this package

One can import the function 'diffusion2d.solver()' from the package. In order to use such fuction, the user needs to provide the values of variables 'dx', 'dy', and 'D', which correspond to number of nodes in x and y direction and diffusivity of the material. Default values are already set in the code. 

## Citing
