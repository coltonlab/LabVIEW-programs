import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np
class Old_calculations(): # Just tab the function to archive it
    
    def check_phase(data):
        voltages = np.array(list(data['voltages'].keys()))
        for v in voltages:
            fig, ax = plt.subplots()
            pcg.plot_data(data['voltages'][v],ax=ax, smooth=False)
            ax.set_title(v)

    """

    All Absorption -  legend
    All reflection - legend
    EA of each with absorption - add titles, all the same scale
    ER of each with absorption - add titles, all the same scale
    EA of all 500V
    ER of all 500V 

    """

    # fig, ax1 = plt.subplots()
    # plt.title("500V ER")

    def EA_template():
        # Dictionary that holds all of the data with input voltages
        data = {}
        data['voltages'] = {}

        # trans and blank will have strings as their voltage value, but each voltage will be an integer
        data['blank'] = rcf.read_trans_data(1021)
        data['trans'] = rcf.read_trans_data(1022)


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
        pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True)
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
    # EA_template()

"""AFRL samples """
def L_Ala_PbI_3_16K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(2094)
    data['trans'] = rcf.read_trans_data(2093)

    # # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(2084) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(2086) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(2087) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(2088) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(2089) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(2090) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(2091) # voltage_file


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
L_Ala_PbI_3_16K()
def S_3F_MBA_2PBI4_16K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(2078)
    data['trans'] = rcf.read_trans_data(2077)

    # # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(2075) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(2076) # voltage_file


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
# S_3F_MBA_2PBI4_16K()
def S_3Cl_MBA_2PBI4_16K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(2045)
    data['trans'] = rcf.read_trans_data(2046)

    # # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(2048) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(2049) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(2050) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(2051) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(2052) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(2053) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(2054) # voltage_file


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
#S_3Cl_MBA_2PBI4_16K()

def S_3Cl_MBA_2PBI4_300K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(2044)
    data['trans'] = rcf.read_trans_data(2043)

    # # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(2042) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(2041) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(2040) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(2035) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(2039) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(2038) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(2037) # voltage_file


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
# S_3Cl_MBA_2PBI4_300K()

def S_3I_MBA_2PBI4_18K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1960)
    data['trans'] = rcf.read_trans_data(1976)

    # # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(1969) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(1970) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1971) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1972) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1973) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1974) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1975) # voltage_file


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
# S_3I_MBA_2PBI4_18K()

def S_3I_MBA_2PBI4_290K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1960)
    data['trans'] = rcf.read_trans_data(1961)

    # # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(1962) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(1963) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1964) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1965) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1966) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1967) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1968) # voltage_file


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
# S_3I_MBA_2PBI4_290K()

"""Kentucky Plots, Kevin (CHDA, CHDMA, 4-AMP, 4-AMPY)"""

"""4-AMP_SnI4 6-11-25"""
def AMP4_SnI4_15K_Thin_3s():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1934)
    data['trans'] = rcf.read_trans_data(1935)

    # # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][150] = rcf.read_trans_data(1937) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1938) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1939) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1940) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1941) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1942) # voltage_file


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=False)
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
# AMP4_SnI4_15K_Thin_3s()


def AMP4_SnI4_15K_Thin():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1923)
    data['trans'] = rcf.read_trans_data(1924)

    # # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    # data['voltages'][100] = rcf.read_trans_data(1833) # voltage_file
    # data['voltages'][150] = -rcf.read_trans_data(1834) # voltage_file
    # data['voltages'][150]['Digikrom Spectr.:0 (?)'] *= -1
    data['voltages'][200] = rcf.read_trans_data(1925) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1926) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1927) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1928) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1929) # voltage_file


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=False, phased=False)
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
# AMP4_SnI4_15K_Thin()
"""NPB Samples"""
def S_1_1_NPB_S2_16K():
        # Dictionary that holds all of the data with input voltages
        data = {}
        data['voltages'] = {}

        # trans and blank will have strings as their voltage value, but each voltage will be an integer
        data['blank'] = rcf.read_trans_data_old(1750)
        data['trans'] = rcf.read_trans_data_old(1751)


        # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
        
        # data['voltages'][100] = rcf.read_trans_data_old(1678) # voltage_file
        # data['voltages'][150] = rcf.read_trans_data_old(1679) # voltage_file
        # data['voltages'][200] = rcf.read_trans_data_old(1680) # voltage_file
        # data['voltages'][250] = rcf.read_trans_data_old(1681) # voltage_file        
        # data['voltages'][300] = rcf.read_trans_data_old(1682) # voltage_file
        # data['voltages'][350] = rcf.read_trans_data_old(1683) # voltage_file

        # Ion migration after this point?
        # data['voltages'][400] = rcf.read_trans_data_old(1684) # voltage_file
        # data['voltages'][500] = rcf.read_trans_data_old(1687) # voltage_file
        # data['voltages'][201] = rcf.read_trans_data_old(1686) # voltage_file

        # check_phase(data)


        # plots the EA
        fig, ax1 = plt.subplots()
        # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=False, colorbar=True, phased=False)
        # ax1.legend()
        # ax1.set_ylabel('Electroreflection (mOD)')
        ax1.set_ylabel('Electroabsorption (mOD)')

        # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=False)

        # Plots the Absorption
        ax2 = ax1.twinx()
        right_color = 'green'
        pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=False)


        # make the right axis ABS color
        # ax2.set_ylabel('Reflection (OD)', color=right_color)
        ax2.set_ylabel('Absorption (OD)', color=right_color)
        ax2.spines['right'].set_color(right_color)
        ax2.yaxis.set_tick_params(color=right_color)
        for label in ax2.get_yticklabels():
            label.set_color(right_color)


        plt.show()
# S_1_1_NPB_S2_16K()

def R_NEAPbI295K():
        # Dictionary that holds all of the data with input voltages
        data = {}
        data['voltages'] = {}

        # trans and blank will have strings as their voltage value, but each voltage will be an integer
        data['blank'] = rcf.read_trans_data_old(1616)
        data['trans'] = rcf.read_trans_data_old(1617)


        # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
        # data['voltages'][0] = rcf.read_trans_data(545) # voltage_file
        # data['voltages'][100] = rcf.read_trans_data(597) # voltage_file
        # data['voltages'][200] = rcf.read_trans_data(598) # voltage_file
        data['voltages'][150] = rcf.read_trans_data_old(1619) # voltage_file
        data['voltages'][300] = rcf.read_trans_data_old(1614) # voltage_file
        data['voltages'][301] = rcf.read_trans_data_old(1618) # voltage_file
        data['voltages'][400] = rcf.read_trans_data_old(1620) # voltage_file

        # check_phase(data)


        # plots the EA
        fig, ax1 = plt.subplots()
        pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=False, colorbar=True)
        # ax1.legend()
        # ax1.set_ylabel('Electroreflection (mOD)')
        ax1.set_ylabel('Electroabsorption (mOD)')

        # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=False)

        # Plots the Absorption
        ax2 = ax1.twinx()
        right_color = 'green'
        pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=False)


        # make the right axis ABS color
        # ax2.set_ylabel('Reflection (OD)', color=right_color)
        ax2.set_ylabel('Absorption (OD)', color=right_color)
        ax2.spines['right'].set_color(right_color)
        ax2.yaxis.set_tick_params(color=right_color)
        for label in ax2.get_yticklabels():
            label.set_color(right_color)


        plt.show()
# R_NEAPbI295K()

def R_NEAPbI15K():
        # Dictionary that holds all of the data with input voltages
        data = {}
        data['voltages'] = {}

        # trans and blank will have strings as their voltage value, but each voltage will be an integer
        data['blank'] = rcf.read_trans_data_old(1634)
        data['trans'] = rcf.read_trans_data_old(1633)
        
        # voltage scans
        data['voltages'][150] = rcf.read_trans_data_old(1631) # voltage_file
        data['voltages'][200] = rcf.read_trans_data_old(1630) # voltage_file
        data['voltages'][250] = rcf.read_trans_data_old(1629) # voltage_file
        data['voltages'][300] = rcf.read_trans_data_old(1628) # voltage_file
        data['voltages'][350] = rcf.read_trans_data_old(1627) # voltage_file
        data['voltages'][400] = rcf.read_trans_data_old(1626) # voltage_file
        data['voltages'][450] = rcf.read_trans_data_old(1632) # voltage_file

        # check_phase(data)


        # plots the EA
        fig, ax1 = plt.subplots()
        pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=False, colorbar=True)
        # ax1.legend()
        # ax1.set_ylabel('Electroreflection (mOD)')
        ax1.set_ylabel('Electroabsorption (mOD)')

        # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=False)

        # Plots the Absorption
        ax2 = ax1.twinx()
        right_color = 'green'
        pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=False)


        # make the right axis ABS color
        # ax2.set_ylabel('Reflection (OD)', color=right_color)
        ax2.set_ylabel('Absorption (OD)', color=right_color)
        ax2.spines['right'].set_color(right_color)
        ax2.yaxis.set_tick_params(color=right_color)
        for label in ax2.get_yticklabels():
            label.set_color(right_color)


        plt.show()
