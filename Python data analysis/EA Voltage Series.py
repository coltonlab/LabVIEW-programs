import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np

def check_phase(data):
    voltages = np.array(list(data['voltages'].keys()))
    for v in voltages:
        fig, ax = plt.subplots()
        pcg.plot_data(data['voltages'][v],ax=ax, smooth=False)
        ax.set_title(v)





def EA_template():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(595)
    data['trans'] = rcf.read_trans_data(596)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    # data['voltages'][0] = rcf.read_trans_data(545) # voltage_file
    data['voltages'][100] = rcf.read_trans_data(597) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(598) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(599) # voltage_file
    # data['voltages'][400] = rcf.read_trans_data(600) # voltage_file
    # data['voltages'][500] = rcf.read_trans_data(601) # voltage_file
    # data['voltages'][600] = rcf.read_trans_data(602) # voltage_file

    # data['voltages'][601] = rcf.read_trans_data(594) # voltage_file



    # check_phase(data)


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma', smooth=True, energy=True)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=100, smooth=False)

    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=True)


    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)


    plt.show()

EA_template()