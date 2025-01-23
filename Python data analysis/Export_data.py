import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np



def PESI_2F_17K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    export = 'C:/Data/Compiled Data/Kentcky Henry/Low temp' # Folder location to export the data

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1405, export_folder=export)
    data['trans'] = rcf.read_trans_data(1406, export_folder=export)


    data['voltages'][100] = rcf.read_trans_data(1407, export_folder=export) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(1408, export_folder=export) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1409, export_folder=export) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1410, export_folder=export) # voltage_file

    
    # plots the EA
    fig, ax1 = plt.subplots()
    # ax1.set_ylim(0,0.15)
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=True, phased=True)
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=200, smooth=True,color='red',energy=True)

    # Plots the Absorption
    ax2 = ax1.twinx()
    # ax2.set_ylim(0,2)
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=True,legend='Abs')


    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)

    plt.title('2-F PESI Electroabsorption Spectra')
    plt.show()
    
PESI_2F_17K()


