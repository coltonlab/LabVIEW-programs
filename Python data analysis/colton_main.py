import plot_colton_graphs as pcg
import read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np

def data_template():
    data = {}
    
    fig, ax = plt.subplots()
    data['trans'] = rcf.read_trans_data(381)

    pcg.plot_data(data['trans'],ax=ax)

    


def absorption_template():
    data = {}

    data['blank'] = rcf.read_trans_data()
    data['trans'] = rcf.read_trans_data()

    fig, ax = plt.subplots()

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False)

    # ax.legend(trans_files)
    

def EA_template():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(78)
    data['trans'] = rcf.read_trans_data(79)


    data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    # data['voltages'][200] = rcf.read_trans_data(235) # voltage_file
    # data['voltages'][250] = rcf.read_trans_data(236) # voltage_file
    # data['voltages'][300] = rcf.read_trans_data(237) # voltage_file


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma', smooth=True)


    # Plots the Absorption 
    ax2 = ax1.twinx()
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True)


    # make the right axis ABS color
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)


    # plt.savefig(fig_name, format='png', dpi=300)
    

def EA_temperature_series_template(): # Needs to be updated
    # date where the data is stored
    file_path = 'C:/Data/2024-02-23/'

    data = {}
    data['trans'] = {}
    data['voltages'] = {}

    blank_file = file_path + 'Blank 2-MePESI 300-700nm 295K.xls'
    data['blank'] = rcf.read_trans_data(blank_file) 
    
    # go through the temperatures
    temperatures = [18,50,100,150,200,250,295]
    
    for temp in temperatures:
        trans_file = file_path + 'Trans 2-MePESI 300-700nm {}K.xls'.format(temp)
        data['trans'][temp] = rcf.read_trans_data(trans_file)

        voltage_file = file_path + '300V EA 2-MePESI 300-700nm {}K.xls'.format(temp)
        data['voltages'][temp] = rcf.read_trans_data(voltage_file)


    # Create the first plot with the first y-axis
    fig1, ax1 = plt.subplots()
    pcg.plot_EA_temp_series(data, ax=ax1, color_map_name='rainbow')


    fig2, ax2 = plt.subplots()
    pcg.plot_ABS_temp_series(data, ax=ax2, color_map_name='rainbow')


    # plt.savefig(fig_name, format='png', dpi=300)
    

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
    data = rcf.read_CD_data()
    data2 = rcf.read_CD_data()
    

    fig, ax = plt.subplots()
    # plot data
    pcg.plot_CD(data, ax=ax)
    

    # Temporary stuff
    fig, ax = plt.subplots()
    
    import colton_math_functions as cmf

    # Calculate the absorption signal
    ABS_data = cmf.absorption(data['Keithley (V)'], data2['Keithley (V)'])    
     
    # legend name 
    legend = 'Absorption'    

    ax.plot(data['Digikrom Spectr.:0 (?)'],ABS_data, label=legend)
    # ax.legend()
    ax.set_xlabel('Wavelength')
    ax.set_ylabel('Absorption (OD)')


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





# derivative_template()
# data_template()
# absorption_template()
# EA_template()
# EA_temperature_series_template()
#CD_template()
fit_template()

plt.show()