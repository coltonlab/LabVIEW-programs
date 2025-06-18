import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import public.colton_math_functions as cmf
import matplotlib.pyplot as plt
import numpy as np


def CD_template_new():
    data = {}

    trans_files = range(1271,1278) # insert row number in excel
    blank_files =range(1278,1285) # insert row number in excel
    
    fig, ax = plt.subplots()
    for i in range(len(trans_files)):
        data['trans'] = rcf.read_trans_data(trans_files)
        data['blank'] = rcf.read_trans_data(blank_files)

        # plot data
        pcg.plot_absorption(data, ax=ax, smooth=False, color=name_color[i])
        ax.legend(trans_files)

    return
# 

def CD_template(): # Needs to be updated
    data = rcf.read_lockin_fluke_data(784)

    fig1, ax1 = plt.subplots()
    CD_data = pcg.plot_CD(data, ax=ax1, energy=False, Phased=False)

    # legend name
    legend = 'Absorption'

    # plt.show()
    return CD_data

# fluke = CD_template()





def CD_s_1_1():
    data = {}

    fig, ax = plt.subplots()
    data['DC'] = rcf.read_trans_data_old(1764) # S

    data['1'] = rcf.read_trans_data_old(1760) # S
    data['2'] = rcf.read_trans_data_old(1762) # S
    corrected_df = (data['1'] + data['2'])/2
    corrected_df['Digikrom Spectr.:0 (?)'] = data['1']['Digikrom Spectr.:0 (?)']
    data['AC'] = corrected_df
    
    CD_data1 = pcg.plot_CD_Carter(data, ax=ax, energy=False, smoothed=False)

    plt.title('Rough CD of S-1-1-NPB')
# CD_s_1_1()


def CD_r_1_1():
    data = {}

    fig, ax = plt.subplots()

    data['DC'] = rcf.read_trans_data_old(1765) # R
    data['1'] = rcf.read_trans_data_old(1761) # R
    data['2'] = rcf.read_trans_data_old(1763) # R
    corrected_df = (data['1'] + data['2'])/2
    corrected_df['Digikrom Spectr.:0 (?)'] = data['1']['Digikrom Spectr.:0 (?)']

    data['AC'] = corrected_df
    

    CD_data1 = pcg.plot_CD_Carter(data, ax=ax, energy=False, smoothed=False)

    plt.title('Rough CD of R-1-1-NPB')
# CD_r_1_1()



def CD_RMBA_Temp():
    data = {}

    trans_files = range(1271,1275) # insert row number in excel
    blank_files =range(1278,1282) # insert row number in excel

    name_color = ['red','blue','green','purple','orange','cyan','black']
    
    fig, ax = plt.subplots()
    for i in range(len(trans_files)):
        data['AC'] = rcf.read_trans_data(trans_files[i])
        data['DC'] = rcf.read_trans_data(blank_files[i])

        # plot data
        pcg.plot_CD_Carter(data, ax=ax, smooth=False, color=name_color[i])
        ax.legend(trans_files)

    plt.show()

# CD_RMBA_Temp()



# plt.show()


def R_1_1_NPB_S1_300K():
    # Dictionary that holds all of the data with input voltages
    data = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data_old(1766)
    data['trans'] = rcf.read_trans_data_old(1765)


    data['DC'] = rcf.read_trans_data_old(1765) # R

    # Flip windows
    data['1'] = rcf.read_trans_data_old(1761) # R
    data['2'] = rcf.read_trans_data_old(1763) # R
    corrected_df = (data['1'] + data['2'])/2
    corrected_df['Digikrom Spectr.:0 (?)'] = data['1']['Digikrom Spectr.:0 (?)']

    data['AC'] = corrected_df
    
    # plots the EA
    fig, ax1 = plt.subplots()
    CD_data1 = pcg.plot_CD_Carter(data, ax=ax1, energy=False, smoothed=False)


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

    ax1.set_title('R-1-1 NPB')
# R_1_1_NPB_S1_300K()


def S_1_1_NPB_S1_300K():
    # Dictionary that holds all of the data with input voltages
    data = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data_old(1766)
    data['trans'] = rcf.read_trans_average_data(1872)

    data['DC'] =  data['trans']

    data['AC'] = rcf.read_trans_average_data(1871)

    
    # plots the EA
    fig, ax1 = plt.subplots()
    CD_data1 = pcg.plot_CD_Carter(data, ax=ax1, energy=False, smoothed=False)


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

    ax1.set_title('S-1-1 NPB')
