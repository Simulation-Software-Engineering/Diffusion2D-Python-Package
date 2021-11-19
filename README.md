# Diffusion2D-Python-Package
We created a super small python solver to solve the diffuion equation in 2D.

## Instructions for students

Please follow the instructions in [exercise_python_packaging_text.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/building-and-packaging/material/exercise_python_packaging_text.md).
The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description

**Information about solver.py**: This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package

Use pip3 to install the package locally. See next section.

### Using pip3 to install from PyPI

To get the latest version of our package, type:
`pip install --user -index-url https://test.pypi.org/simple/ schumaaxdiffusion2D`

### Required dependencies

- Python
- pip
- NumPy
- Matplotlib


## Running this package

write a script `use_schumaax_solver.py`, which contains the following lines:

```
 from schumaaxDiffusion2D import diffusion2D
 
 diffusion2d.solve()
```

## Citing
If you use our package, please cite us as: Diffusion2D, SSE-lecture winter 21/22, University of Stuttgart, project.