# R_NEAPbI15K()

def R_NEAPbI15K2():
        # Dictionary that holds all of the data with input voltages
        data = {}
        data['voltages'] = {}

        # trans and blank will have strings as their voltage value, but each voltage will be an integer
        data['blank'] = rcf.read_trans_data_old(1641)
        data['trans'] = rcf.read_trans_data_old(1642)
        
        # voltage scans
        data['voltages'] = rcf.read_voltage_series_data(1648) # voltage_series_file
        # data['voltages'][200] = rcf.read_trans_data_old(1646) # voltage_file
        # data['voltages'][250] = rcf.read_trans_data_old(1645) # voltage_file
        # data['voltages'][300] = rcf.read_trans_data_old(1644) # voltage_file
        # data['voltages'][350] = rcf.read_trans_data_old(1643) # voltage_file
        # data['voltages'][400] = rcf.read_trans_data_old(1647) # voltage_file
    
        # data['voltages'][350] = rcf.read_trans_data_old(1643) # voltage_file
        # check_phase(data)


        # plots the EA
        fig, ax1 = plt.subplots()
        pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=False, colorbar=True, flip=True)
        # ax1.legend()
        # ax1.set_ylabel('Electroreflection (mOD)')
        ax1.set_ylabel('Electroabsorption (mOD)')

        # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=400, smooth=True,energy=False)

        # Plots the Absorption
        ax2 = ax1.twinx()
        right_color = 'green'
        pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=False)


        # make the right axis ABS color
        # ax2.set_ylabel('Reflection (OD)', color=right_color)
        ax2.set_ylabel('Absorption (OD)', color=right_color)
        ax2.spines['right'].set_color(right_color)
        ax2.yaxis.set_tick_params(color=right_color)
        for label in ax2.get_yticklabels():
            label.set_color(right_color)


        plt.show()
# R_NEAPbI15K2()

def S_1_1_NPB_16K():
        # Dictionary that holds all of the data with input voltages
        data = {}
        data['voltages'] = {}

        # trans and blank will have strings as their voltage value, but each voltage will be an integer
        data['blank'] = rcf.read_trans_data_old(1672)
        data['trans'] = rcf.read_trans_data_old(1673)


        # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
        
        data['voltages'][100] = rcf.read_trans_data_old(1678) # voltage_file
        data['voltages'][150] = rcf.read_trans_data_old(1679) # voltage_file
        data['voltages'][200] = rcf.read_trans_data_old(1680) # voltage_file
        data['voltages'][250] = rcf.read_trans_data_old(1681) # voltage_file        
        data['voltages'][300] = rcf.read_trans_data_old(1682) # voltage_file
        data['voltages'][350] = rcf.read_trans_data_old(1683) # voltage_file

        # Ion migration after this point?
        # data['voltages'][400] = rcf.read_trans_data_old(1684) # voltage_file
        # data['voltages'][500] = rcf.read_trans_data_old(1687) # voltage_file
        # data['voltages'][201] = rcf.read_trans_data_old(1686) # voltage_file

        # check_phase(data)


        # plots the EA
        fig, ax1 = plt.subplots()
        pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=False, colorbar=True, phased=False)
        # ax1.legend()
        # ax1.set_ylabel('Electroreflection (mOD)')
        ax1.set_ylabel('Electroabsorption (mOD)')

        # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=False)

        # Plots the Absorption
        ax2 = ax1.twinx()
        right_color = 'green'
        pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=False)


        # make the right axis ABS color
        # ax2.set_ylabel('Reflection (OD)', color=right_color)
        ax2.set_ylabel('Absorption (OD)', color=right_color)
        ax2.spines['right'].set_color(right_color)
        ax2.yaxis.set_tick_params(color=right_color)
        for label in ax2.get_yticklabels():
            label.set_color(right_color)


        plt.show()
# S_1_1_NPB_16K()

def rac_1_1_NPB_295K():
        # Dictionary that holds all of the data with input voltages
        data = {}
        data['voltages'] = {}

        # trans and blank will have strings as their voltage value, but each voltage will be an integer
        data['blank'] = rcf.read_trans_data_old(1707)
        data['trans'] = rcf.read_trans_data_old(1708)


        # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
        
        data['voltages'][100] = rcf.read_trans_data_old(1709) # voltage_file
        data['voltages'][150] = rcf.read_trans_data_old(1710) # voltage_file
        data['voltages'][200] = rcf.read_trans_data_old(1711) # voltage_file
        data['voltages'][250] = rcf.read_trans_data_old(1712) # voltage_file        
        data['voltages'][300] = rcf.read_trans_data_old(1713) # voltage_file
        # data['voltages'][350] = rcf.read_trans_data_old(1714) # voltage_file
        

        # check_phase(data)
        # plots the EA
        fig, ax1 = plt.subplots()
        pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=False, colorbar=True, phased=True,flip=True)
        # ax1.legend()
        # ax1.set_ylabel('Electroreflection (mOD)')
        ax1.set_ylabel('Electroabsorption (mOD)')

        # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=300, smooth=False, energy=False)

        # Plots the Absorption
        ax2 = ax1.twinx()
        right_color = 'green'
        pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=False)


        # make the right axis ABS color
        # ax2.set_ylabel('Reflection (OD)', color=right_color)
        ax2.set_ylabel('Absorption (OD)', color=right_color)
        ax2.spines['right'].set_color(right_color)
        ax2.yaxis.set_tick_params(color=right_color)
        for label in ax2.get_yticklabels():
            label.set_color(right_color)


        # plt.show()
# rac_1_1_NPB_295K()

def rac_1_1_NPB_16K():
        # Dictionary that holds all of the data with input voltages
        data = {}
        data['voltages'] = {}

        # trans and blank will have strings as their voltage value, but each voltage will be an integer
        data['blank'] = rcf.read_trans_data_old(1707)
        data['trans'] = rcf.read_trans_data_old(1715)

        
        data['voltages'][100] = rcf.read_trans_data_old(1716) # voltage_file
        data['voltages'][125] = rcf.read_trans_data_old(1717) # voltage_file
        data['voltages'][150] = rcf.read_trans_data_old(1718) # voltage_file
        data['voltages'][175] = rcf.read_trans_data_old(1728) # voltage_file        
        data['voltages'][200] = rcf.read_trans_data_old(1727) # voltage_file
        data['voltages'][225] = rcf.read_trans_data_old(1721) # voltage_file
        data['voltages'][250] = rcf.read_trans_data_old(1722) # voltage_file
        data['voltages'][275] = rcf.read_trans_data_old(1723) # voltage_file        
        data['voltages'][300] = rcf.read_trans_data_old(1724) # voltage_file
        data['voltages'][325] = rcf.read_trans_data_old(1725) # voltage_file
        data['voltages'][350] = rcf.read_trans_data_old(1726) # voltage_file        

        # check_phase(data)
        # plots the EA
        fig, ax1 = plt.subplots()
        pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=False, colorbar=True, phased=False,flip=True)
        # ax1.legend()
        # ax1.set_ylabel('Electroreflection (mOD)')
        ax1.set_ylabel('Electroabsorption (mOD)')

        # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=300, smooth=False, energy=False)

        # Plots the Absorption
        ax2 = ax1.twinx()
        right_color = 'green'
        pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=False)


        # make the right axis ABS color
        # ax2.set_ylabel('Reflection (OD)', color=right_color)
        ax2.set_ylabel('Absorption (OD)', color=right_color)
        ax2.spines['right'].set_color(right_color)
        ax2.yaxis.set_tick_params(color=right_color)
        for label in ax2.get_yticklabels():
            label.set_color(right_color)


        plt.show()
# rac_1_1_NPB_16K()

"""Kentucky Plots, Kevin (CHDA, CHDMA, 4-AMP, 4-AMPY)"""

"""4-AMP_SnI4 6-11-25"""
def AMP4_SnI4_295K_3():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1842)
    data['trans'] = rcf.read_trans_data(1843)

    # # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    # data['voltages'][100] = rcf.read_trans_data(1833) # voltage_file
    # data['voltages'][150] = -rcf.read_trans_data(1834) # voltage_file
    # data['voltages'][150]['Digikrom Spectr.:0 (?)'] *= -1
    # data['voltages'][200] = rcf.read_trans_data(1835) # voltage_file
    # data['voltages'][250] = rcf.read_trans_data(1836) # voltage_file
    # data['voltages'][300] = rcf.read_trans_data(1839) # voltage_file
    # data['voltages'][350] = rcf.read_trans_data(1838) # voltage_file
    # data['voltages'][400] = rcf.read_trans_data(1209) # voltage_file


    # plots the EA
    fig, ax1 = plt.subplots()
    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=True)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'
    data['trans'] = rcf.read_trans_data(1831)
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=True)
    ax2.axhline

    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)
    plt.show()
# AMP4_SnI4_295K_3()