S_1_1_NPB_S1_300K()


def S_1_1_NPB_300K_No_Windows():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data_blank = {}
    # trans and blank will have strings as their voltage value, but each voltage will be an integer

    data['DC'] = rcf.read_trans_data(1769) # S
    data['AC'] = rcf.read_trans_data(1770)

    
    data_blank['DC'] = rcf.read_trans_data(1767) # S
    data_blank['AC'] = rcf.read_trans_data(1768)

    
    # plots the EA
    fig, ax1 = plt.subplots()
    CD = pcg.plot_CD_Carter(data, ax=ax1, energy=False, smoothed=False)
    CD_Blank = pcg.plot_CD_Carter(data_blank, ax=ax1, energy=False, smoothed=False)



    data['blank'] = data_blank['DC']
    data['trans'] = data['DC']

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

    ax1.set_title('S-1-1 NPB')
# S_1_1_NPB_300K_No_Windows()


def S_1_1_NPB_300K_No_Windows_2():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data_blank = {}
    fig, ax1 = plt.subplots()
    # trans and blank will have strings as their voltage value, but each voltage will be an integer

    data['DC'] = rcf.read_trans_data(1769) # S
    data['AC'] = rcf.read_trans_data(1770)

    
    data_blank['DC'] = rcf.read_trans_data(1767) # S
    data_blank['AC'] = rcf.read_trans_data(1768)

    # Wavelength is pulled from DC
    # data['AC'] = data['AC'] - data_blank['AC']
    # data['AC'] = data['AC'] - (data_blank['AC'] * data['DC']/data_blank['DC']*5/8)
    
    
    CD = pcg.plot_CD_Carter(data, ax=ax1, energy=False, smoothed=False, color='blue')
    CD_Blank = pcg.plot_CD_Carter(data_blank, ax=ax1, energy=False, smoothed=False, color='red')

    # data['AC'] = data['AC'] - data_blank['AC']
    data['AC'] = data['AC'] - (data_blank['AC'] * data['DC']/data_blank['DC']*5/8)
    CD = pcg.plot_CD_Carter(data, ax=ax1, energy=False, smoothed=False, color='black')

    data['blank'] = data_blank['DC']
    data['trans'] = data['DC']/(5/8)

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

    ax1.set_title('S-1-1 NPB No Windows')
# S_1_1_NPB_300K_No_Windows_2()

def S_1_1_NPB_300K_Windows():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data_blank = {}
    fig, ax1 = plt.subplots()
    # trans and blank will have strings as their voltage value, but each voltage will be an integer

    data['DC'] = rcf.read_trans_data(1778) # S
    data['AC'] = rcf.read_trans_data(1779)

    
    data_blank['DC'] = rcf.read_trans_data(1776) # S
    data_blank['AC'] = rcf.read_trans_data(1777)

    # Wavelength is pulled from DC
    # data['AC'] = data['AC'] - data_blank['AC']
    # data['AC'] = data['AC'] - (data_blank['AC'] * data['DC']/data_blank['DC']*5/8)
    
    
    CD = pcg.plot_CD_Carter(data, ax=ax1, energy=False, smoothed=False, color='blue')
    CD_Blank = pcg.plot_CD_Carter(data_blank, ax=ax1, energy=False, smoothed=False, color='red')

    # data['AC'] = data['AC'] - data_blank['AC']
    data['AC'] = data['AC'] - (data_blank['AC'] * data['DC']/data_blank['DC']*5/8)
    CD = pcg.plot_CD_Carter(data, ax=ax1, energy=False, smoothed=False, color='black')

    data['AC'] = data['AC'] - data_blank['AC']
    CD = pcg.plot_CD_Carter(data, ax=ax1, energy=False, smoothed=False, color='green')

    data['blank'] = data_blank['DC']
    data['trans'] = data['DC']/(5/8)

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

    ax1.set_title('S-1-1 NPB Windows')
    ax1.set_ybound(lower=-1000)
# S_1_1_NPB_300K_Windows()

