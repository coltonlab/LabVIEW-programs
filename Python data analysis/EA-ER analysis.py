import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame

def Export_data(data, filename, smooth=False): # Need to edit this

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

def export_dielectric(dataT, dataR, title, smooth=False):
    import public.colton_math_functions as cmf

    calculations = {}
    calculations['wavenumber (1/cm)'] = 1/(dataT['blank']['Digikrom Spectr.:0 (?)'].values*1e-7) # This is 1/cm 

    # transmittance
    if smooth:
        calculations['trans'] = cmf.transmition_smooth(dataT['trans']['R (V)'], dataT['blank']['I (V)'])    
        calculations['reflect'] = cmf.reflection_smooth(dataR['trans']['R (V)'], dataR['blank']['R (V)'] ,dataR['blank']['I (V)'])
    else:
        calculations['trans'] = cmf.transmition(dataT['trans']['R (V)'], dataT['blank']['I (V)'])
        calculations['reflect'] = cmf.reflection(dataR['trans']['R (V)'], dataR['blank']['R (V)'] ,dataR['blank']['I (V)'])

    df = DataFrame(calculations)

    # Export to CSV
    df[['wavenumber (1/cm)','trans']].to_csv(f"C:\\Users\\carterms\\OneDrive - Brigham Young University\\Desktop\\ER Analysis\\dielectric\\{title} - Trans.dat", index=False, header=False, sep='\t') 
    df[['wavenumber (1/cm)','reflect']].to_csv(f"C:\\Users\\carterms\\OneDrive - Brigham Young University\\Desktop\\ER Analysis\\dielectric\\{title} - reflect.dat", index=False, header=False, sep='\t')     

def compress(dataAll, start=0, end=None):
    data = dataAll.copy()
    data_keys = list(data.keys())
    for key in data_keys:
        data[key] = data[key].iloc[start: end]
    return data

def plot_data(data, title, flip = False, reflection=False, smooth=False, Eg=0, Ex=0, energy=True, phased=True):
    # plots the EA or ER
    fig, ax1 = plt.subplots()
    
    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'

    # Absorption or reflection 
    if reflection: 
        ax1.set_ylabel('Electroreflection (x1000)')
        pcg.plot_ER_series(data, ax=ax1, color_map_name='plasma_r', smooth=smooth, energy=energy, phased=phased, flip=flip, colorbar=False)
        pcg.plot_reflection(data, ax=ax2, color=right_color, smooth=smooth, energy=energy,legend='Abs')
    else:   
        ax1.set_ylabel('Electroabsorption (mOD)')
        pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=smooth, energy=energy, phased=phased, flip=flip)
        pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=smooth, energy=energy,legend='Abs')

    

    # plotting the eg and Ex lines
    ax2.axvline(x=Eg, color='blue', linestyle='-.', linewidth=0.5, label="Eg = {:.3f} eV".format(Eg)) if Eg else False
    ax2.axvline(x=Ex,color='red', linestyle='-.', linewidth=0.5, label="Exciton = {:.3f} eV".format(Ex)) if Ex else False


    # plot parameters
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)
    ax2.legend()
    plt.title(title)