"""4-AMP_SnI4 6-10-25"""
def AMP4_SnI4_295K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1830)
    data['trans'] = rcf.read_trans_data(1832)

    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(1833) # voltage_file
    data['voltages'][150] = -rcf.read_trans_data(1834) # voltage_file
    data['voltages'][150]['Digikrom Spectr.:0 (?)'] *= -1
    data['voltages'][200] = rcf.read_trans_data(1835) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1836) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1839) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1838) # voltage_file
    # data['voltages'][400] = rcf.read_trans_data(1209) # voltage_file


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=True)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'
    data['trans'] = rcf.read_trans_data(1831)
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True)

    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)
    plt.show()
# AMP4_SnI4_295K()

"""4-AMP_SnI4 6-10-25"""
def AMP4_SnI4_17K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1830)
    data['trans'] = rcf.read_trans_data(1841)

    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    # data['voltages'][100] = rcf.read_trans_data(1833) # voltage_file
    # data['voltages'][150] = -rcf.read_trans_data(1834) # voltage_file
    # data['voltages'][200] = rcf.read_trans_data(1835) # voltage_file
    # data['voltages'][250] = rcf.read_trans_data(1836) # voltage_file
    # data['voltages'][300] = rcf.read_trans_data(1839) # voltage_file
    # data['voltages'][350] = rcf.read_trans_data(1838) # voltage_file
    # data['voltages'][400] = rcf.read_trans_data(1209) # voltage_file


    # plots the EA
    fig, ax1 = plt.subplots()
    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=True)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

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
# AMP4_SnI4_17K()



"""CHDA"""
def CHDA_EA_16K_first():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1144)
    data['trans'] = rcf.read_trans_data(1137)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    # data['voltages'][0] = rcf.read_trans_data(545) # voltage_file
    # data_T['voltages'][200] = rcf.read_trans_data(1118) # voltage_file
    # data['voltages'][200] = rcf.read_trans_data(598) # voltage_file
    data['voltages'][100] = rcf.read_trans_data(1145) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1146) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1147) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1148) # voltage_file
    data['voltages'][300]['X (V)'] *= -1 # voltage_file
    data['voltages'][200]['X (V)'] *= -1 # voltage_file
    data['voltages'][100]['X (V)'] *= -1 # voltage_file
    data['voltages'][400]['X (V)'] *= -1 # voltage_file
    # data['voltages'][601] = rcf.read_trans_data(594) # voltage_file



    # check_phase(data)


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=200, smooth=True,energy=False)

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
# CHDA_EA_16K_first()

def CHDA_EA_295K_first():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1158)
    data['trans'] = rcf.read_trans_data(1143)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    # data['voltages'][0] = rcf.read_trans_data(545) # voltage_file
    # data_T['voltages'][200] = rcf.read_trans_data(1118) # voltage_file
    # data['voltages'][200] = rcf.read_trans_data(598) # voltage_file
    data['voltages'][100] = rcf.read_trans_data(1154) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1155) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1156) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1157) # voltage_file
    data['voltages'][100]['X (V)'] *= -1
    data['voltages'][200]['X (V)'] *= -1
    data['voltages'][300]['X (V)'] *= -1
    data['voltages'][400]['X (V)'] *= -1



    # check_phase(data)


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=200, smooth=True,energy=False)

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
# CHDA_EA_295K_first()

"""CHDMA"""
def CHDMA_EA_295K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1161)
    data['trans'] = rcf.read_trans_data(1162)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    # data['voltages'][0] = rcf.read_trans_data(545) # voltage_file
    # data_T['voltages'][200] = rcf.read_trans_data(1118) # voltage_file
    # data['voltages'][200] = rcf.read_trans_data(598) # voltage_file
    data['voltages'][100] = rcf.read_trans_data(1163) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1164) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1165) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1166) # voltage_file
    data['voltages'][100]['X (V)'] *= -1
    data['voltages'][200]['X (V)'] *= -1
    data['voltages'][300]['X (V)'] *= -1
    data['voltages'][400]['X (V)'] *= -1
    # check_phase(data)


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=200, smooth=True,energy=False)

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
# CHDMA_EA_295K()

def CHDMA_EA_16K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1167)
    data['trans'] = rcf.read_trans_data(1169)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(1170) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1174) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1171) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1173) # voltage_file

    # check_phase(data)


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')
    ax1.set_ylim(-10,4)

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=300, smooth=True,energy=False)

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
# CHDMA_EA_16K()

def CHDMA_EA_17K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1175)
    data['trans'] = rcf.read_trans_data(1189)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(1190) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1191) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1188) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1192) # voltage_file
    data['voltages'][100]['X (V)'] *= -1
    data['voltages'][200]['X (V)'] *= -1
    data['voltages'][300]['X (V)'] *= -1
    data['voltages'][400]['X (V)'] *= -1

    # check_phase(data)


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=300, smooth=False,energy=True,phased=False)

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
# CHDMA_EA_17K()

"""CHDMA 2 - Short Pass Filter at 600nm"""
def CHDMA_EA_295K_2():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1340)
    data['trans'] = rcf.read_trans_data(1341)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    # data['voltages'][0] = rcf.read_trans_data(545) # voltage_file
    # data_T['voltages'][200] = rcf.read_trans_data(1118) # voltage_file
    # data['voltages'][200] = rcf.read_trans_data(598) # voltage_file
    data['voltages'][100] = rcf.read_trans_data(1342) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1343) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1344) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1345) # voltage_file
    # Need to rephase by 180 deg
    data['voltages'][100]['X (V)'] *= -1
    data['voltages'][200]['X (V)'] *= -1
    data['voltages'][300]['X (V)'] *= -1
    data['voltages'][400]['X (V)'] *= -1
    # check_phase(data)


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=200, smooth=True,energy=False)

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
# CHDMA_EA_295K_2()

# fig, ax1 = plt.subplots()
# ax2=ax1.twinx()

def CHDMA_16K_400_600():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1346)
    data['trans'] = rcf.read_trans_data(1354)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_voltage_series_data(1370)[100] # voltage_file
    data['voltages'][200] = rcf.read_voltage_series_data(1370)[200] # voltage_file
    data['voltages'][300] = rcf.read_voltage_series_data(1370)[300] # voltage_file
    data['voltages'][400] = rcf.read_voltage_series_data(1370)[400] # voltage_file
    # data['voltages'][401] = rcf.read_trans_data(1232) # voltage_file, isn't at 500V. It's the 400V with the short pass filter
    data['voltages'][100]['X (V)'] *= -1
    data['voltages'][200]['X (V)'] *= -1
    data['voltages'][300]['X (V)'] *= -1
    data['voltages'][400]['X (V)'] *= -1
    # # check_phase(data)


    # plots the EA
    # fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=False,energy=True,phased=False,color='red')

    # Plots the Absorption
    # ax2 = ax1.twinx()
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=True)


    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    # ax2.set_ylabel('Absorption (OD)', color=right_color)
    # ax2.spines['right'].set_color(right_color)
    # ax2.yaxis.set_tick_params(color=right_color)
    # for label in ax2.get_yticklabels():
    #     label.set_color(right_color)


    # plt.show()
# CHDMA_16K_400_600()

def CHDMA_16K_580_700():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1347)
    data['trans'] = rcf.read_trans_data(1348)

    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_voltage_series_data(1371)[100] # voltage_file
    data['voltages'][200] = rcf.read_voltage_series_data(1371)[200] # voltage_file
    data['voltages'][300] = rcf.read_voltage_series_data(1371)[300] # voltage_file
    data['voltages'][400] = rcf.read_voltage_series_data(1371)[400] # voltage_file
    # data['voltages'][401] = rcf.read_trans_data(1232) # voltage_file, isn't at 500V. It's the 400V with the short pass filter
    # data['voltages'][100]['X (V)'][:40] -= 0.5e-11
    # data['voltages'][200]['X (V)'][:40] -= 2e-11
    # data['voltages'][300]['X (V)'][:40] -= 3e-11
    # data['voltages'][400]['X (V)'][:40] -= 3e-11
    # check_phase(data)


    # plots the EA
    # fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=False, colorbar=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=False,energy=True,phased=False,color='red')

    # Plots the Absorption
    # ax2 = ax1.twinx()
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
# CHDMA_16K_580_700()

"""4-AMP - Bad Sample"""

def AMP4_295K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1196)
    data['trans'] = rcf.read_trans_data(1197)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(1198) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1199) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1200) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1201) # voltage_file

    # check_phase(data)


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=300, smooth=False,energy=True,phased=False)

    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True)


    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)


    plt.show()
# AMP4_295K()

def AMP4_16K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1196)
    data['trans'] = rcf.read_trans_data(1204)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(1207) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1208) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1209) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1206) # voltage_file

    # check_phase(data)


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=300, smooth=False,energy=True,phased=False)

    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True)


    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)


    plt.show()
# AMP4_16K()

"""4-AMPY"""

