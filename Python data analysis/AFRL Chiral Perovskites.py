'''
AFRL Chiral Perovskites Analysis Script
This script is designed to analyze the chiral perovskites dataset from the AFRL. It includes functions to load the dataset, preprocess it, and visualize the results.
'''
# Imported Libraries
import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import public.export_colton_data as ecd
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame

def voltage_series_with_absorption(data, title, temp, smooth_abs=False, smooth_ea=False, energy=False, phased=False, export=False, remote=False, flip=False):
    """
    Function to plot the electroabsorption (EA) and absorption data for a series of voltages.
    Parameters:
        data (dict): Dictionary containing the data for blank, trans, and voltages.
        smooth (bool): Whether to smooth the voltage data.  Default is False.
        energy (bool): Whether to plot the energy scale. Default is False.      
        phased (bool): Whether to plot the phased voltage data. Default is False.
    """
    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=smooth_ea, energy=energy, phased=phased, flip=flip)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=smooth_abs, energy=energy)
    ax2.axhline

    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)

    plt.title(f'{title} EA and Absorption')

    if export:
        ecd.Export_EA_series_data(data, filename=f'AFRL\\{title} EA_series_data_{temp}K.csv', smooth_abs=smooth_abs, smooth_ea=smooth_ea, remote=remote, flip=flip, phased=phased)


def temp_series(data, title, smooth_abs=False, smooth_ea=False, smooth_cd=False, energy=False, phased=False, flip_ea=False, flip_cd=False, export=False, remote=False):
    # Create the first plot with the first y-axis
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    fig3, ax3 = plt.subplots()
    fig4, ax4 = plt.subplots()

    # plot the graphs
    pcg.plot_ABS_temp_series(data,ax=ax1, color_map_name='rainbow', smooth=smooth_abs,  energy=energy)
    pcg.plot_EA_temp_series(data, ax=ax2, color_map_name='rainbow', smooth=smooth_ea,   energy=energy, phased=phased, flip=flip_ea)
    pcg.plot_CD_temp_series(data, ax=ax3, color_map_name='rainbow', smooth=smooth_cd,   energy=energy, phased=phased, flip=flip_cd)
    # pcg.plot_ABS_CD_EA(data, ax=ax3,

    if export:
        ecd.Export_ABS_temp_data(data, filename=f'AFRL\\{title} ABS_temp_series_data.csv', smooth=smooth_abs, remote=remote)
        ecd.Export_EA_temp_data(data,   filename=f'AFRL\\{title} EA_temp_series_data.csv', smooth=smooth_ea, remote=remote, flip=flip_ea, phased=phased)
        ecd.Export_CD_temp_data(data,   filename=f'AFRL\\{title} CD_temp_series_data.csv', smooth=smooth_cd, remote=remote, flip=flip_cd, phased=phased)




"""AFRL samples """
def L_Ala_PbI_3_16K(remote=False):
    title = 'L-Ala PbI_3' # Change this to perovskite name
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['low temp'] = {}
    data['low temp']['voltages'] = {} # Low temp voltage Series
    data['temp series'] = {}
    data['temp series']['trans'] = {}
    data['temp series']['voltages'] = {}
    data['temp series']['pem'] = {}
    data['high temp'] = {}
    data['high temp']['voltages'] = {} # Low temp voltage Series
    
    # Which ones to plot
    plot_low_temp_voltage_series = True
    plot_trio_temp_series = False
    plot_high_temp_voltage_series = False

    # Low temp Voltage Series
    low_temp_voltages = [100, 150, 200, 250, 300, 350, 400]
    low_temp_volt_file_list  =  range(2084, 2093) #[2084,2086,2087,2088,2089,2090,2091,2092]
    low_temp_blank = 2094
    low_temp_trans = 2093

    # Temperature Series
    temperatures = [15,50,100,150,200,250,300]
    temp_series_blank = 2094
    temp_trans_file_list = range(1944,1951)
    temp_volt_file_list  = range(1951,1958)
    temp_pem_file_list   = range(1951,1958)

    # High temp Voltage Series
    high_temp_voltages = [100, 150, 200, 250, 300, 350, 400]
    high_temp_volt_file_list  = range(2084, 2092)
    high_temp_blank = 2094
    high_temp_trans = 2093


    ''' read data for low temp voltage series '''
    if plot_low_temp_voltage_series:
        # trans and blank will have strings as their voltage value, but each voltage will be an integer
        data['low temp']['blank'] = rcf.read_trans_data(low_temp_blank, remote=remote)
        data['low temp']['trans'] = rcf.read_trans_data(low_temp_trans, remote=remote)

        for i, voltage in enumerate(low_temp_voltages):
            data['low temp']['voltages'][voltage] = rcf.read_trans_data(low_temp_volt_file_list[i], remote=remote)

        # Plot EA and Absorption
        voltage_series_with_absorption(data['low temp'], title=title, temp=16, energy=False, phased=False, smooth_abs=False, smooth_ea=False, flip=False, remote=remote, export=False)

    ''' read data for the ABS, EA, CD temperature series '''
    if plot_trio_temp_series:
        # blank data
        data['temp series']['blank'] = rcf.read_trans_data(temp_series_blank, remote=remote)
        
        for i, temp in enumerate(temperatures):
            data['temp series']['trans'][temp] = rcf.read_trans_data(temp_trans_file_list[i], remote=remote)
            data['temp series']['voltages'][temp] = rcf.read_trans_data(temp_volt_file_list[i], remote=remote)
            data['temp series']['CD'][temp] = rcf.read_trans_data(temp_pem_file_list[i], remote=remote)
        
        # Plot ABS, EA, and CD temp series
        temp_series(data['temp series'], title, smooth_abs=False, smooth_ea=False, smooth_cd=False, energy=False, phased=False, flip_ea=False, flip_cd=False, remote=remote, export=False)

    ''' read data for high temp voltage series '''
    if plot_high_temp_voltage_series:
        # trans and blank will have strings as their voltage value, but each voltage will be an integer
        data['high temp']['blank'] = rcf.read_trans_data(high_temp_blank, remote=remote)
        data['high temp']['trans'] = rcf.read_trans_data(high_temp_trans, remote=remote)

        for i, voltage in enumerate(high_temp_voltages):
            data['high temp']['voltages'][voltage] = rcf.read_trans_data(high_temp_volt_file_list[i], remote=remote)

        # Plot EA and Absorption
        voltage_series_with_absorption(data['high temp'], title=title, temp=295, energy=False, phased=False, smooth_abs=False, smooth_ea=False, flip=False, remote=remote, export=False)

    


