def plot_data_transmittance(data, title, flip = False, reflection=False, smooth=False, Eg=0, Ex=0):
    # plots the EA or ER
    fig, ax1 = plt.subplots()
    
    # Plots the Absorption
    ax2 = ax1.twinx()
    right_color = 'green'

    # Absorption or reflection 
    if reflection: 
        ax1.set_ylabel('Electroreflection (x1000)')
        pcg.plot_ER_series(data, ax=ax1, color_map_name='plasma_r', smooth=smooth, energy=True, phased=True, flip=flip, colorbar=False)
        pcg.plot_reflection(data, ax=ax2, color=right_color, smooth=smooth, energy=True,legend='Abs')
    else:   
        pcg.plot_ER_series(data, ax=ax1, color_map_name='plasma_r', smooth=smooth, energy=True, phased=True, flip=flip)
        ax1.set_ylabel('Electrotransmittance (mOD)')
        pcg.plot_reflection(data, ax=ax2, color=right_color, smooth=smooth, energy=True,legend='Abs')
        ax2.set_ylabel('transmittance',fontsize = 14, color=right_color)

    

    # plotting the eg and Ex lines
    ax2.axvline(x=Eg, color='blue', linestyle='-.', linewidth=0.5, label="Eg = {:.3f} eV".format(Eg)) if Eg else False
    ax2.axvline(x=Ex,color='red', linestyle='-.', linewidth=0.5, label="Exciton = {:.3f} eV".format(Ex)) if Ex else False


    # plot parameters
    ax2.spines['right'].set_color(right_color)
    ax2.yaxis.set_tick_params(color=right_color)
    for label in ax2.get_yticklabels():
        label.set_color(right_color)
    ax2.legend()
    plt.title(title)

def plot_data_trans_refl_abs(dataT, dataR, title, Eg=0, Ex=0, smooth=False):
    
    # plots the EA or ER
    fig, axes = plt.subplots(nrows=2,ncols=2)
    ((ax1, ax2), (ax3, ax4)) = axes

    for ax in [ax1, ax2, ax3]:
        # plotting the eg and Ex lines
        ax.axvline(x=Eg, color='blue', linestyle='-.', linewidth=0.5, label="Eg = {:.3f} eV".format(Eg)) if Eg else False
        ax.axvline(x=Ex,color='red', linestyle='-.', linewidth=0.5, label="Exciton = {:.3f} eV".format(Ex)) if Ex else False
    # ax1.legend()
        
    pcg.plot_ref_trans_abs(dataT, dataR, axes, smooth = smooth, energy=True)
    # export_dielectric(dataT, dataR, title, smooth=True)
    fig.suptitle(title)

def plot_derivatives(dataT, dataR, title, Eg=0, Ex=0):
    # plots the EA or ER
    fig, axes = plt.subplots(nrows=2,ncols=2)
    ((ax1, ax2), (ax3, ax4)) = axes

    for ax in [ax1, ax2, ax3, ax4]:
        # plotting the eg and Ex lines
        ax.axvline(x=Eg, color='blue', linestyle='-.', linewidth=0.5, label="Eg = {:.3f} eV".format(Eg)) if Eg else False
        ax.axvline(x=Ex,color='red', linestyle='-.', linewidth=0.5, label="Exciton = {:.3f} eV".format(Ex)) if Ex else False

    # ax1.legend()
        
    pcg.plot_individual_derivatives(dataT, dataR, axes, energy=True)
    fig.suptitle(title)


def plot_fit(dataT, dataR, title, Eg=0, Ex=0):
    # plots the EA or ER
    fig, ax = plt.subplots()
    fig2, ax2 = plt.subplots()


    ax.axvline(x=Eg, color='blue', linestyle='-.', linewidth=0.5, label="Eg = {:.3f} eV".format(Eg)) if Eg else False
    ax.axvline(x=Ex,color='red', linestyle='-.', linewidth=0.5, label="Exciton = {:.3f} eV".format(Ex)) if Ex else False

    # ax1.legend()
        
    pcg.plot_exciton_fit(dataT, ax, voltage=600, Ex=Ex, smooth = False, color='red')
    # pcg.plot_exciton_fit(dataR, ax2, voltage=600, Ex=Ex, smooth = False, color='red')
    # pcg.plot_EA_amplitude(dataT, ax=ax, color_map_name='plasma_r', smooth=True, energy=True, phased=True, flip=False)
    # fig.suptitle(title)



def plot_raw_data(data, title):
    # plots the EA or ER
    fig, ax = plt.subplots()
    voltages = np.array(list(data['voltages'].keys()))

    for voltage in voltages:
        pcg.plot_data(data['voltages'][voltage],ax=ax, energy=False, smooth=False)
    plt.title(title)