def AMPY4_295K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1221)
    data['trans'] = rcf.read_trans_data(1222)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(1223) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1224) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1225) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1226) # voltage_file

    # check_phase(data)


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=100, smooth=False,energy=True,phased=False)

    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True)


    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)


    plt.show()
    # # AMPY4_295K()

    # # fig, ax1 = plt.subplots()
    # # ax2=ax1.twinx()

    # # The shift between the two separate scans is not going away, and there isn't an easy way to correct it.
    # # The biggest issue is that the zero point does not fall at the same spot for both scans. So, 
    # # shifting by adding would be the ideal solution, but that does not work because it shifts everything, making the
    # # plot diverge at higher energies, even though the plot there should go to 0.
    # # I half-fixed the problem by actually shifting the 590-700nm data - keep in mind that there is still some PL
    # # in the lower part of that range, hence, that explains why the signals b4/after the short pass are different.
    # # I just shifted the first 40 points ie, up to 630nm, but that's more of a bandaid solution than anything else.
    # # Thus, I am sending that plot with the caveat that it may not be an accurate representation of the actual data, and
    # # then sending separate plots for each range as well.
    # def AMPY4_16K_400_600():
    #     # Dictionary that holds all of the data with input voltages
    #     data = {}
    #     data['voltages'] = {}

    #     # trans and blank will have strings as their voltage value, but each voltage will be an integer
    #     data['blank'] = rcf.read_trans_data(1292)
    #     data['trans'] = rcf.read_trans_data(1291)


    #     # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    #     data['voltages'][100] = rcf.read_trans_data(1282) # voltage_file
    #     data['voltages'][200] = rcf.read_trans_data(1283) # voltage_file
    #     data['voltages'][300] = rcf.read_trans_data(1284) # voltage_file
    #     data['voltages'][400] = rcf.read_trans_data(1285) # voltage_file
    #     # data['voltages'][401] = rcf.read_trans_data(1232) # voltage_file, isn't at 500V. It's the 400V with the short pass filter
    #     value = -1
    #     data['voltages'][100]['X (V)'] *= value
    #     data['voltages'][200]['X (V)'] *= value 
    #     data['voltages'][300]['X (V)'] *= value 
    #     data['voltages'][400]['X (V)'] *= value 
    #     # # check_phase(data)


    #     # plots the EA
    #     # fig, ax1 = plt.subplots()
    #     pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=False)
    #     # ax1.set_ylabel('Electroreflection (mOD)')
    #     ax1.set_ylabel('Electroabsorption (mOD)')

    #     # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=False,energy=True,phased=False,color='red')

    #     # Plots the Absorption
    #     # ax2 = ax1.twinx()
    #     right_color = 'green'
    #     pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=True)


    #     # make the right axis ABS color
    #     # ax2.set_ylabel('Reflection (OD)', color=right_color)
    #     # ax2.set_ylabel('Absorption (OD)', color=right_color)
    #     # ax2.spines['right'].set_color(right_color)
    #     # ax2.yaxis.set_tick_params(color=right_color)
    #     # for label in ax2.get_yticklabels():
    #     #     label.set_color(right_color)


    #     # plt.show()
    # # AMPY4_16K_400_600()

def AMPY4_16K_590_700():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1293)
    data['trans'] = rcf.read_trans_data(1290)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(1289) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1288) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1287) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1286) # voltage_file
    # data['voltages'][401] = rcf.read_trans_data(1232) # voltage_file, isn't at 500V. It's the 400V with the short pass filter
    data['voltages'][100]['X (V)'][:40] -= 0.5e-11
    data['voltages'][200]['X (V)'][:40] -= 2e-11
    data['voltages'][300]['X (V)'][:40] -= 3e-11
    data['voltages'][400]['X (V)'][:40] -= 3e-11
    data['voltages'][100]['X (V)'] *= -1
    data['voltages'][200]['X (V)'] *= -1 
    data['voltages'][300]['X (V)'] *= -1 
    data['voltages'][400]['X (V)'] *= -1 
    # check_phase(data)


    # plots the EA
    # fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=False, colorbar=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=False,energy=True,phased=False,color='red')

    # Plots the Absorption
    # ax2 = ax1.twinx()
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
# AMPY4_16K_590_700()

""" PM6 """
def PM6_EA():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    # data['blank'] = rcf.read_trans_data(1032)
    data['trans'] = rcf.read_trans_data(1033)


    # data['voltages'][300] = rcf.read_trans_data(1010) # voltage_file
    # data['voltages'][400] = rcf.read_trans_data(1011) # voltage_file
    data['voltages'][500] = rcf.read_trans_data(1012) # voltage_file

    # plots the EA
    # fig, ax1 = plt.subplots()
    ax1.set_ylim(-0.15,0.15)
    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma', smooth=True, energy=True, phased=True)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=True,color='blue',energy=True,legend='PM6')

    # Plots the Absorption
    # ax2 = ax1.twinx()
    # ax2.set_ylim(0.07,0.095)
    # right_color = 'green'
    # pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True,legend='Abs')


    # # make the right axis ABS color
    # # ax2.set_ylabel('Reflection (OD)', color=right_color)
    # ax2.set_ylabel('Absorption (OD)', color=right_color)
    # ax2.spines['right'].set_color(right_color)
    # ax2.yaxis.set_tick_params(color=right_color)
    # for label in ax2.get_yticklabels():
    #     label.set_color(right_color)

    # plt.title('PM6 Electroabsorption Spectra')
    # plt.show()
# PM6_EA()

def PM6_ER():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    # data['blank'] = rcf.read_trans_data(1031)
    data['trans'] = rcf.read_trans_data(1029)


    # data['voltages'][300] = rcf.read_trans_data(1025) # voltage_file
    # data['voltages'][400] = rcf.read_trans_data(1026) # voltage_file
    data['voltages'][500] = rcf.read_trans_data(1027) # voltage_file

    # check_phase(data)


    # plots the EA
    # fig, ax1 = plt.subplots()
    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma', smooth=True, energy=True, phased=False)
    ax1.set_ylim(-0.15,0.15)
    ax1.set_ylabel('Electroreflection (mOD)')
    # ax1.set_ylabel('Electroabsorption (mOD)')

    pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=True,color='blue',energy=True,legend='PM6')

    # # Plots the Absorption
    # ax2 = ax1.twinx()
    # right_color = 'green'
    # pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True,legend='Reflection')


    # # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    # ax2.set_ylim(-0.08,-0.06)
    # ax2.spines['right'].set_color(right_color)
    # ax2.yaxis.set_tick_params(color=right_color)
    # for label in ax2.get_yticklabels():
    #     label.set_color(right_color)

    # plt.title('PM6 Electroreflection Spectra')
    # plt.show()
# PM6_ER()

""" 2-1 PM6Y6 """
def PM6Y6_21_ER():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    # data['blank'] = rcf.read_trans_data(1056)
    data['trans'] = rcf.read_trans_data(1060)

    # data['voltages'][300] = rcf.read_trans_data(1061) # voltage_file
    # data['voltages'][400] = rcf.read_trans_data(1062) # voltage_file
    data['voltages'][500] = rcf.read_trans_data(1063) # voltage_file
    # Data needs to be flipped (phased 180 deg wrong)
    # data['voltages'][300] *= -1 # voltage_file
    # data['voltages'][400] *= -1 # voltage_file
    data['voltages'][500] *= -1 # voltage_file

    # check_phase(data)

    # plots the EA
    # fig, ax1 = plt.subplots() 
    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma', smooth=True, energy=True, phased=False)
    ax1.set_ylim(-0.3,0.2)
    ax1.set_ylabel('Electroreflection (mOD)')
    # ax1.set_ylabel('Electroabsorption (mOD)')

    pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=True,color='black',energy=True,legend='2:1 PM6Y6')

    # # Plots the Absorption
    # ax2 = ax1.twinx()
    # right_color = 'green'
    # pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True,legend='Reflection')


    # # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    # # ax2.set_ylim(-0.5,0.5)
    # # ax2.set_ylabel('Absorption (OD)', color=right_color)
    # ax2.spines['right'].set_color(right_color)
    # ax2.yaxis.set_tick_params(color=right_color)
    # for label in ax2.get_yticklabels():
    #     label.set_color(right_color)

    # plt.title('2:1 PM6Y6 Electroreflection Spectra')
    # plt.show()
# PM6Y6_21_ER()

def PM6Y6_21_ER_new():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1056)
    data['trans'] = rcf.read_trans_data(1071)

    data['voltages'][500] = rcf.read_trans_data(1072) # voltage_file


    # check_phase(data)

    # plots the EA
    fig, ax1 = plt.subplots() 
    # ax1.set_ylim(0,0.2)
    ax1.set_ylabel('Electroreflection (mOD)')
    # ax1.set_ylabel('Electroabsorption (mOD)')

    pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=False)

    plt.title('2:1 PM6Y6 Electroreflection Spectra')
    plt.show()
# PM6Y6_21_ER_new()

