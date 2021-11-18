import matplotlib.pyplot as plt

def create_plot(fig, fig_counter, u, T_cold, T_hot, n, dt):
    """
    Creates one plot for a particular time stamp

    Args:
        fig ([type]): [description]
        fig_counter ([type]): [description]
        u ([type]): [description]
        T_cold ([type]): [description]
        T_hot ([type]): [description]
        n ([type]): [description]
        dt ([type]): [description]

    Returns:
        [type]: [description]
    """
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)  # image for color bar axes
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))
    return fig, im

def output_plots(fig, im):
    """
    Outputs all the four plots as one figure

    Args:
        fig ([type]): [description]
        im ([type]): [description]
    """
    # Plot output figures
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()