def ER_and_EA_template():
    # Dictionary that holds all of the data with input voltages
    data830 = {}
    data810 = {}

    data830['voltages'] = {}
    data810['voltages'] = {}

    # read in the transmission data
    data830['blank'], data810['blank'] = rcf.read_2lockin(612)
    data830['trans'], data810['trans'] = rcf.read_2lockin(613)

    # data810['trans'] = compress(data810['trans'],start=35, end=-10)
    # data810['blank'] = compress(data810['blank'],start=35, end=-10)
    # data830['trans'] = compress(data830['trans'],start=35, end=-10)
    # data830['blank'] = compress(data830['blank'],start=35, end=-10)

    # Generate values for both sequences
    voltages = range(125, 601, 25)  # 100 to 600 in steps of 25
    excel_rows = range(592, 612, 1)  # 591 to 611 in steps of 1
      
    # Read in the voltages
    for voltage, row in zip(voltages, excel_rows):
        data830['voltages'][voltage], data810['voltages'][voltage] = rcf.read_2lockin(row)

    plot_data(data830, title='ER data')
    plot_data(data810, title='EA data')
    # plt.show()

    # Export_data(data, 'Duke\\Duke_R_4_FMBA_15D_2_18_15K_smoothed_with_absorption.csv', smooth=True) Need to come up with a better way of doing this


def plot_franz_keldysh(data, title, flip = False, reflection=False, smooth=False, Eg=0, Ex=0, energy=True, phased=True):
    # plots the EA or ER
    fig, ax1 = plt.subplots()




    # pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=smooth, energy=True, phased=True, flip=flip)
    # selected_x, refined_x, matched_y = pcg.plot_EA_amplitude(data, ax=ax1, color_map_name='plasma_r', smooth=smooth, energy=energy, phased=phased, flip=flip)
    data = pcg.plot_EA_amplitude_all(data, ax=ax1, color_map_name='plasma_r', smooth=smooth, energy=energy, phased=phased, flip=flip)
    



    fig2, ax2 = plt.subplots()
    # pcg.plot_peak_amplitude_all(data, ax=ax2, color_map_name='plasma_r', energy=energy)
    
    # pcg.plot_peak_amplitude(data, ax=ax2, color_map_name='plasma_r', refined_x=refined_x, matched_y=matched_y, energy=energy)



    # print(data['voltages'])

    # # plotting the eg and Ex lines
    ax1.axvline(x=Eg, color='blue', linestyle='-.', linewidth=0.5, label="Eg = {:.3f} eV".format(Eg)) if Eg else False
    ax1.axvline(x=Ex,color='red', linestyle='-.', linewidth=0.5, label="Exciton = {:.3f} eV".format(Ex)) if Ex else False

    # plt.title(title)



######################################################################################################################################################################################
def rac_1_1_NPB_16K():
    remote = False # Set to True if you want to run this on the remote computer
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1707, remote=remote) # blank_file
    data['trans'] = rcf.read_trans_data(1715, remote=remote)

    data['voltages'][100] = rcf.read_trans_data(1716, remote=remote) # voltage_file
    data['voltages'][125] = rcf.read_trans_data(1717, remote=remote) # voltage_file
    data['voltages'][150] = rcf.read_trans_data(1718, remote=remote) # voltage_file
    data['voltages'][175] = rcf.read_trans_data(1728, remote=remote) # voltage_file        
    data['voltages'][200] = rcf.read_trans_data(1727, remote=remote) # voltage_file
    data['voltages'][225] = rcf.read_trans_data(1721, remote=remote) # voltage_file
    data['voltages'][250] = rcf.read_trans_data(1722, remote=remote) # voltage_file
    data['voltages'][275] = rcf.read_trans_data(1723, remote=remote) # voltage_file        
    data['voltages'][300] = rcf.read_trans_data(1724, remote=remote) # voltage_file
    data['voltages'][325] = rcf.read_trans_data(1725, remote=remote) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1726, remote=remote) # voltage_file        

    Eg = 3.4768
    Ex = 3.124 

    plot_data(data, title='rac-1-1 NPB 0.5nm', flip = True, reflection=False, Eg=Eg, Ex=Ex, smooth=False, energy=True, phased=True)
    plot_franz_keldysh(data, title='C5 EA analysis', flip = True, reflection=False, Eg=Eg, Ex=Ex, smooth=False, energy=True, phased=False)


    # plt.show()