def PM6Y6_21_EA():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    # data['blank'] = rcf.read_trans_data(1064)
    data['trans'] = rcf.read_trans_data(1067)


    # data['voltages'][300] = rcf.read_trans_data(1068) # voltage_file
    # data['voltages'][400] = rcf.read_trans_data(1069) # voltage_file
    data['voltages'][500] = rcf.read_trans_data(1070) # voltage_file
    # Data needs to be flipped (phased 180 deg wrong)
    # data['voltages'][300] *= -1 # voltage_file
    # data['voltages'][400] *= -1 # voltage_file
    # data['voltages'][500] *= -1 # voltage_file
    
    # plots the EA
    # fig, ax1 = plt.subplots()
    # ax1.set_ylim(0,0.15)
    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma', smooth=True, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=True,color='black',energy=True,legend='2:1 PM6Y6')
    
    # # Plots the Absorption
    # ax2 = ax1.twinx()
    # # ax2.set_ylim(0.04,0.1)
    # right_color = 'green'
    # pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True,legend='Abs')


    # # make the right axis ABS color
    # # ax2.set_ylabel('Reflection (OD)', color=right_color)
    # ax2.set_ylabel('Absorption (OD)', color=right_color)
    # ax2.spines['right'].set_color(right_color)
    # ax2.yaxis.set_tick_params(color=right_color)
    # for label in ax2.get_yticklabels():
    #     label.set_color(right_color)

    # plt.title('2:1 PM6Y6 Electroabsorption Spectra')
    # plt.show()
# PM6Y6_21_EA()

""" 1-1.2 PM6Y6 """
def PM6Y6_112_ER():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    # data['blank'] = rcf.read_trans_data(1073)
    data['trans'] = rcf.read_trans_data(1075)

    # data['voltages'][300] = rcf.read_trans_data(1077) # voltage_file
    # data['voltages'][400] = rcf.read_trans_data(1078) # voltage_file
    data['voltages'][500] = rcf.read_trans_data(1079) # voltage_file
    value = 300
    # data['voltages'][300]['X (V)'] -= data['voltages'][300]['X (V)'][value]
    # data['voltages'][400]['X (V)'] -= data['voltages'][400]['X (V)'][value]
    data['voltages'][500]['X (V)'] -= data['voltages'][500]['X (V)'][value]


    # check_phase(data)

    # plots the EA
    # fig, ax1 = plt.subplots()
    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma', smooth=True, energy=True, phased=False)
    ax1.set_ylim(-0.2,0.2)
    ax1.set_ylabel('Electroreflection (mOD)')
    # ax1.set_ylabel('Electroabsorption (mOD)')

    pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=True,color='cyan',energy=True,legend='1:1.2 PM6Y6',phased=False)

    # # Plots the Absorption
    # ax2 = ax1.twinx()
    # right_color = 'green'
    # pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True,legend='Reflection')


    # # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    # # ax2.set_ylim(-0.5,0.5)
    # # ax2.set_ylabel('Absorption (OD)', color=right_color)
    # ax2.spines['right'].set_color(right_color)
    # ax2.yaxis.set_tick_params(color=right_color)
    # for label in ax2.get_yticklabels():
    #     label.set_color(right_color)

    # plt.title('1:1.2 PM6Y6 Electroreflection Spectra')
    # plt.show()
# PM6Y6_112_ER()

def PM6Y6_112_EA():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    # data['blank'] = rcf.read_trans_data(1080)
    data['trans'] = rcf.read_trans_data(1083)


    # data['voltages'][300] = rcf.read_trans_data(1084) # voltage_file
    # data['voltages'][400] = rcf.read_trans_data(1085) # voltage_file
    data['voltages'][500] = rcf.read_trans_data(1086) # voltage_file
    # value = 300
    # data['voltages'][300]['X (V)'] -= data['voltages'][300]['X (V)'][value]
    # data['voltages'][400]['X (V)'] -= data['voltages'][400]['X (V)'][value]
    # data['voltages'][500]['X (V)'] -= data['voltages'][500]['X (V)'][value]
    
    # plots the EA
    # fig, ax1 = plt.subplots()
    # ax1.set_ylim(0,0.15)
    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma', smooth=True, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=True,color='cyan',energy=True,legend='1:1.2 PM6Y6')

    # # Plots the Absorption
    # ax2 = ax1.twinx()
    # # ax2.set_ylim(0.04,0.1)
    # right_color = 'green'
    # pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True,legend='Abs')


    # # make the right axis ABS color
    # # ax2.set_ylabel('Reflection (OD)', color=right_color)
    # ax2.set_ylabel('Absorption (OD)', color=right_color)
    # ax2.spines['right'].set_color(right_color)
    # ax2.yaxis.set_tick_params(color=right_color)
    # for label in ax2.get_yticklabels():
    #     label.set_color(right_color)

    # plt.title('1:1.2 PM6Y6 Electroabsorption Spectra')
    # plt.show()
# PM6Y6_112_EA()

""" 1-2 PM6Y6 """
def PM6Y6_12_ER():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    # data['blank'] = rcf.read_trans_data(1034)
    data['trans'] = rcf.read_trans_data(1037)

    # data['voltages'][300] = rcf.read_trans_data(1038) # voltage_file
    # data['voltages'][400] = rcf.read_trans_data(1039) # voltage_file
    data['voltages'][500] = rcf.read_trans_data(1040) # voltage_file
    value = 300
    # data['voltages'][300]['X (V)'] -= data['voltages'][300]['X (V)'][value]
    # data['voltages'][400]['X (V)'] -= data['voltages'][400]['X (V)'][value]
    data['voltages'][500]['X (V)'] -= data['voltages'][500]['X (V)'][value]
    # data['voltages'][300]['X (V)'] += 1.4202172e-12
    # data['voltages'][400]['X (V)'] += 4.2003812e-12
    # data['voltages'][500]['X (V)'] += 1.0245343e-11
    # check_phase(data)

    # plots the EA
    # fig, ax1 = plt.subplots() 
    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma', smooth=True, energy=True, phased=False)
    ax1.set_ylim(-0.1,1.5)
    ax1.set_ylabel('Electroreflection (mOD)')
    # ax1.set_ylabel('Electroabsorption (mOD)')

    pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=True,color='magenta',energy=True,legend='1:2 PM6Y6',phased=False)

    # # Plots the Absorption
    # ax2 = ax1.twinx()
    # right_color = 'green'
    # pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True,legend='Reflection')

    # # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    # # ax2.legend(loc='upper left')
    # # ax2.set_ylim(-0.5,0.5)
    # # ax2.set_ylabel('Absorption (OD)', color=right_color)
    # ax2.spines['right'].set_color(right_color)
    # ax2.yaxis.set_tick_params(color=right_color)
    # for label in ax2.get_yticklabels():
    #     label.set_color(right_color)

    # plt.title('1:2 PM6Y6 Electroreflection Spectra')
    # plt.show()
# PM6Y6_12_ER()

def PM6Y6_12_EA():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    # data['blank'] = rcf.read_trans_data(1041)
    data['trans'] = rcf.read_trans_data(1044)


    # data['voltages'][300] = rcf.read_trans_data(1045) # voltage_file
    # data['voltages'][400] = rcf.read_trans_data(1046) # voltage_file
    data['voltages'][500] = rcf.read_trans_data(1047) # voltage_file
    # value = 61
    # data['voltages'][300]['X (V)'] -= data['voltages'][300]['X (V)'][value]
    # data['voltages'][400]['X (V)'] -= data['voltages'][400]['X (V)'][value]
    # data['voltages'][500]['X (V)'] -= data['voltages'][500]['X (V)'][value]

    # plots the EA
    # fig, ax1 = plt.subplots()
    ax1.set_ylim(-10,30)
    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma', smooth=True, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=True,color='magenta',energy=True,legend='1:2 PM6Y6')

    # # Plots the Absorption
    # ax2 = ax1.twinx()
    # ax2.set_ylim(0,1.6)
    # right_color = 'green'
    # pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True,legend='Abs')


    # # make the right axis ABS color
    # # ax2.set_ylabel('Reflection (OD)', color=right_color)
    # ax2.set_ylabel('Absorption (OD)', color=right_color)
    # ax2.spines['right'].set_color(right_color)
    # ax2.yaxis.set_tick_params(color=right_color)
    # for label in ax2.get_yticklabels():
    #     label.set_color(right_color)

    # plt.title('1:2 PM6Y6 Electroabsorption Spectra')
    # plt.show()
# PM6Y6_12_EA()

""" Y6 data """
def Y6_ER():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    # data['blank'] = rcf.read_trans_data(1087)
    data['trans'] = rcf.read_trans_data(1090)

    # data['voltages'][300] = rcf.read_trans_data(1091) # voltage_file
    # data['voltages'][400] = rcf.read_trans_data(1092) # voltage_file
    data['voltages'][500] = rcf.read_trans_data(1093) # voltage_file
    # value = 250
    # data['voltages'][300]['X (V)'] -= data['voltages'][300]['X (V)'][value]
    # data['voltages'][400]['X (V)'] -= data['voltages'][400]['X (V)'][value]
    # data['voltages'][500]['X (V)'] -= data['voltages'][500]['X (V)'][value]

    # check_phase(data)

    # plots the EA
    # fig, ax1 = plt.subplots() 
    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma', smooth=True, energy=True, phased=False)
    ax1.set_ylim(-0.1,0.4)
    ax1.set_ylabel('Electroreflection (mOD)')
    # ax1.set_ylabel('Electroabsorption (mOD)')

    pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=True,color='red',energy=True,legend='Y6')

    # # Plots the Absorption
    # ax2 = ax1.twinx()
    # right_color = 'green'
    # pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True,legend='Reflection')


    # # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    # # ax2.set_ylim(-0.5,0.5)
    # # ax2.set_ylabel('Absorption (OD)', color=right_color)
    # ax2.spines['right'].set_color(right_color)
    # ax2.yaxis.set_tick_params(color=right_color)
    # for label in ax2.get_yticklabels():
    #     label.set_color(right_color)

    # plt.title('Y6 Electroreflection Spectra')
    ax1.set_ylim(-0.3,0.3)
    ax1.set_ylabel('Electroreflection (mOD)')
    plt.show()
