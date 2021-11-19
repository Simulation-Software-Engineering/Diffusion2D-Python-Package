# Diffusion2D-Python-Package

## Project description

This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. 
This code solves the diffusion equation using the Finite Difference Method. 
The thermal diffusivity and initial conditions of the system can be changed by the user. 
The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package

### Using pip3 to install from PyPI

Use either

`pip3 install haagjndiffusion2D`

or 

`python3 -m pip install haagjndiffusion2D`

to install.

### Required dependencies

- Python >= 3.6
- [NumPy](https://numpy.org)
- [Matplotlib](https://matplotlib.org)

## Running this package

Minimal working example:

```
from haagjndiffusion2D import diffusion2d
diffusion2d.solve()
```

## Citing

This code is based on [Chapter 7 of the book "Learning Scientific Programming with Python](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).