def C5_2022_09_08():
    # Dictionary that holds all of the data with input voltages
    data830 = {}
    data810 = {}
    data830['voltages'] = {}
    data810['voltages'] = {}

    # read in the transmission data
    data830['blank'], data810['blank'] = rcf.read_2lockin(576, Old=True)
    data830['trans'], data810['trans'] = rcf.read_2lockin(577, Old=True)

    start, end = 50, -50
    data810['trans'] = compress(data810['trans'],start=start, end=end)
    data810['blank'] = compress(data810['blank'],start=start, end=end)
    data830['trans'] = compress(data830['trans'],start=start, end=end)
    data830['blank'] = compress(data830['blank'],start=start, end=end)

    # Generate values for both sequences
    voltages =   range(300, 600+1, 50)  # 100 to 600 in steps of 25
    excel_rows = range(569, 575+1, 1)  # 591 to 611 in steps of 1
      
    # Read in the voltages
    for voltage, row in zip(voltages, excel_rows):
        data830['voltages'][voltage], data810['voltages'][voltage] = rcf.read_2lockin(row)

    # plot_data(data830, title='C5 ER analysis', flip = False, reflection=True, Eg=2.845, Ex=2.845-272/1000, smooth=True)
    plot_data(data810, title='C5 EA analysis', flip = True, reflection=False, Eg=2.845, Ex=2.845-272/1000, smooth=False)
    plot_franz_keldysh(data810, title='C5 EA analysis', flip = True, reflection=False, Eg=2.845, Ex=2.845-272/1000, smooth=False, energy=True, phased=False)
    # plot_derivatives(data810, data830, title='C5 analysis', Eg=2.845, Ex=2.845-272/1000)
    # plot_data_trans_refl_abs(data810, data830, title='C5 analysis', Eg=2.845, Ex=2.845-272/1000)
    # plot_fit(data810, data830, title='C5 analysis', Eg=2.845, Ex=2.845-272/1000)
    plt.show()


def AMP_SnI4_Sample3_6_11_2025():
    # Dictionary that holds all of the data with input voltages
    data830 = {}
    data810 = {}
    data830['voltages'] = {}
    data810['voltages'] = {}

    # read in the transmission data
    data830['blank'], data810['blank'] = rcf.read_2lockin(1847, Old=False, switch=True)
    data830['trans'], data810['trans'] = rcf.read_2lockin(1845, Old=False, switch=True)

    # start, end = 50, -50
    # data810['trans'] = compress(data810['trans'],start=start, end=end)
    # data810['blank'] = compress(data810['blank'],start=start, end=end)
    # data830['trans'] = compress(data830['trans'],start=start, end=end)
    # data830['blank'] = compress(data830['blank'],start=start, end=end)

    # Generate values for both sequences
    voltages =   range(300, 600+1, 50)  # 100 to 600 in steps of 25
    excel_rows = range(569, 575+1, 1)  # 591 to 611 in steps of 1
      
    # Read in the voltages
    # for voltage, row in zip(voltages, excel_rows):
    #     data830['voltages'][voltage], data810['voltages'][voltage] = rcf.read_2lockin(row)

    # plot_data(data830, title='C5 ER analysis', flip = False, reflection=True, Eg=2.845, Ex=2.845-272/1000, smooth=True)
    # plot_data(data810, title='C5 EA analysis', flip = True, reflection=False, Eg=2.845, Ex=2.845-272/1000, smooth=False)
    # plot_franz_keldysh(data810, title='C5 EA analysis', flip = True, reflection=False, Eg=2.845, Ex=2.845-272/1000, smooth=False, energy=True, phased=False)
    # plot_derivatives(data810, data830, title='C5 analysis', Eg=2.845, Ex=2.845-272/1000)
    plot_data_trans_refl_abs(data810, data830, title='4-AMP SnI4 Front', Eg=0, Ex=0)
    # plot_fit(data810, data830, title='C5 analysis', Eg=2.845, Ex=2.845-272/1000)
    plt.show()


