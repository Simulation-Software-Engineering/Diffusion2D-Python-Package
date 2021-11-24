import matplotlib.pyplot as plt


def create_plot(timestamp, u0, u, D, dt, dx2, dy2, fig, fig_counter):
    n = 0
    for n in range(timestamp+1):
        u0, u = do_timestep(u0, u, D, dt, dx2, dy2)

    ax = fig.add_subplot(220 + fig_counter)
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))
    return (ax, u.copy())


def output_plots(timesteps, u0, u, D, dt, dx2, dy2, T_cold, T_hot, fig):
    im = None
    fig_counter = 0

    for ts in timesteps:
        fig_counter += 1
        ax, u = create_plot(ts, u0, u, D, dt, dx2, dy2, fig, fig_counter)

        # image for color bar axes
        im = ax.imshow(
            u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)
    return im


def do_timestep(u_nm1, u, D, dt, dx2, dy2):
    # Propagate with forward-difference in time, central-difference in space
    u[1:-1, 1:-1] = u_nm1[1:-1, 1:-1] + D * dt * (
            (u_nm1[2:, 1:-1] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[:-2, 1:-1]) / dx2
            + (u_nm1[1:-1, 2:] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[1:-1, :-2])
            / dy2)

    u_nm1 = u.copy()
    return u_nm1, u