# Y6_ER()

def Y6_EA():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    # data['blank'] = rcf.read_trans_data(1094)
    data['trans'] = rcf.read_trans_data(1097)


    # data['voltages'][300] = rcf.read_trans_data(1098) # voltage_file
    # data['voltages'][400] = rcf.read_trans_data(1099) # voltage_file
    data['voltages'][500] = rcf.read_trans_data(1100) # voltage_file
    # value = 300
    # data['voltages'][300]['X (V)'] -= data['voltages'][300]['X (V)'][value]
    # data['voltages'][400]['X (V)'] -= data['voltages'][400]['X (V)'][value]
    # data['voltages'][500]['X (V)'] -= data['voltages'][500]['X (V)'][value]
    
    # plots the EA
    # fig, ax1 = plt.subplots()
    # ax1.set_ylim(0,0.15)
    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma', smooth=True, energy=True, phased=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=True,color='red',energy=True,legend='Y6')

    # # Plots the Absorption
    # ax2 = ax1.twinx()
    # # ax2.set_ylim(0.04,0.1)
    # right_color = 'green'
    # pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True,legend='Abs')


    # # make the right axis ABS color
    # # ax2.set_ylabel('Reflection (OD)', color=right_color)
    # ax2.set_ylabel('Absorption (OD)', color=right_color)
    # ax2.spines['right'].set_color(right_color)
    # ax2.yaxis.set_tick_params(color=right_color)
    # for label in ax2.get_yticklabels():
    #     label.set_color(right_color)

    # plt.title('Y6 Electroabsorption Spectra')
    plt.show()
# Y6_EA()

""" 4-F PESI Kentucky """
def PESI4F_or_normal():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1395)
    data['trans'] = rcf.read_trans_data(1396)


    data['voltages'][100] = rcf.read_trans_data(1388) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(1389) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1390) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1391) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1392) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1393) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1394) # voltage_file

    value = -1
    data['voltages'][100]['X (V) Phased'] *= value
    data['voltages'][150]['X (V) Phased'] *= value 
    data['voltages'][200]['X (V) Phased'] *= value 
    data['voltages'][250]['X (V) Phased'] *= value
    data['voltages'][300]['X (V) Phased'] *= value 
    data['voltages'][350]['X (V) Phased'] *= value 
    data['voltages'][400]['X (V) Phased'] *= value 
    
    # plots the EA
    fig, ax1 = plt.subplots()
    # ax1.set_ylim(0,0.15)
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=True)
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=300, smooth=True,color='red',energy=True,legend='4-F PESI 300V')

    # Plots the Absorption
    ax2 = ax1.twinx()
    ax2.set_ylim(0,2)
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True,legend='Abs')


    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)

    plt.title('PESI Electroabsorption Spectra')
    plt.show()
# PESI4F_or_normal()

def PESI4F_or_normal2():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1405)
    data['trans'] = rcf.read_trans_data(1404)


    data['voltages'][100] = rcf.read_trans_data(1397) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(1398) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1399) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1400) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1401) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1402) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1403) # voltage_file

    value = -1
    data['voltages'][100]['X (V) Phased'] *= value
    data['voltages'][150]['X (V) Phased'] *= value 
    data['voltages'][200]['X (V) Phased'] *= value 
    data['voltages'][250]['X (V) Phased'] *= value
    data['voltages'][300]['X (V) Phased'] *= value 
    data['voltages'][350]['X (V) Phased'] *= value 
    data['voltages'][400]['X (V) Phased'] *= value 
    
    # plots the EA
    fig, ax1 = plt.subplots()
    # ax1.set_ylim(0,0.15)
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=True)
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=300, smooth=True,color='red',energy=True,legend='4-F PESI 300V')

    # Plots the Absorption
    ax2 = ax1.twinx()
    ax2.set_ylim(0,2)
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True,legend='Abs')


    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)

    plt.title('PESI Electroabsorption Spectra')
    plt.show()
# PESI4F_or_normal2()

def PESI2CF3():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(154)
    data['trans'] = rcf.read_trans_data(155)


    data['voltages'][100] = rcf.read_trans_data(159) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(158) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(157) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(156) # voltage_file
    # data['voltages'][275] = rcf.read_trans_data(245) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(160) # voltage_file

    value = -1
    data['voltages'][100]['X (V) Phased'] *= value
    data['voltages'][150]['X (V) Phased'] *= value 
    data['voltages'][200]['X (V) Phased'] *= value 
    data['voltages'][250]['X (V) Phased'] *= value
    data['voltages'][300]['X (V) Phased'] *= value 
    
    # plots the EA
    fig, ax1 = plt.subplots()
    # ax1.set_ylim(0,0.15)
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=True)
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=300, smooth=True,color='red',energy=True,legend='4-F PESI 300V')

    # Plots the Absorption
    ax2 = ax1.twinx()
    ax2.set_ylim(0,2)
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True,legend='Abs')


    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)

    plt.title('2-CF3 PESI Electroabsorption Spectra')
    plt.show()
# PESI2CF3()

def PESI4F():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(239)
    data['trans'] = rcf.read_trans_data(238)


    data['voltages'][100] = rcf.read_trans_data(244) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(243) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(242) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(241) # voltage_file
    data['voltages'][275] = rcf.read_trans_data(245) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(240) # voltage_file
    
    # plots the EA
    fig, ax1 = plt.subplots()
    # ax1.set_ylim(0,0.15)
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=True)
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=300, smooth=True,color='red',energy=True,legend='4-F PESI 300V')

    # Plots the Absorption
    ax2 = ax1.twinx()
    ax2.set_ylim(0,2)
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True,legend='Abs')


    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)

    plt.title('4-F PESI Electroabsorption Spectra')
    plt.show()
# PESI4F()

def EA2mPESI():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1243)
    data['trans'] = rcf.read_trans_data(1244)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    # data['voltages'][0] = rcf.read_trans_data(545) # voltage_file
    # data['voltages'][100] = rcf.read_trans_data(1245) # voltage_file
    # data['voltages'][150] = rcf.read_trans_data(1246) # voltage_file
    # data['voltages'][200] = rcf.read_trans_data(1247) # voltage_file
    # data['voltages'][250] = rcf.read_trans_data(1248) # voltage_file
    # data['voltages'][300] = rcf.read_trans_data(1249) # voltage_file
    # data['voltages'][600] = rcf.read_trans_data(602) # voltage_file
    data['voltages'] = rcf.read_voltage_series_data(1250)

    # data['voltages'][601] = rcf.read_trans_data(594) # voltage_file



    # check_phase(data)


    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, flip=True)
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

    plt.title('4-Methyl PESI Electroabsorption Spectra')
    plt.show()
# EA2mPESI()

def EA3fPESI():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1251)
    data['trans'] = rcf.read_trans_data(1252)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    # data['voltages'][0] = rcf.read_trans_data(545) # voltage_file
    data['voltages'][100] = rcf.read_trans_data(1253) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(1254) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1255) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1256) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1257) # voltage_file
    # data['voltages'][600] = rcf.read_trans_data(602) # voltage_file
    # data['voltages'] = rcf.read_voltage_series_data(1250)

    data['voltages'][100] *= -1
    data['voltages'][150] *= -1
    data['voltages'][200] *= -1
    data['voltages'][250] *= -1
    data['voltages'][300] *= -1

    # data['voltages'][601] = rcf.read_trans_data(594) # voltage_file

    # check_phase(data)

    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True)
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
# EA3fPESI()

