import plot_colton_graphs as pcg
import read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np

def Absorption_template():
    fig, ax = plt.subplots()

    # date where the data is stored
    file_path = 'C:/Data/2024-02-22/'

    blank_file = file_path + 'Blank 2-MePESI 16K 300-700nm.xls'
    trans_file = file_path + 'Trans 2-MePESI 16K 300-700nm.xls'

    # Dictionary that holds all of the data with input voltages
    data = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(blank_file)
    data['trans'] = rcf.read_trans_data(trans_file)

    # plot data
    pcg.plot_absorption(data, ax=ax)
    
    plt.show()


def EA_voltage_template():
    # date where the data is stored
    file_path = 'C:/Data/2024-02-22/'

    blank_file = file_path + 'Blank 2-MePESI 16K 300-700nm.xls'
    trans_file = file_path + 'Trans 2-MePESI 16K 300-700nm.xls'
    voltage_file = file_path + 'EA 250V 2-MePESI 295K fast 2.xls'
    voltage = 250

    # fig_name = 'Y6 data.png' 

    # Dictionary that holds all of the data with input voltages
    data = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(blank_file)
    data['trans'] = rcf.read_trans_data(trans_file)
    data['voltage'] = rcf.read_trans_data(voltage_file) # For a single voltage

    # Create the first plot with the first y-axis
    fig, ax1 = plt.subplots()

    pcg.plot_EA_voltage(data, ax=ax1, voltage=voltage)
    # ax1.set_ylabel('Y1', color='blue')

    ax2 = ax1.twinx()
    ABS_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=ABS_color)


    # make the right ABS color

    ax2.set_ylabel('Absorption (OD)', color=ABS_color)

    # Set the color of the right y-axis line
    ax2.spines['right'].set_color(ABS_color)

    # Set the color of the right y-axis ticks to ABS color
    ax2.yaxis.set_tick_params(color=ABS_color)

    # Set the color of the tick labels on the right y-axis to ABS color
    for label in ax2.get_yticklabels():
        label.set_color(ABS_color)

    
    # plt.savefig(fig_name, format='png', dpi=300)
    plt.show()




def EA_series_template():
    # date where the data is stored
    file_path = 'C:/Data/2024-02-22/'

    blank_file = file_path + 'Blank 2-MePESI 16K 300-700nm.xls'
    trans_file = file_path + 'Trans 2-MePESI 16K 300-700nm.xls'
    voltage_series_file = file_path + 'EA 2-MePESI 16K 300-700nm 100-300V.xls'

    # Dictionary that holds all of the data with input voltages
    data = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(blank_file)
    data['trans'] = rcf.read_trans_data(trans_file)
    data['voltages'] = rcf.read_voltage_series_data(voltage_series_file) # This returns a dictionary with the values
    # ex: data['voltages'][100] = rcf.read_trans_data(Single_voltage_filename) # For a single voltage

    # Create the first plot with the first y-axis
    fig, ax1 = plt.subplots()

    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma')

    ax2 = ax1.twinx()
    ABS_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=ABS_color)


    # make the right axis ABS color

    ax2.set_ylabel('Absorption (OD)', color=ABS_color)

    # Set the color of the right y-axis line
    ax2.spines['right'].set_color(ABS_color)

    # Set the color of the right y-axis ticks to ABS color
    ax2.yaxis.set_tick_params(color=ABS_color)

    # Set the color of the tick labels on the right y-axis to ABS color
    for label in ax2.get_yticklabels():
        label.set_color(ABS_color)

    
    # plt.savefig(fig_name, format='png', dpi=300)
    plt.show()


# Absorption_template()
EA_series_template()