import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np




def derivative_template():
    data = {}

    data['blank'] = rcf.read_trans_data(78)
    data['trans'] = rcf.read_trans_data(79)


    # plots the ABS
    fig, ax1 = plt.subplots()
    pcg.plot_absorption(data, ax=ax1, smooth=True)


    # Plots the Derivatives 
    ax2 = ax1.twinx()
    right_color = 'green'
    pcg.plot_deriv_absorption(data, ax=ax2, smooth=True, color=right_color)
    pcg.plot_deriv_absorption(data, ax=ax2, smooth=True, color='red', order=2)




    # make the right axis ABS color
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)

    plt.show()

    
derivative_template()

'''Still a working progress'''
def fit_template():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(2)
    data['trans'] = rcf.read_trans_data(13)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][300] = rcf.read_trans_data(18) # voltage_file



    # plots the ABS
    fig, ax1 = plt.subplots()
    # pcg.plot_absorption(data, ax=ax1, smooth=True)
    # pcg.plot_EA_voltage(data, ax=ax1, voltage=550, smooth=True)
    pcg.plot_FK_fit(data, ax=ax1, voltage=300, smooth=True)

    plt.show()






