import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import public.colton_math_functions as cmf
import matplotlib.pyplot as plt
import numpy as np


def CD_template_new():
    data = {}

    trans_files = [] # insert row number in excel
    blank_files =[] # insert row number in excel

    name_color = ['red', 'blue', 'green','black','orange'] # This doesn't have to change unless you have more than 5 plots
    
    fig, ax = plt.subplots()
    for i in range(len(trans_files)):
        data['trans'] = rcf.read_trans_data(trans_files)
        data['blank'] = rcf.read_trans_data(blank_files)

        # plot data
        pcg.plot_absorption(data, ax=ax, smooth=False, color=name_color[i])
        ax.legend(trans_files)


def CD_template(): # Needs to be updated
    data = rcf.read_lockin_fluke_data(662)

    fig, ax = plt.subplots()
    pcg.plot_CD(data, ax=ax, energy=False, Phased=True)

    # legend name
    legend = 'Absorption'

    plt.show()

# CD_template()





def CD_carter():
    data = {}

    fig, ax = plt.subplots()

    data['DC'] = rcf.read_trans_data(745)
    data['AC'] = rcf.read_trans_data(746)
    pcg.plot_CD_Carter(data, ax=ax, energy=False, Phased=False)


    data['AC'] = rcf.read_trans_data(746)-6e-12
    pcg.plot_CD_Carter(data, ax=ax, energy=False, Phased=False)


    data['AC'] = rcf.read_trans_data(746)-7e-12
    pcg.plot_CD_Carter(data, ax=ax, energy=False, Phased=False)

    data['AC'] = rcf.read_trans_data(746)-8e-12
    pcg.plot_CD_Carter(data, ax=ax, energy=False, Phased=False)

    plt.show()

CD_carter()