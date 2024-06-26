import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np


def CPL_template():
    data = rcf.read_PMT_data(78)

    # plots the EA
    fig, ax1 = plt.subplots()

    # Plots the Absorption 
    ax2 = ax1.twinx()
    right_color = 'green'

    # plot the data
    pcg.plot_CPL(data, ax1=ax1, ax2=ax2)


    # make the right axis ABS color
    ax2.set_ylabel('NAME ME', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)


    # plt.savefig(fig_name, format='png', dpi=300)

    plt.show()