def AMP_SnI4_Thick_6_11_2025():
    # Dictionary that holds all of the data with input voltages
    data830 = {}
    data810 = {}
    data830['voltages'] = {}
    data810['voltages'] = {}

    # read in the transmission data
    data830['blank'], data810['blank'] = rcf.read_2lockin(1848, Old=False, switch=True)
    data830['trans'], data810['trans'] = rcf.read_2lockin(1849, Old=False, switch=True)

    # start, end = 50, -50
    # data810['trans'] = compress(data810['trans'],start=start, end=end)
    # data810['blank'] = compress(data810['blank'],start=start, end=end)
    # data830['trans'] = compress(data830['trans'],start=start, end=end)
    # data830['blank'] = compress(data830['blank'],start=start, end=end)

    # Generate values for both sequences
    voltages =   range(300, 600+1, 50)  # 100 to 600 in steps of 25
    excel_rows = range(569, 575+1, 1)  # 591 to 611 in steps of 1
      
    # Read in the voltages
    # for voltage, row in zip(voltages, excel_rows):
    #     data830['voltages'][voltage], data810['voltages'][voltage] = rcf.read_2lockin(row)

    # plot_data(data830, title='C5 ER analysis', flip = False, reflection=True, Eg=2.845, Ex=2.845-272/1000, smooth=True)
    # plot_data(data810, title='C5 EA analysis', flip = True, reflection=False, Eg=2.845, Ex=2.845-272/1000, smooth=False)
    # plot_franz_keldysh(data810, title='C5 EA analysis', flip = True, reflection=False, Eg=2.845, Ex=2.845-272/1000, smooth=False, energy=True, phased=False)
    # plot_derivatives(data810, data830, title='C5 analysis', Eg=2.845, Ex=2.845-272/1000)
    plot_data_trans_refl_abs(data810, data830, title='4-AMP SnI4 Back', Eg=0, Ex=0, smooth=False)
    # plot_fit(data810, data830, title='C5 analysis', Eg=2.845, Ex=2.845-272/1000)
    plt.show()


def rac_1_1_NPB_half_nm_16K():
    remote = True # Set to True if you want to run this on the remote computer
    # Dictionary that holds all of the data with input voltages
    data = {}
    data['voltages'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(1733, remote=remote) # blank_file
    data['trans'] = rcf.read_trans_data(1732, remote=remote)
  
    data['voltages'][300] = rcf.read_trans_data(1729, remote=remote) # voltage_file
    data['voltages'][325] = rcf.read_trans_data(1730, remote=remote) # voltage_file
    data['voltages'][350] = rcf.read_trans_data(1731, remote=remote) # voltage_file   

    Eg = 3.4768
    Ex = 3.124 

    plot_data(data, title='rac-1-1 NPB 0.5nm', flip = True, reflection=False, Eg=Eg, Ex=Ex, smooth=False, energy=True, phased=True)
    plot_franz_keldysh(data, title='C5 EA analysis 2', flip = True, reflection=False, Eg=Eg, Ex=Ex, smooth=False, energy=True, phased=False)


    # plt.show()



def main():
    # rac_1_1_NPB_16K()
    # AMP_SnI4_Sample3_6_11_2025()
    AMP_SnI4_Thick_6_11_2025()
    # rac_1_1_NPB_half_nm_16K()
    # C5_2022_09_08()
    plt.show()
main()
