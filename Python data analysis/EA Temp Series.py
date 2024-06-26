import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np


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

    plt.show()





