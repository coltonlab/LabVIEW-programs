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


"""Kentucky Plots, Kevin (CHDA, CHDMA, 4-AMP, 4-AMPY)"""

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
# AMPY4_295K()

fig, ax1 = plt.subplots()
ax2=ax1.twinx()

# The shift between the two separate scans is not going away, and there isn't an easy way to correct it.
# The biggest issue is that the zero point does not fall at the same spot for both scans. So, 
# shifting by adding would be the ideal solution, but that does not work because it shifts everything, making the
# plot diverge at higher energies, even though the plot there should go to 0.
# I half-fixed the problem by actually shifting the 590-700nm data - keep in mind that there is still some PL
# in the lower part of that range, hence, that explains why the signals b4/after the short pass are different.
# I just shifted the first 40 points ie, up to 630nm, but that's more of a bandaid solution than anything else.
# Thus, I am sending that plot with the caveat that it may not be an accurate representation of the actual data, and
# then sending separate plots for each range as well.
def AMPY4_16K_400_600():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1292)
    data['trans'] = rcf.read_trans_data(1291)


    # data['voltages'] = rcf.read_voltage_series_data(80) # voltage_series_file
    data['voltages'][100] = rcf.read_trans_data(1282) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1283) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1284) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1285) # voltage_file
    # data['voltages'][401] = rcf.read_trans_data(1232) # voltage_file, isn't at 500V. It's the 400V with the short pass filter
    value = -1
    data['voltages'][100]['X (V)'] *= value
    data['voltages'][200]['X (V)'] *= value 
    data['voltages'][300]['X (V)'] *= value 
    data['voltages'][400]['X (V)'] *= value 
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
# AMPY4_16K_400_600()

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
def PESI4F():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(239)
    data['trans'] = rcf.read_trans_data(238)


    data['voltages'][100] = rcf.read_trans_data(1101) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(1102) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1103) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1104) # voltage_file
    data['voltages'][275] = rcf.read_trans_data(1105) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1106) # voltage_file
    
    # plots the EA
    fig, ax1 = plt.subplots()
    # ax1.set_ylim(0,0.15)
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma', smooth=True, energy=True, phased=False)
    ax1.set_ylabel('Electroabsorption (mOD)')

    # pcg.plot_EA_voltage(data=data, ax=ax1, voltage=500, smooth=True,color='red',energy=True,legend='Y6')

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
# EA2CF3PESI()



""" 4-F PESI Kentucky """
def PESI4F_new():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1269)
    data['trans'] = rcf.read_trans_data(1268)


    data['voltages'][100] = rcf.read_trans_data(1259) # voltage_file
    data['voltages'][200] = rcf.read_trans_data(1260) # voltage_file
    data['voltages'][300] = rcf.read_trans_data(1261) # voltage_file
    data['voltages'][400] = rcf.read_trans_data(1262) # voltage_file

    
    # plots the EA
    fig, ax1 = plt.subplots()
    # ax1.set_ylim(0,0.15)
    pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma', smooth=True, energy=True, phased=False)
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
    # plt.show()
# PESI4F_new()
