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

def plot_data(data, title, flip = False, reflection=False, smooth=False, Eg=0, Ex=0):
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
        ax1.set_ylabel('Electroabsorption (mOD)')
        pcg.plot_EA_series(data, ax=ax1, color_map_name='plasma_r', smooth=smooth, energy=True, phased=True, flip=flip)
        pcg.plot_absorption(data, ax=ax2, color=right_color, smooth=smooth, energy=True,legend='Abs')

    

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

def plot_data_trans_refl_abs(dataT, dataR, title, Eg=0, Ex=0):
    
    # plots the EA or ER
    fig, axes = plt.subplots(nrows=2,ncols=2)
    ((ax1, ax2), (ax3, ax4)) = axes

    for ax in [ax1, ax2, ax3]:
        # plotting the eg and Ex lines
        ax.axvline(x=Eg, color='blue', linestyle='-.', linewidth=0.5, label="Eg = {:.3f} eV".format(Eg)) if Eg else False
        ax.axvline(x=Ex,color='red', linestyle='-.', linewidth=0.5, label="Exciton = {:.3f} eV".format(Ex)) if Ex else False

    ax1.legend()
        
    pcg.plot_ref_trans_abs(dataT, dataR, axes, smooth = True, energy=True)
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

######################################################################################################################################################################################
def BAPBr_2022_09_29():
    # Dictionary that holds all of the data with input voltages
    data830 = {}
    data810 = {}

    data830['voltages'] = {}
    data810['voltages'] = {}

    # read in the transmission data
    data830['blank'], data810['blank'] = rcf.read_2lockin(612)
    data830['trans'], data810['trans'] = rcf.read_2lockin(613)

    data810['trans'] = compress(data810['trans'],start=35, end=-10)
    data810['blank'] = compress(data810['blank'],start=35, end=-10)
    data830['trans'] = compress(data830['trans'],start=35, end=-10)
    data830['blank'] = compress(data830['blank'],start=35, end=-10)

    # Generate values for both sequences
    voltages = range(125, 601, 25)  # 100 to 600 in steps of 25
    excel_rows = range(592, 612, 1)  # 591 to 611 in steps of 1
      
    # Read in the voltages
    for voltage, row in zip(voltages, excel_rows):
        data830['voltages'][voltage], data810['voltages'][voltage] = rcf.read_2lockin(row)

    # plot_data(data830, title='ER data')
    # plot_data(data810, title='EA data')
    plot_data_trans_refl_abs(data810, data830, title='BAPBr-2022-09-29 analysis', Eg=3.392, Ex=3.392-352/1000)
    # plt.show()

    # Export_data(data, 'Duke\\Duke_R_4_FMBA_15D_2_18_15K_smoothed_with_absorption.csv', smooth=True) Need to come up with a better way of doing this

def MAPBr_2022_10_06():
    # Dictionary that holds all of the data with input voltages
    data830 = {}
    data810 = {}

    data830['voltages'] = {}
    data810['voltages'] = {}

    # read in the transmission data
    data830['blank'], data810['blank'] = rcf.read_2lockin(638)
    data830['trans'], data810['trans'] = rcf.read_2lockin(653)

    # data810['trans'] = compress(data810['trans'],start=35, end=-10)
    # data810['blank'] = compress(data810['blank'],start=35, end=-10)
    # data830['trans'] = compress(data830['trans'],start=35, end=-10)
    # data830['blank'] = compress(data830['blank'],start=35, end=-10)

    # Generate values for both sequences
    voltages =   range(100, 425+1, 25)  # 100 to 600 in steps of 25
    excel_rows = range(639, 652+1, 1)  # 591 to 611 in steps of 1
      
    # Read in the voltages
    for voltage, row in zip(voltages, excel_rows):
        data830['voltages'][voltage], data810['voltages'][voltage] = rcf.read_2lockin(row)

    # plot_data(data830, title='ER data')
    # plot_data(data810, title='EA data')
    plot_data_trans_refl_abs(data810, data830, title='MAPBr 2022-10-06 analysis', Eg=2.317, Ex=2.317-28/1000)
    # plt.show()

