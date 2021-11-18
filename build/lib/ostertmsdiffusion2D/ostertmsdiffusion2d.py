"""
Solving the two-dimensional diffusion equation

Example acquired from https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/
"""

import numpy as np
import matplotlib.pyplot as plt

from .output import create_plot, output_plots

######################
# Initial Conditions #
######################

# plate size, mm
w = h = 10.

# Initial cold temperature of square domain
T_cold = 300

# Initial hot temperature of circular disc at the center
T_hot = 700

class ostertmsdiffusion2D:
    ##################
    # Solve Function #
    ##################
    def solve(dx = 0.1, dy = 0.1, D = 4):
        """
        This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. 
        This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. 
        The code produces four plots at various timepoints of the simulation. 
        The diffusion process can be clearly observed in these plots.

        Args:
            dx (float, optional): intervals in x- directions, mm. Defaults to 0.1.
            dy (float, optional): intervals in y- directions, mm. Defaults to 0.1.
            D (int, optional): Thermal diffusivity of steel, mm^2/s. Defaults to 4.
        """

        # Number of discrete mesh points in X and Y directions
        nx, ny = int(w / dx), int(h / dy)

        # Computing a stable time step
        dx2, dy2 = dx * dx, dy * dy
        dt = dx2 * dy2 / (2 * D * (dx2 + dy2))

        print("dt = {}".format(dt))

        u0 = T_cold * np.ones((nx, ny))
        u = u0.copy()

        # Initial conditions - circle of radius r centred at (cx,cy) (mm)
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(nx):
            for j in range(ny):
                p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
                if p2 < r2:
                    u0[i, j] = T_hot


        def do_timestep(u_nm1, u, D, dt, dx2, dy2):
            # Propagate with forward-difference in time, central-difference in space
            u[1:-1, 1:-1] = u_nm1[1:-1, 1:-1] + D * dt * (
                    (u_nm1[2:, 1:-1] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[:-2, 1:-1]) / dx2
                    + (u_nm1[1:-1, 2:] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[1:-1, :-2]) / dy2)

            u_nm1 = u.copy()
            return u_nm1, u


        # Number of timesteps
        nsteps = 101
        # Output 4 figures at these timesteps
        n_output = [0, 10, 50, 100]
        fig_counter = 0
        fig = plt.figure()

        # Time loop
        for n in range(nsteps):
            u0, u = do_timestep(u0, u, D, dt, dx2, dy2)

            # Create figure
            if n in n_output:
                fig_counter += 1
                fig, im = create_plot(fig, fig_counter, u, T_cold, T_hot, n, dt)

        output_plots(fig, im)