def S_3F_MBA_2PBI4_16K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(2078)
    data['trans'] = rcf.read_trans_data(2077)

    # # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(2075) 
    data['voltages'][400] = rcf.read_trans_data(2076) 


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=True)
    ax2.axhline

    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)

def S_3Cl_MBA_2PBI4_16K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(2045)
    data['trans'] = rcf.read_trans_data(2046)

    # # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(2048) 
    data['voltages'][150] = rcf.read_trans_data(2049) 
    data['voltages'][200] = rcf.read_trans_data(2050) 
    data['voltages'][250] = rcf.read_trans_data(2051) 
    data['voltages'][300] = rcf.read_trans_data(2052) 
    data['voltages'][350] = rcf.read_trans_data(2053) 
    data['voltages'][400] = rcf.read_trans_data(2054) 


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=False, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=False)
    ax2.axhline

    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)

def S_3Cl_MBA_2PBI4_300K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(2044)
    data['trans'] = rcf.read_trans_data(2043)

    # # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(2042) 
    data['voltages'][150] = rcf.read_trans_data(2041) 
    data['voltages'][200] = rcf.read_trans_data(2040) 
    data['voltages'][250] = rcf.read_trans_data(2035) 
    data['voltages'][300] = rcf.read_trans_data(2039) 
    data['voltages'][350] = rcf.read_trans_data(2038) 
    data['voltages'][400] = rcf.read_trans_data(2037) 


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=True)
    ax2.axhline

    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)

def S_3I_MBA_2PBI4_18K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1960)
    data['trans'] = rcf.read_trans_data(1976)

    # # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(1969) 
    data['voltages'][150] = rcf.read_trans_data(1970) 
    data['voltages'][200] = rcf.read_trans_data(1971) 
    data['voltages'][250] = rcf.read_trans_data(1972) 
    data['voltages'][300] = rcf.read_trans_data(1973) 
    data['voltages'][350] = rcf.read_trans_data(1974) 
    data['voltages'][400] = rcf.read_trans_data(1975) 


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=True)
    ax2.axhline

    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)

def S_3I_MBA_2PBI4_290K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1960)
    data['trans'] = rcf.read_trans_data(1961)

    # # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(1962) 
    data['voltages'][150] = rcf.read_trans_data(1963) 
    data['voltages'][200] = rcf.read_trans_data(1964) 
    data['voltages'][250] = rcf.read_trans_data(1965) 
    data['voltages'][300] = rcf.read_trans_data(1966) 
    data['voltages'][350] = rcf.read_trans_data(1967) 
    data['voltages'][400] = rcf.read_trans_data(1968) 


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=True)
    ax2.axhline

    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)

def main():
    REMOTE = False  # Set to True if running on remote server, False for local testing
    # Uncomment the function you want to run
    L_Ala_PbI_3_16K(remote=REMOTE)
    # S_3F_MBA_2PBI4_16K()
    # S_3Cl_MBA_2PBI4_16K()
    # S_3Cl_MBA_2PBI4_300K()
    # S_3I_MBA_2PBI4_18K()
    # S_3I_MBA_2PBI4_290K()
    plt.show()


if __name__ == "__main__":
    main()

