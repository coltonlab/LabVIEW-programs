import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import public.colton_math_functions as cmf
import matplotlib.pyplot as plt
import numpy as np



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
    


    # Calculate the absorption signal
    ABS_data = cmf.absorption(data['Keithley (V)'], data2['Keithley (V)'])    
     
    # legend name 
    legend = 'Absorption'    

    ax.plot(data['Digikrom Spectr.:0 (?)'],ABS_data, label=legend)
    # ax.legend()
    ax.set_xlabel('Wavelength')
    ax.set_ylabel('Absorption (OD)')

    plt.show()