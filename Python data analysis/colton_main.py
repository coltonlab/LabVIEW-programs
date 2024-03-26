import plot_colton_graphs as pcg
import read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np



def Absorption_template():
    fig, ax = plt.subplots()

    # date where the data is stored
    file_path = 'C:/Data/2024-03-21/'

    blank_file = file_path + 'Blank PM6Y6 1_2 LN LP850 850-1400nm.xls'
    trans_file = file_path + 'Trans PM6Y6 1_2 LN LP850 850-1400nm spot2.xls'

    #blank_file2 = file_path + 'Blank 2 PM6 LN LP850 850-1400nm 1nm step 300ms.xls'
    #trans_file2 = file_path + 'Trans PM6 LN LP850 850-1400nm 1nm step 300ms.xls'

    # Dictionary that holds all of the data with input voltages
    data = {}
    #data2 = {}
    names = ['C:/Data/2024-03-21/Trans PM6Y6 1_2 LN LP850 850-1400nm spot1.xls',
             'C:/Data/2024-03-21/Trans PM6Y6 1_1-2 LN LP850 850-1400nm spot 1.xls',
            'C:/Data/2024-03-20/Trans PM6-Y6 2-1 LN LP850 850-1400nm Spot 4.xls',
            'C:/Data/2024-03-19/Trans Y6 LN LP850 850-1400nm 1nm step 300ms spot 2.xls',
            'C:/Data/2024-03-19/Trans PM6 LN LP850 850-1400nm 1nm step 300ms spot 4.xls']
    
    blank_names =['C:/Data/2024-03-21/Blank PM6Y6 1_2 LN LP850 850-1400nm.xls',
                  'C:/Data/2024-03-21/Blank PM6Y6 1_1-2 LN LP850 850-1400nm.xls',
                  'C:/Data/2024-03-20/Blank PM6-Y6 2-1 LN LP850 850-1400nm.xls',
                  'C:/Data/2024-03-19/Blank 2 Y6 LN LP850 850-1400nm 1nm step 300ms spot 1.xls',
                  'C:/Data/2024-03-19/Blank 2 PM6 LN LP850 850-1400nm 1nm step 300ms.xls']

    name_color = ['red', 'blue', 'green','black','orange']
    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    #data['blank'] = rcf.read_trans_data(blank_file)
    
    
    for i in range(len(names)):
        trans_file = names[i]
        blank_file = blank_names[i]
            
        data['trans'] = rcf.read_trans_data(trans_file)
        data['blank'] = rcf.read_trans_data(blank_file)

        #data2['blank'] = rcf.read_trans_data(blank_file2)
        #data2['trans'] = rcf.read_trans_data(trans_file2)

        # plot data
        pcg.plot_absorption(data, ax=ax, smooth=False, color=name_color[i])
        ax.legend(names)
        # pcg.plot_absorption(data, ax=ax, smooth=True, color='red')

        #pcg.plot_absorption(data2,ax=ax,smooth=False,color='black')
    
    plt.show()


def EA_voltage_template():
    # date where the data is stored
    file_path = 'C:/Data/2024-03-14/'

    blank_file = file_path + 'Blank SL LN LP550 620-1400nm 300ms 1nm.xls'
    trans_file = file_path + 'Trans PM6 SL LN LP550 620-1400nm 300ms 1nm.xls'

    voltage_file = file_path + 'EA 350V PM6 SL LN LP550 620-1400nm 300ms 1nm.xls'
    voltage = 350

    # fig_name = 'Y6 data.png' 

    # Dictionary that holds all of the data with input voltages
    data = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(blank_file)
    data['trans'] = rcf.read_trans_data(trans_file)
    data['voltage'] = rcf.read_trans_data(voltage_file) # For a single voltage

    # Create the first plot with the first y-axis
    fig, ax1 = plt.subplots()

    pcg.plot_EA_voltage(data, ax=ax1, smooth=False, voltage=voltage)
    pcg.plot_EA_voltage(data, ax=ax1, smooth=True, voltage=voltage, color='red')
    # ax1.set_ylabel('Y1', color='blue')

    ax2 = ax1.twinx()
    ABS_color = 'green'
    pcg.plot_absorption(data, ax=ax2, smooth=False, color=ABS_color)
    pcg.plot_absorption(data, ax=ax2, smooth=True, color='black')

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


def EA_voltage_series_template():
    # date where the data is stored
    file_path = 'C:/Data/2024-03-21/'

    # blank_file = file_path + 'Blank PM6-Y6 2-1 LN LP850 850-1400nm.xls'
    # trans_file = file_path + 'Trans PM6-Y6 2-1 LN LP850 850-1400nm Spot 1.5.xls'
    # voltage_series_file = file_path + 'Voltage Series EA PM6-Y6 2-1 LN LP850 850-1400nm Spot 1.5.xls'


    blank_file = file_path + 'Blank PM6Y6 1_1-2 LN LP850 850-1400nm.xls'
    trans_file = file_path + 'Trans PM6Y6 1_1-2 LN LP850 850-1400nm spot 3.xls'
    voltage_series_file1 = file_path + 'EA 150V PM6Y6 1_1-2 LN LP850 850-1400nm spot 3.xls'
    voltage_series_file2 = file_path + 'EA 350V PM6Y6 1_1-2 LN LP850 850-1400nm spot 3.xls'
    voltage_series_file3 = file_path + 'EA 550V PM6Y6 1_1-2 LN LP850 850-1400nm spot 3.xls'

    # Dictionary that holds all of the data with input voltages
    data = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(blank_file)
    data['trans'] = rcf.read_trans_data(trans_file)
    data['voltages'] = {}
    # data['voltages'] = rcf.read_voltage_series_data(voltage_series_file) # This returns a dictionary with the values
    
    data['voltages'][150] = rcf.read_trans_data(voltage_series_file1)
    data['voltages'][350] = rcf.read_trans_data(voltage_series_file2)
    data['voltages'][550] = rcf.read_trans_data(voltage_series_file3)
    # ex: data['voltages'][100] = rcf.read_trans_data(Single_voltage_filename) # For a single voltage

    # Create the first plot with the first y-axis
    fig, ax1 = plt.subplots()

    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma', smooth=True)

    ax2 = ax1.twinx()
    ABS_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=ABS_color, smooth=False)


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


def EA_temperature_series_template():
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


def CD_template():
    fig, ax = plt.subplots()

    # date where the data is stored
    file_path = 'C:/Data/2024-03-05/CD test B12 400ohm input amplifier.xls'
    file_path2 = 'C:/Data/2024-03-05/CD test blank 400ohm amplifier.xls'

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data = rcf.read_CD_data(file_path)
    data2 = rcf.read_CD_data(file_path2)
    
    # plot data
    pcg.plot_CD(data, ax=ax)

    plt.show()

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

    plt.show()




# EA_voltage_template()
# EA_voltage_series_template()
Absorption_template()
# EA_temperature_series_template()
#CD_template()