def S_1_1_NPB_Inhibit():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data_blank = {}
    fig, ax1 = plt.subplots()
    # trans and blank will have strings as their voltage value, but each voltage will be an integer

    data['DC'] = rcf.read_trans_data(1778) # S
    data['AC'] = rcf.read_trans_data(1779)

    
    data_blank['DC'] = rcf.read_trans_data(1778) # S
    data_blank['AC'] = rcf.read_trans_data(1780)

    # Wavelength is pulled from DC
    # data['AC'] = data['AC'] - data_blank['AC']
    # data['AC'] = data['AC'] - (data_blank['AC'] * data['DC']/data_blank['DC']*5/8)
    
    
    CD = pcg.plot_CD_Carter(data, ax=ax1, energy=False, smoothed=False, color='blue')
    CD_Blank = pcg.plot_CD_Carter(data_blank, ax=ax1, energy=False, smoothed=False, color='red')

    data_blank['DC'] = rcf.read_trans_data(1776) # S
    # # data['AC'] = data['AC'] - data_blank['AC']
    # data['AC'] = data['AC'] - (data_blank['AC'] * data['DC']/data_blank['DC']*5/8)
    # CD = pcg.plot_CD_Carter(data, ax=ax1, energy=False, smoothed=False, color='black')
    data['AC']['X (V) Phased'] = cmf.savitzky_golay_smoothing(data['AC']['X (V) Phased']) - cmf.savitzky_golay_smoothing(data_blank['AC']['X (V) Phased'])
    # data['AC']['X (V) Phased'] = data['AC']['X (V) Phased'] - data_blank['AC']['X (V) Phased']
    CD = pcg.plot_CD_Carter(data, ax=ax1, energy=False, smoothed=False, color='green')

    data['blank'] = data_blank['DC']
    data['trans'] = data['DC']/(5/8)

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

    ax1.set_title('S-1-1 NPB Windows')
    ax1.set_ybound(lower=-1000)
# S_1_1_NPB_Inhibit()

def Air_Inhibit():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data_blank = {}
    fig, ax1 = plt.subplots()
    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    value = 6
    data['DC'] = rcf.read_trans_data(1815) # S
    data['AC'] = rcf.read_trans_data(1814 + value)

    
    data_blank['DC'] = rcf.read_trans_data(1815) # S
    data_blank['AC'] = rcf.read_trans_data(1813 + value)

    # Wavelength is pulled from DC
    # data['AC'] = data['AC'] - data_blank['AC']
    # data['AC'] = data['AC'] - (data_blank['AC'] * data['DC']/data_blank['DC']*5/8)
    
    
    CD = pcg.plot_CD_Carter(data, ax=ax1, energy=False, smoothed=False, color='blue')
    CD_Blank = pcg.plot_CD_Carter(data_blank, ax=ax1, energy=False, smoothed=False, color='red')

    data['AC'] = data['AC'] - data_blank['AC']
    CD = pcg.plot_CD_Carter(data, ax=ax1, energy=False, smoothed=False, color='green')
    plt.title('0 degree')
# Air_Inhibit()


def History():
    # Dictionary that holds all of the data with input voltages
    data = {}
    data_blank = {}
    fig, ax1 = plt.subplots()
    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    value = 6
    data['DC'] = rcf.read_trans_data(1860) # S
    data['AC'] = rcf.read_trans_data(1859)

    
    data_blank['DC'] = rcf.read_trans_data(1861) # S
    data_blank['AC'] = rcf.read_trans_data(1858)

    # Wavelength is pulled from DC
    # data['AC'] = data['AC'] - data_blank['AC']
    # data['AC'] = data['AC'] - (data_blank['AC'] * data['DC']/data_blank['DC']*5/8)
    
    
    CD = pcg.plot_CD_Carter(data, ax=ax1, energy=False, smoothed=True, color='blue')
    CD_Blank = pcg.plot_CD_Carter(data_blank, ax=ax1, energy=False, smoothed=True, color='red')

    # data['AC'] = data['AC'] - data_blank['AC']
    # CD = pcg.plot_CD_Carter(data, ax=ax1, energy=False, smoothed=False, color='green')
    plt.title('Vit. B12 and Background Offset (Low light)')
# History()






plt.show()