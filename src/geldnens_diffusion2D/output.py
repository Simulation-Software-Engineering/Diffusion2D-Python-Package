"""
Module for the diffusion output/graph drawing functions
"""

import matplotlib.pyplot as plt

def create_plot(u, T_cold, T_hot, time_secs, fig, fig_counter):
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)  # image for color bar axes
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(time_secs * 1000))

    return im

def output_plots(fig, im):
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