def EACHDMAPESI400600():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1316)
    data['trans'] = rcf.read_trans_data(1315)


    data['voltages'] = rcf.read_voltage_series_data(1314) # voltage_series_file
    # data['voltages'][0] = rcf.read_trans_data(545) # voltage_file
    # data['voltages'][100] = rcf.read_trans_data(1253) # voltage_file
    # data['voltages'][150] = rcf.read_trans_data(1254) # voltage_file
    # data['voltages'][200] = rcf.read_trans_data(1255) # voltage_file
    # data['voltages'][250] = rcf.read_trans_data(1256) # voltage_file
    # data['voltages'][300] = rcf.read_trans_data(1257) # voltage_file
    # data['voltages'][600] = rcf.read_trans_data(602) # voltage_file
    # data['voltages'] = rcf.read_voltage_series_data(1250)

    data['voltages'][100] *= -1
    data['voltages'][150] *= -1
    data['voltages'][200] *= -1
    data['voltages'][250] *= -1
    data['voltages'][300] *= -1
    data['voltages'][350] *= -1
    data['voltages'][400] *= -1


    data1 = {}
    data1['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data1['blank'] = rcf.read_trans_data(1319)
    data1['trans'] = rcf.read_trans_data(1318)


    data1['voltages'] = rcf.read_voltage_series_data(1317) # voltage_series_file

    data1['voltages'][100] *= -1
    data1['voltages'][150] *= -1
    data1['voltages'][200] *= -1
    data1['voltages'][250] *= -1
    data1['voltages'][300] *= -1
    data1['voltages'][350] *= -1
    data1['voltages'][400] *= -1

    # data['voltages'][601] = rcf.read_trans_data(594) # voltage_file

    # check_phase(data)

    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, data1, ax=ax1, color_map_name='plasma_r', smooth=True, energy=False)
    # pcg.plot_EA_series(data1, ax=ax1, color_map_name='plasma_r', smooth=True, energy=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=100, smooth=False)

    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=False)


    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)


    plt.show()
# EACHDMAPESI400600()

def EACHDMAPESI580700():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1319)
    data['trans'] = rcf.read_trans_data(1318)


    data['voltages'] = rcf.read_voltage_series_data(1317) # voltage_series_file
    # data['voltages'][0] = rcf.read_trans_data(545) # voltage_file
    # data['voltages'][100] = rcf.read_trans_data(1253) # voltage_file
    # data['voltages'][150] = rcf.read_trans_data(1254) # voltage_file
    # data['voltages'][200] = rcf.read_trans_data(1255) # voltage_file
    # data['voltages'][250] = rcf.read_trans_data(1256) # voltage_file
    # data['voltages'][300] = rcf.read_trans_data(1257) # voltage_file
    # data['voltages'][600] = rcf.read_trans_data(602) # voltage_file
    # data['voltages'] = rcf.read_voltage_series_data(1250)

    data['voltages'][100] *= -1
    data['voltages'][150] *= -1
    data['voltages'][200] *= -1
    data['voltages'][250] *= -1
    data['voltages'][300] *= -1
    data['voltages'][350] *= -1
    data['voltages'][400] *= -1

    # data['voltages'][601] = rcf.read_trans_data(594) # voltage_file

    # check_phase(data)

    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=False)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=100, smooth=False)

    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=False)


    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)


    plt.show()
# EACHDMAPESI580700()

def EA4fPESIn():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1258)
    data['trans'] = rcf.read_trans_data(1259)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    # data['voltages'][0] = rcf.read_trans_data(545) # voltage_file
    data['voltages'][100] = rcf.read_trans_data(1260) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(1261) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1262) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1263) # voltage_file
    data['voltages'][275] = rcf.read_trans_data(1264) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1265) # voltage_file
    # data['voltages'] = rcf.read_voltage_series_data(1250)

    # data['voltages'][601] = rcf.read_trans_data(594) # voltage_file

    # check_phase(data)

    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True)
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
# EA4fPESIn()

def EA2CF3PESI():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1266)
    data['trans'] = rcf.read_trans_data(1267)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    # data['voltages'][0] = rcf.read_trans_data(545) # voltage_file
    data['voltages'][100] = rcf.read_trans_data(1268) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(1269) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1270) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1271) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1272) # voltage_file
    # data['voltages'] = rcf.read_voltage_series_data(1250)

    # data['voltages'][100] *= -1
    # data['voltages'][150] *= -1
    # data['voltages'][200] *= -1
    # data['voltages'][250] *= -1
    # data['voltages'][300] *= -1

    # data['voltages'][601] = rcf.read_trans_data(594) # voltage_file

    # check_phase(data)

    # plots the EA
    fig, ax1 = plt.subplots()
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True)
    # ax1.set_ylabel('Electroreflection (mOD)')
    ax1.set_ylabel('Electroabsorption (mOD)')
    ax1.set_ylim(-0.3,0.7)

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=100, smooth=False)

    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=True, )


    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)

    plt.title('2-CF3 PESI Electroabsorption Spectra')

    plt.show()
# EA2CF3PESI()

""" 4-F PESI Kentucky """
def PESI4F_new():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # # trans and blank will have strings as their voltage value, but each voltage will be an integer
    # data['blank'] = rcf.read_trans_data(1269)
    # data['trans'] = rcf.read_trans_data(1268)


    # data['voltages'][100] = rcf.read_trans_data(1259) # voltage_file
    # data['voltages'][200] = rcf.read_trans_data(1260) # voltage_file
    # data['voltages'][300] = rcf.read_trans_data(1261) # voltage_file
    # data['voltages'][400] = rcf.read_trans_data(1262) # voltage_file

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1258)
    data['trans'] = rcf.read_trans_data(1259)


    data['voltages'][100] = rcf.read_trans_data(1260) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(1261) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1262) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1263) # voltage_file
    data['voltages'][275] = rcf.read_trans_data(1264) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1265) # voltage_file

    
    # plots the EA
    fig, ax1 = plt.subplots()
    # ax1.set_ylim(0,0.15)
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=False, flip=True)
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=True,color='red',energy=True,legend='Y6')

    # Plots the Absorption
    ax2 = ax1.twinx()
    # ax2.set_ylim(0,2)
    right_color = 'green'
    pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=True, energy=True,legend='Abs')


    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)

    plt.title('4-F PESI Electroabsorption Spectra')
    plt.show()
# PESI4F_new()

""" 2-F PESI Kentucky """
def PESI_2F_295K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    export = 'C:/Data/Compiled Data/Kentcky Henry/Room temp' # Folder location to export the data


    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1399)
    data['trans'] = rcf.read_trans_data(1400)


    data['voltages'][100] = rcf.read_trans_data(1401) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(1402) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1403) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1404) # voltage_file

    
    # plots the EA
    fig, ax1 = plt.subplots()
    # ax1.set_ylim(0,0.15)
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=True, phased=True)
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=True,color='red',energy=True,legend='Y6')

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
# PESI_2F_295K()

def PESI_2F_17K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}
    export = 'C:/Data/Compiled Data/Kentcky Henry/Low temp' # Folder location to export the data

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1405)
    data['trans'] = rcf.read_trans_data(1406)


    data['voltages'][100] = rcf.read_trans_data(1407) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(1408) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1409) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1410) # voltage_file
    data['voltages'][100]['X (V) Phased'] = -data['voltages'][100]['X (V) Phased']

    # plots the EA
    fig, ax1 = plt.subplots()
    # ax1.set_ylim(0,0.15)
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=True, phased=True, flip=True)
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
# PESI_2F_17K()

def PESI_2F_17K_570_640():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1411)
    data['trans'] = rcf.read_trans_data(1412)


    # data['voltages'][100] = rcf.read_trans_data(1407) # voltage_file
    # data['voltages'][150] = rcf.read_trans_data(1408) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1413) # voltage_file
    # data['voltages'][250] = rcf.read_trans_data(1404) # voltage_file

    
    # plots the EA
    fig, ax1 = plt.subplots()
    # ax1.set_ylim(0,0.15)
    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=False, phased=True)
    ax1.set_ylabel('Electroabsorption (mOD)')

    pcg.plot_EA_voltage(data=data, ax=ax1, voltage=200, smooth=False,color='red',energy=True)

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
# PESI_2F_17K_570_640()

"""4-AMP Kentucky"""

def Kevin4AMP_295K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1431)
    data['trans'] = rcf.read_trans_data(1432)


    data['voltages'][100] = rcf.read_trans_data(1433) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(1434) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1435) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1436) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1437) # voltage_file
    # data['voltages'][201] = rcf.read_trans_data(1438) # voltage_file
    
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

    plt.title('4-AMP PESI Electroabsorption Spectra')
    plt.show()
# Kevin4AMP_295K()

def Export_data(data, filename, smooth=False):
    from pandas import DataFrame
    import public.colton_math_functions as cmf
    voltages = np.array(list(data['voltages'].keys()))

    EA_calculations = {}
    EA_calculations['Energy (eV)'] = cmf.wavelength_to_energy(data['trans']['Digikrom Spectr.:0 (?)'])
    
    if smooth:
        EA_calculations['Absorption (OD)'] = cmf.absorption_smooth(data['trans']['X (V) Phased'], data['blank']['X (V) Phased'])
        for voltage in voltages:
            EA_calculations[f'EA {voltage} (mOD)'] = cmf.EA_smooth(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])*1000

    else:
        EA_calculations['Absorption (OD)'] = cmf.absorption(data['trans']['X (V) Phased'], data['blank']['X (V) Phased'])
        for voltage in voltages:
            EA_calculations[f'EA {voltage} (mOD)'] = cmf.EA(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])*1000

    df = DataFrame(EA_calculations)

    # Export to CSV
    df.to_csv(f"C:\\Data\\Compiled Data\\{filename}", index=False) 

