# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:05:51 2021

@author: user
"""

import matplotlib.pyplot as plt

def create_plot(n,u,fig_counter,fig,dt,T_cold,T_hot):

    # Create figure
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)  # image for color bar axes
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))
    
    return im,ax


def output_plots(fig,im):
    
    # Plot output figures
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()

    
    return