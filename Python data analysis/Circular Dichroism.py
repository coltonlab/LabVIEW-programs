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




def CD_template(): # Needs to be updated
    data = rcf.read_lockin_fluke_data(784)

    fig1, ax1 = plt.subplots()
    CD_data = pcg.plot_CD(data, ax=ax1, energy=False, Phased=False)

    # legend name
    legend = 'Absorption'

    # plt.show()
    return CD_data

# fluke = CD_template()





def CD_carter():
    data = {}

    fig, ax = plt.subplots()
    data['DC'] = rcf.read_trans_data(1383)
    data['AC'] = rcf.read_trans_data(1384)
    
    CD_data1 = pcg.plot_CD_Carter(data, ax=ax, energy=False, smoothed=False, color='green')


    data['DC'] = rcf.read_trans_data(1387)
    data['AC'] = rcf.read_trans_data(1385)
    
    CD_data1 = pcg.plot_CD_Carter(data, ax=ax, energy=False, smoothed=False)

    data['AC'] = rcf.read_trans_data(1386)
    
    CD_data2 = pcg.plot_CD_Carter(data, ax=ax, energy=False, smoothed=False)

    CD_data = (CD_data1+CD_data2)/2
    # data['DC'] = rcf.read_trans_data(985)
    # data['AC'] = rcf.read_trans_data(986)

    # x,Cd2 = pcg.plot_CD_Carter(data, ax=ax, energy=False, smoothed=True)

    # CD_diff=Cd2-Cd1

    plt.plot([280,620],[0,0],'k-')
    plt.plot(data['DC']['Digikrom Spectr.:0 (?)'],CD_data,'r-')
    plt.xlim(290,610)
        

    # data['AC offset'] = rcf.read_trans_data(986)

    # pcg.plot_CD_Carter(data, ax=ax, energy=False, smoothed=False)
    plt.show()


CD_carter()

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