"""Kevin 4-AMP PESI Sample Data"""
def Kevin4AMP_295K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1431)
    data['trans'] = rcf.read_trans_data(1432)


    data['voltages'][100] = rcf.read_trans_data(1433) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(1434) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1435) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1436) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1437) # voltage_file
    # data['voltages'][201] = rcf.read_trans_data(1438) # voltage_file
    
    # plots the EA
    fig, ax1 = plt.subplots()
    # ax1.set_ylim(0,0.15)
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=True)
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

    plt.title('4-AMP PESI Electroabsorption Spectra')
    plt.show()
# Kevin4AMP_295K()

""" This is the Duke 2D sample"""
def Xi_2D_15K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1511)
    data['trans'] = rcf.read_trans_data(1512)


    data['voltages'][200] = rcf.read_trans_data(1513) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1514) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1515) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1516) # voltage_file
    
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

    plt.title('R-4-FMBA 2D @ 15K Electroabsorption Spectra')
    plt.show()
    # Export_data(data, 'Duke\\2D_15K_data.csv')
# Xi_2D_15K()

def Xi_2D_295K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1528)
    data['trans'] = rcf.read_trans_data(1529)


    # data['voltages'][200] = rcf.read_trans_data(1530) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1531) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1532) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1533) # voltage_file
    
    # plots the EA
    fig, ax1 = plt.subplots()
    # ax1.set_ylim(0,0.15)
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', export=True)
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

    plt.title('R-4-FMBA 2D @ 295K Electroabsorption Spectra')
    plt.show()
    # Export_data(data, 'Duke\\2D_295K_data.csv')
# Xi_2D_295K()


""" This is the 1.5D sample"""
def Xi_15D_295K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1517)
    data['trans'] = rcf.read_trans_data(1524)


    data['voltages'][200] = rcf.read_trans_data(1525) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1526) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1527) # voltage_file
    
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

    plt.title('R-4-FMBA 1.5D @ 295K Electroabsorption Spectra')
    plt.show()
    Export_data(data, 'Duke\\1.5D_295K_data.csv')    
# Xi_15D_295K()

def Xi_15D_15K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1517)
    data['trans'] = rcf.read_trans_data(1518)


    data['voltages'][200] = rcf.read_trans_data(1519) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1520) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1521) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1522) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1523) # voltage_file
    
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

    plt.title('R-4-FMBA 1.5D @ 15K Electroabsorption Spectra')
    plt.show()
    Export_data(data, 'Duke\\1.5D_15K_data.csv')
# Xi_15D_15K()


""" This is the 1.5D sample"""
def Xi_15D_295K_new():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1534)
    data['trans'] = rcf.read_trans_data(1535)


    data['voltages'][200] = rcf.read_trans_data(1536) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1537) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1538) # voltage_file
    
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

    plt.title('R-4-FMBA 1.5D @ 295K Electroabsorption Spectra')
    plt.show()
    Export_data(data, 'Duke\\1.5D_295K_data_new.csv')    
# Xi_15D_295K_new()




def Xi_15D_15K_new():
    ################################################################################################
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1539)
    data['trans'] = rcf.read_trans_data(1540)


    data['voltages'][150] = rcf.read_trans_data(1541) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1542) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1543) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1544) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1545) # voltage_file
    
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


    Export_data(data, 'Duke\\1.5D_15K_350nm-450nm_data.csv')
################################################################################################
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1546)
    data['trans'] = rcf.read_trans_data(1547)


    data['voltages'][150] = rcf.read_trans_data(1548) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1549) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1550) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1551) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1552) # voltage_file
    
    # plots the EA
    # fig, ax1 = plt.subplots()
    ax1.set_ylim(-0.2,0.3)
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=True, phased=True, colorbar=False)
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=200, smooth=True,color='red',energy=True)

    # Plots the Absorption
    # ax2 = ax1.twinx()
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

    plt.title('R-4-FMBA 1.5D @ 15K Electroabsorption Spectra')
    plt.show()
    Export_data(data, 'Duke\\1.5D_15K_440nm-650nm_data.csv')
# Xi_15D_15K_new()


def Xi_15D_295K_new_2():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1555)
    data['trans'] = rcf.read_trans_data(1556)


    data['voltages'][250] = rcf.read_trans_data(1557) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1558) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1559) # voltage_file
    
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

    plt.title('R-4-FMBA 1.5D @ 295K Electroabsorption Spectra')
    plt.show()
    # Export_data(data, 'Duke\\1.5D_295K_data_new_2.csv')    
# Xi_15D_295K_new_2()



def Xi_15D_15K_new_2():

    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    # data['blank'] = rcf.read_trans_data(1560)
    data['trans'] = rcf.read_trans_data(1566)


    # data['voltages'] = rcf.read_voltage_series_data(1565)
    # data['voltages'][150] = rcf.read_trans_data(1548) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1570) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1569) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1568) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1567) # voltage_file
    
    # plots the EA
    fig, ax1 = plt.subplots()
    # ax1.set_ylim(-0.2,0.3)
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=True, phased=True, colorbar=True)
    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=True, colorbar=False)
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=200, smooth=True,color='red',energy=True)

    # Plots the Absorption
    ax2 = ax1.twinx()
    # ax2.set_ylim(0,2)
    right_color = 'green'
    # pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=True,legend='Abs')

    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)

    plt.title('R-4-FMBA 1.5D @ 15K Electroabsorption Spectra')
    plt.show()
    # Export_data(data, 'Duke\\1.5D_15K_350nm-440nm_data_redone.csv')
# Xi_15D_15K_new_2()


def Xi_15D_15K_new_3():

    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    # data['blank'] = rcf.read_trans_data(1560)
    data['trans'] = rcf.read_trans_data(1571)


    data['voltages'] = rcf.read_voltage_series_data(1563)
    # data['voltages'][150] = rcf.read_trans_data(1548) # voltage_file
    # data['voltages'][200] = rcf.read_trans_data(1570) # voltage_file
    # data['voltages'][250] = rcf.read_trans_data(1569) # voltage_file
    # data['voltages'][300] = rcf.read_trans_data(1568) # voltage_file
    # data['voltages'][350] = rcf.read_trans_data(1567) # voltage_file
    
    # plots the EA
    fig, ax1 = plt.subplots()
    # ax1.set_ylim(-0.2,0.3)
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=True, phased=True, colorbar=True)
    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=True, colorbar=False)
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=200, smooth=True,color='red',energy=True)

    # Plots the Absorption
    ax2 = ax1.twinx()
    # ax2.set_ylim(0,2)
    right_color = 'green'
    # pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=True,legend='Abs')

    # make the right axis ABS color
    # ax2.set_ylabel('Reflection (OD)', color=right_color)
    ax2.set_ylabel('Absorption (OD)', color=right_color)
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)

    plt.title('R-4-FMBA 1.5D @ 15K Electroabsorption Spectra')
    plt.show()
    # Export_data(data, 'Duke\\1.5D_15K_350nm-440nm_data_redone.csv')
# Xi_15D_15K_new_3()


def Xi_15D_15K_sample2():

    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    # data['blank'] = rcf.read_trans_data(1560)
    data['trans'] = rcf.read_trans_data(1577)


    # data['voltages'] = rcf.read_voltage_series_data(1563)
    # data['voltages'][150] = rcf.read_trans_data(1548) # voltage_file
    # data['voltages'][200] = rcf.read_trans_data(1570) # voltage_file
    data['voltages'][250] = rcf.read_trans_average_data(1576) # voltage_file
    data['voltages'][300] = rcf.read_trans_average_data(1575) # voltage_file
    data['voltages'][350] = rcf.read_trans_average_data(1574) # voltage_file
    
    # plots the EA
    fig, ax1 = plt.subplots()
    # ax1.set_ylim(-0.2,0.3)
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=False, energy=True, phased=True, colorbar=True)
    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=True, energy=True, phased=True, colorbar=False)
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=200, smooth=True,color='red',energy=True)

    # Plots the Absorption
    # ax2 = ax1.twinx()
    # ax2.set_ylim(0,2)
    right_color = 'green'
    # pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=False, energy=True,legend='Abs')

    # make the right axis ABS color
    # # ax2.set_ylabel('Reflection (OD)', color=right_color)
    # ax2.set_ylabel('Absorption (OD)', color=right_color)
    # ax2.spines['right'].set_color(right_color)
    # ax2.yaxis.set_tick_params(color=right_color)
    # for label in ax2.get_yticklabels():
    #     label.set_color(right_color)

    plt.title('R-4-FMBA 1.5D @ 15K Electroabsorption Spectra')
    plt.show()
    # Export_data(data, 'Duke\\1.5D_15K_350nm-440nm_data_redone.csv')
# Xi_15D_15K_sample2()





def Duke_R_4_FMBA_15D_15K():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data_old(1580)
    data['trans'] = rcf.read_trans_data_old(1581)


    data['voltages'][200] = rcf.read_trans_data(1582) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1583) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1584) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1585) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1586) # voltage_file
    
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

    plt.title('R-4-FMBA 1.5D @ 15K Electroabsorption Spectra')
    plt.show()
    # Export_data(data, 'Duke\\Duke_R_4_FMBA_15D_2_18_15K_smoothed_with_absorption.csv', smooth=True)
# Duke_R_4_FMBA_15D_15K()

plt.show()