# def MAPBr_2022_10_06():
#     # Dictionary that holds all of the data with input voltages
#     data830 = {}
#     data810 = {}
    
#     data830['voltages'] = {}
#     data810['voltages'] = {}

#     # read in the transmission data
#     data830['blank'], data810['blank'] = rcf.read_2lockin(638)
#     data830['trans'], data810['trans'] = rcf.read_2lockin(653)

#     # Generate values for both sequences
#     voltages =   range(100, 425+1, 25)  # 100 to 600 in steps of 25
#     excel_rows = range(639, 652+1, 1)  # 591 to 611 in steps of 1
      
#     # Read in the voltages
#     for voltage, row in zip(voltages, excel_rows):
#         data830['voltages'][voltage], data810['voltages'][voltage] = rcf.read_2lockin(row)

#     # plot_data(data830, title='ER or EA data')
#     # plot_data(data810, title='EA or ER data')
#     plot_data_trans_refl_abs(data810, data830, title='MAPBr 2022-10-06 analysis', Eg=2.317, Ex=28/1000)
#     # plt.show()

def C5_2022_09_08():
    # Dictionary that holds all of the data with input voltages
    data830 = {}
    data810 = {}
    data830['voltages'] = {}
    data810['voltages'] = {}

    # read in the transmission data
    data830['blank'], data810['blank'] = rcf.read_2lockin(576)
    data830['trans'], data810['trans'] = rcf.read_2lockin(577)

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

    plot_data(data830, title='C5 ER analysis', flip = False, reflection=True, Eg=2.845, Ex=2.845-272/1000, smooth=True)
    plot_data(data810, title='C5 EA analysis', flip = True, reflection=False, Eg=2.845, Ex=2.845-272/1000, smooth=False)
    # plot_derivatives(data810, data830, title='C5 analysis', Eg=2.845, Ex=2.845-272/1000)
    plot_data_trans_refl_abs(data810, data830, title='C5 analysis', Eg=2.845, Ex=2.845-272/1000)
    # plot_fit(data810, data830, title='C5 analysis', Eg=2.845, Ex=2.845-272/1000)
    plt.show()

def C10_2022_05_03():
    # Dictionary that holds all of the data with input voltages
    data830 = {}
    data810 = {}
    data830['voltages'] = {}
    data810['voltages'] = {}

    # read in the transmission data
    data830['blank'], data810['blank'] = rcf.read_2lockin(202)
    data830['trans'], data810['trans'] = rcf.read_2lockin(201)

    # Generate values for both sequences
    voltages =   range(300, 700+1, 100)  # 100 to 600 in steps of 25
    excel_rows = range(196, 200+1, 1)  # 591 to 611 in steps of 1
      
    # Read in the voltages
    for voltage, row in zip(voltages, excel_rows):
        data830['voltages'][voltage], data810['voltages'][voltage] = rcf.read_2lockin(row)

    start, end = 20, -10
    data830['trans'], data810['trans'] = compress(data830['trans'],start=start, end=end), compress(data810['trans'],start=start, end=end)
    data830['blank'], data810['blank'] = compress(data830['blank'],start=start, end=end), compress(data810['blank'],start=start, end=end)
    data830['voltages'][300], data810['voltages'][300] = compress(data830['voltages'][300],start=start, end=end), compress(data810['voltages'][300],start=start, end=end)

    # plot_data(data830, title='C10 ER analysis', flip = False, reflection=True, Eg=2.878, Ex=298/1000)
    # plot_data(data810, title='C10 EA analysis', flip = False, reflection=False, Eg=2.878, Ex=298/1000)
    plot_data_trans_refl_abs(data810, data830, title='C10 analysis', Eg=2.878, Ex=2.878-298/1000)
    # plot_raw_data(data830, title='C10 raw ER Data')
    # plt.show()

