# Diffusion2D-Python-Package

## Project description

This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package

### Using pip3 to install from PyPI

The package is on TestPyPI under the name geldnens_diffusion2D.

### Required dependencies

The package requires only NumPy and Matplotlib.

## Running this package

To run the solver:

    from geldnens_diffusion2D import diffusion2d

    diffusion2d.solve()

## Citing

Package created by Nicolas Geldner, website [here](https://github.com/Simulation-Software-Engineering/Diffusion2D-Python-Package)