def C12_2022_09_02():
    # Dictionary that holds all of the data with input voltages
    data830 = {}
    data810 = {}
    data830['voltages'] = {}
    data810['voltages'] = {}

    # read in the transmission data
    data830['blank'], data810['blank'] = rcf.read_2lockin(552)
    data830['trans'], data810['trans'] = rcf.read_2lockin(553) # First trans was 554 and needed slicing

    # Generate values for both sequences
    voltages =   range(300, 600+1, 50)  # 100 to 600 in steps of 25
    excel_rows = range(545, 551+1, 1)  # 591 to 611 in steps of 1
      
    # Read in the voltages
    for voltage, row in zip(voltages, excel_rows):
        data830['voltages'][voltage], data810['voltages'][voltage] = rcf.read_2lockin(row)

    start, end = 50, -80
    # data830['trans'], data810['trans'] = compress(data830['trans'],start=start, end=end), compress(data810['trans'],start=start, end=end)
    data830['blank'], data810['blank'] = compress(data830['blank'],start=start, end=end), compress(data810['blank'],start=start, end=end)
    data830['voltages'][300], data810['voltages'][300] = compress(data830['voltages'][300],start=start, end=end), compress(data810['voltages'][300],start=start, end=end)

    # plot_data(data830, title='C12 ER analysis', flip = True, reflection=True, smooth=False, Eg=2.869, Ex=292/1000)
    # plot_data(data810, title='C12 EA analysis', flip = True, reflection=False, smooth=False, Eg=2.869, Ex=292/1000)
    # plot_raw_data(data830, title='C12 raw ER Data')
    plot_data_trans_refl_abs(data810, data830, title='C12 analysis', Eg=2.869, Ex=2.869-292/1000)
    # plt.show()

def C16_2022_09_03():
    # Dictionary that holds all of the data with input voltages
    data830 = {}
    data810 = {}
    data830['voltages'] = {}
    data810['voltages'] = {}

    # read in the transmission data
    data830['blank'], data810['blank'] = rcf.read_2lockin(563)
    data830['trans'], data810['trans'] = rcf.read_2lockin(564)

    # Generate values for both sequences
    voltages =   range(300, 600+1, 50)  # 100 to 600 in steps of 25
    excel_rows = range(556, 562+1, 1)  # 591 to 611 in steps of 1
      
    # Read in the voltages
    for voltage, row in zip(voltages, excel_rows):
        data830['voltages'][voltage], data810['voltages'][voltage] = rcf.read_2lockin(row)

    start, end = 50, -35
    data830['trans'], data810['trans'] = compress(data830['trans'],start=start, end=end), compress(data810['trans'],start=start, end=end)
    data830['blank'], data810['blank'] = compress(data830['blank'],start=start, end=end), compress(data810['blank'],start=start, end=end)
    data830['voltages'][300], data810['voltages'][300] = compress(data830['voltages'][300],start=start, end=end), compress(data810['voltages'][300],start=start, end=end)

    # plot_data(data830, title='C16 ER analysis', flip = False, reflection=True, smooth=False, Eg=2.877, Ex=300/1000)
    # plot_data(data810, title='C16 EA analysis', flip = False, reflection=False, smooth=False, Eg=2.877, Ex=300/1000)
    # plot_raw_data(data830, title='C16 raw ER Data')
    plot_data_trans_refl_abs(data810, data830, title='C16 analysis', Eg=2.877, Ex=2.877-300/1000)
    plt.show()

def main():
    # Completed
    C5_2022_09_08()

    # # Bad
    # C10_2022_05_03() # This has terrible ER data, included raw EA data plot
    # C12_2022_09_02() # Hardly a signal in ER and some data is neds to be flipped

    # # need to plot
    # BAPBr_2022_09_29() # This just has some a gap between the lower and higher voltages (Maybe a change in phase or lamp spectrum)
    # MAPBr_2022_10_06()


    # # In progress
    # C16_2022_09_03()
main()
