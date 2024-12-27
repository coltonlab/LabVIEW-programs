"""
Script Name: plot_colton_graphs
Author: Carter Shirley
Date: February 20, 2024
Description: This code takes in a dictionary with the data inside it and gives out a plot.  

"""

import public.read_colton_files as rcf
import public.colton_math_functions as cmf
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.colors import BoundaryNorm
import numpy as np


def plot_EA_series(data, ax, colorbar=True, smooth=False, color_map_name='autumn_r', linewidth = 1, energy=True, phased=True,text_size=14):
    # Get wavelength
    X = data['trans']['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)',fontsize=text_size)    

    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)',fontsize=text_size)

    # Getting the different voltage values
    voltages = np.array(list(data['voltages'].keys()))
    # Adds a color bar if true, otherwise defines colors for each plot item
    if colorbar == True:
        colors = color_bar(voltages, ax, color_map_name, temp=False, pad=0.10)
    else:
        color_map_func = getattr(plt.cm, color_map_name)
        colors = color_map_func(np.linspace(0, 1, len(voltages)))
    # # Create a custom colormap for the voltages 
    # color_map_func = getattr(plt.cm, color_map_name)
    # colors = color_map_func(np.linspace(0, 1, len(voltages))) # <------------ Change plt.cm.__color id__ to get a different color
    # colors = colors[::-1]
    # custom_cmap = ListedColormap(colors)

    # if colorbar == True:
    #     # Add a color bar next to the plot
    #     voltage_diff = abs(voltages[0]-voltages[1])/2
    #     cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=custom_cmap, 
    #         norm=plt.Normalize(vmin=np.min(voltages)-voltage_diff, vmax=np.max(voltages)+voltage_diff)), 
    #         ax=ax, pad=0.15, orientation='vertical')
    #     cbar.set_label('Voltage')
    #     cbar.set_ticks(voltages)       # Example tick positions
    #     cbar_labels  = ['{}V'.format(V) for V in voltages]
    #     cbar.set_ticklabels(cbar_labels)  # Corresponding labels


    if phased:
        for voltage in voltages:            
            data['voltages'][voltage]['X (V)'] = data['voltages'][voltage]['X (V) Phased']


    # Plot the data
    i = 0
    for voltage in voltages:
        # Calculate the EA signal
        if smooth:
            EA_data = cmf.EA_smooth(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])
            # EA_data = EA_data + 1e-4
        else:
            EA_data = cmf.EA(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])
        

        ax.plot(X,EA_data*1000, linewidth=linewidth, color=colors[i])
        i += 1

    ax.tick_params(axis='both',which='major', labelsize=12)
    ax.axhline(y=0,color='k',linewidth=0.8)
    ax.set_ylabel('Electroabsorption (mOD)',fontsize=text_size)
    # ax.set_ylabel('Electroreflection (mOD)',fontsize=text_size)



def plot_EA_temp_series(data, ax, colorbar=True, color_map_name='autumn_r', linewidth = 1, energy=True,smooth=False,text_size=14):
    # Get wavelength
    X = data['blank']['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)')    
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)',fontsize=text_size)

    # Create a color bar
    temperatures = np.array(list(data['voltages'].keys()))
    # colors = color_bar(temperatures, ax, color_map_name, temp=True)
    if colorbar == True:
        colors = color_bar(temperatures, ax, color_map_name, temp=True)
    else:
        color_map_func = getattr(plt.cm, color_map_name)
        colors = color_map_func(np.linspace(0, 1, len(temperatures)))

    # Plot the data
    i = 0
    for temp in temperatures:
        # Calculate the EA signal
        if smooth:
            EA_data = cmf.EA_smooth(data['voltages'][temp]['X (V) Phased'], data['trans'][temp]['R (V)'])
        else:
            EA_data = cmf.EA(data['voltages'][temp]['X (V) Phased'], data['trans'][temp]['R (V)'])
        
        ax.plot(X,EA_data*1000, linewidth=linewidth, color=colors[i])
        i += 1
    
    ax.tick_params(axis='both',which='major', labelsize=12)
    ax.axhline(y=0,color='k',linewidth=0.8)
    ax.set_ylabel('Electroabsorption (mOD)',fontsize=text_size)


def color_bar(temperatures, ax, color_map_name, temp=True, pad = 0):
    # Create a custom colormap for the voltages 
    color_map_func = getattr(plt.cm, color_map_name)
    colors = color_map_func(np.linspace(0, 1, len(temperatures))) # <------------ Change plt.cm.__color id__ to get a different color
    custom_cmap = ListedColormap(colors)

    # Number of temperature points
    num_temperatures = len(temperatures)
    # levels = np.copy(temperatures)
    # Create a normalizer that maps indices (0, 1, 2, ...) to the colormap
    norm = plt.Normalize(vmin=0, vmax=num_temperatures - 1)
    # norm = BoundaryNorm(levels,custom_cmap.N)

    # Create evenly spaced ticks for the colorbar
    ticks = np.linspace(0.5, num_temperatures - 1.5, num_temperatures)

    # Create the colorbar with equally spaced colors
    cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=custom_cmap, norm=norm), ax=ax, pad=pad, orientation='vertical')

    # Set the colorbar label
    if temp:
        cbar.set_label('Temperatures (K)')
        cbar_labels  = [f'{V}K' for V in temperatures]
    else:
        # cbar.set_label('Voltages (V)')
        cbar_labels  = [f'{V}V' for V in temperatures]

    # Set evenly spaced ticks but label them with the actual temperature values
    cbar.set_ticks(ticks)
    cbar.set_ticklabels(cbar_labels)  # Use actual temperatures for the tick labels


    return colors


def plot_ABS_temp_series(data, ax, colorbar=True, color_map_name='autumn_r', linewidth = 1, energy=True, smooth=False,text_size=14):
    # Get wavelength
    X1 = data['blank']['Digikrom Spectr.:0 (?)']
    # X2 = data['blank2']['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)',fontsize = text_size)    
    
    if energy:
        X1 = cmf.wavelength_to_energy(X1)
        # X2 = cmf.wavelength_to_energy(X2)
        ax.set_xlabel('Energy (eV)',fontsize = text_size)



    # Getting the different voltage values
    temperatures = np.array(list(data['trans'].keys()))
    # colors = color_bar(temperatures, ax, color_map_name, temp=True)
    if colorbar == True:
        colors = color_bar(temperatures, ax, color_map_name, temp=True)
    else:
        color_map_func = getattr(plt.cm, color_map_name)
        colors = color_map_func(np.linspace(0, 1, len(temperatures)))

    # Plot the data
    i = 0
    for temp in temperatures:

        # Calculate the EA signal
        if smooth:
            ABS_data1 = cmf.absorption_smooth(data['trans'][temp]['R (V)'], data['blank']['R (V)'])
        else:
            ABS_data1 = cmf.absorption(data['trans'][temp]['R (V)'], data['blank']['R (V)'])
        
        ax.plot(X1,ABS_data1, linewidth=linewidth, color=colors[i])
        i += 1

    # for temp in [200,250,300]:

        # Calculate the EA signal
        # if smooth:
        #     ABS_data2 = cmf.absorption_smooth(data['trans'][temp]['R (V)'], data['blank2']['R (V)'])
        # else:
        #     ABS_data2 = cmf.absorption(data['trans'][temp]['R (V)'], data['blank2']['R (V)'])
        
        # ax.plot(X2,ABS_data2, linewidth=linewidth, color=colors[i])
        # i += 1
    
    ax.tick_params(axis='both',which='major', labelsize=12)
    ax.set_ylabel('Absorption (OD)',fontsize = text_size)



def plot_EA_voltage(data, ax, voltage, smooth=False, color='blue', energy=True,legend=None,phased=True,text_size=14):
    # Get wavelength
    X = data['trans']['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)',fontsize = text_size)    
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)',fontsize = text_size)

    if phased:
        data['voltages'][voltage]['X (V)'] = data['voltages'][voltage]['X (V) Phased']
    
    # Calculate the EA signal
    if smooth:
        EA_data = cmf.EA_smooth(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])
    else:
        EA_data = cmf.EA(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])
    
    
    # legend name
    if legend == None:
        legend = '{}V'.format(voltage)    

    ax.plot(X,EA_data*1000, label=legend, color=color)
    ax.axhline(y=0,color='k',linewidth=0.8)
    plt.legend(loc='upper right')
    ax.set_ylabel('Electroabsorption (mOD)',fontsize = text_size)



def plot_absorption(data, ax, smooth = False, color='blue', energy=True,legend=None,value=1,text_size=14):
    # Get wavelength
    X = data['blank']['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)',fontsize = text_size)    
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)',fontsize = text_size)


    
    # Calculate the absorption signal
    if smooth:
        ABS_data = cmf.absorption_smooth(data['trans']['R (V)'], data['blank']['R (V)'])    
    else:
        ABS_data = cmf.absorption(data['trans']['R (V)'], data['blank']['R (V)'])

    ABS_data = ABS_data/value

    ax.plot(X,ABS_data, color, label=legend)
    # ax.semilogy(X,ABS_data, color, label=legend)
    # ax.legend(loc='upper right')
    ax.tick_params(axis='both',which='major', labelsize=12)
    ax.set_ylabel('Absorption (OD)',fontsize = text_size)
    


def plot_deriv_absorption(data,  ax, smooth = False, color='red', order=1, energy=True):
    # Get wavelength
    X = data['blank']['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)')      
    

    
    # Calculate the absorption signal
    if smooth:
        ABS_data = cmf.absorption_smooth(data['trans']['R (V)'], data['blank']['R (V)'])    
        derivative = cmf.finite_difference_derivative(X, cmf.savitzky_golay_smoothing(ABS_data), order)
    else:
        ABS_data = cmf.absorption(data['trans']['R (V)'], data['blank']['R (V)'])
        derivative = cmf.finite_difference_derivative(X, ABS_data, order)

    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)')

    # derivative = cmf.spline_derivative(wavelength, ABS_data, order=order, s=1e-6)


    # legend name 
    legend = 'Absorption'    

    ax.plot(X[:-order], derivative/np.max(np.abs(derivative)), label=legend, color=color)
    # ax.legend()
    ax.set_ylabel('Absorption (OD)')



''' Still a working progress'''
def plot_FK_fit(data, ax, voltage, smooth = False, color='red', energy=True):
    # Get wavelength
    X = data['blank']['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)')     
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)')



    # Get wavelength
    wavelength = data['trans']['Digikrom Spectr.:0 (?)']
    energy = cmf.wavelength_to_energy(wavelength)
    energy = data['trans']['Digikrom Spectr.:0 (?)']


    # Calculate the absorption signal
    if smooth:
        ABS_data = cmf.absorption_smooth(data['trans']['R (V)'], data['blank']['R (V)'])    
        derivative_1 = cmf.finite_difference_derivative(wavelength, cmf.savitzky_golay_smoothing(ABS_data), 1)
        derivative_2 = cmf.finite_difference_derivative(wavelength, cmf.savitzky_golay_smoothing(ABS_data), 2)
    else:
        ABS_data = cmf.absorption(data['trans']['R (V)'], data['blank']['R (V)'])
        derivative_1 = cmf.finite_difference_derivative(wavelength, ABS_data, 1)
        derivative_2 = cmf.finite_difference_derivative(wavelength, ABS_data, 2)

    data_to_fit = data['voltages'][voltage]['X (V) Phased']
    
    # Normalize the data
    data_to_fit/=np.max(abs(data_to_fit))
    derivative_1/=np.max(abs(derivative_1))
    derivative_2/=np.max(abs(derivative_2))
    
    offset = -1
    # print(derivative_1[1:])
    FK_fit = cmf.FK_fit(d_1 = derivative_1[1:offset], d_2 = derivative_2[:offset], data_to_fit = data_to_fit[2:offset])
    # legend name 
    legend = 'Absorption'    

    ax.plot(X[:], data_to_fit, label='data to fit')
    ax.plot(X[1:], derivative_1, label='d_1')
    ax.plot(X[2:], derivative_2, label='d_2')
    ax.plot(X[2:offset], FK_fit, label='Fit', color=color)
    ax.legend()
    ax.set_ylabel('Absorption (mOD)')



def plot_data(data, ax, smooth = False, energy=True):
    # Get wavelength
    X = data['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)')    
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)')

  
    # Gets all of the keys except the wavelength 
    # data_keys = list(data.keys())[1:]
    data_keys = list(data.keys())[4:6]
    # data_keys = ['X (V) Phased']
    
    # Plot the data
    if smooth:
        for data_key in data_keys:
            ax.plot(X, cmf.savitzky_golay_smoothing(data[data_key]) ,label=data_key)    
            # ax.semilogy(X, cmf.savitzky_golay_smoothing(data[data_key]) ,label=data_key)  
        # ax.plot(X,data['X (V)'],label = 'X (V)')
        # ax.plot(X,data['R (V)'],label = 'R (V)')
    else:
        for data_key in data_keys:
            ax.plot(X, data[data_key] ,label=data_key)
        # ax.plot(X,data['X (V)'],label = 'X (V)')
        # ax.plot(X,data['R (V)'],label = 'R (V)')

    
    ax.legend()
    ax.set_ylabel('Raw data')



def plot_CD(data, ax, energy=True, Phased=True):
    # Get wavelength
    X = data['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)')      
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)')


    # Calculate the EA signal
    if Phased:
        CD_data = cmf.circular_dichrosim(data['X (V) Phased'], data['Fluke (V)'])
    else:
        CD_data = cmf.circular_dichrosim_smooth(data['X830 (V)'], data['Fluke (V)']-0.0175)

    # ax.plot(X,data['Fluke (V)'])
    # ax.plot(X,data['X830 (V)'])
    ax.plot(X,-CD_data)
    ax.set_ylabel('Circular Dichrosim (mdeg)')
    return CD_data



def plot_CD_Carter(data, ax, energy=True, smoothed=False, smooth=False,color='blue'):
    # Get wavelength
    X = data['DC']['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)')      
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)')
    


    # Calculate the EA signal
    if smoothed:
        CD_data = cmf.circular_dichrosim_smooth(data['AC']['X (V)'], data['DC']['R (V)'])
    else:
        # CD_data = cmf.circular_dichrosim_smooth(-data['AC']['X (V)'], data['DC']['X (V)'])
        CD_data = cmf.circular_dichrosim(data['AC']['X (V)'], data['DC']['R (V)'])

    print('Not phased')

    Y = np.zeros_like(X)

    ax.plot(X,CD_data,color)
    ax.axhline(0,color='black',linewidth=1)
    # ax.plot(X,Y)
    ax.set_ylabel('Circular Dichrosim (mdeg)')
    return CD_data



'''
This plots the data for Photoluminescense, it gives the option to also plot it on a log plot
'''
def plot_PL(data, ax, energy=True, normalize=False):
    # Get wavelength

    X = data['Wavelength']
    ax.set_xlabel('Wavelength (nm)')    
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)')    

    max_value = 1
    if normalize:
            max_value = np.max(np.array(data['Processed Data']))

    # Y = (data['Processed Data']-max_value)/(data['Processed Data'][85]-max_value)
    Y =data['Processed Data']/max_value
    # print(cmf.FWHM(X,data['Processed Data']))
    ax.plot(X, Y)
    # ax.semilogy(X, Y)
    ax.set_ylabel('PL Intensity A.U.')


'''
This plots the data for Photoluminescense, it gives the option to also plot it on a log plot
'''
# def plot_EA_series(data, ax, colorbar=True, smooth=False, color_map_name='autumn_r', linewidth = 1, energy=True, phased=True,text_size=14):
# # def plot_PL_test(data, ax, energy=True, normalize=False):
#     # Get wavelength
#     X = data['trans']['Digikrom Spectr.:0 (?)']
#     ax.set_xlabel('Wavelength (nm)',fontsize=text_size)    

    
#     if energy:
#         X = cmf.wavelength_to_energy(X)
#         ax.set_xlabel('Energy (eV)',fontsize=text_size)

#     # Getting the different voltage values
#     voltages = np.array(list(data['voltages'].keys()))
#     # Adds a color bar if true, otherwise defines colors for each plot item
#     if colorbar == True:
#         colors = color_bar(voltages, ax, color_map_name, temp=False, pad=0.10)
#     else:
#         color_map_func = getattr(plt.cm, color_map_name)
#         colors = color_map_func(np.linspace(0, 1, len(voltages)))
#     # # Create a custom colormap for the voltages 
#     # color_map_func = getattr(plt.cm, color_map_name)
#     # colors = color_map_func(np.linspace(0, 1, len(voltages))) # <------------ Change plt.cm.__color id__ to get a different color
#     # colors = colors[::-1]
#     # custom_cmap = ListedColormap(colors)

#     # if colorbar == True:
#     #     # Add a color bar next to the plot
#     #     voltage_diff = abs(voltages[0]-voltages[1])/2
#     #     cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=custom_cmap, 
#     #         norm=plt.Normalize(vmin=np.min(voltages)-voltage_diff, vmax=np.max(voltages)+voltage_diff)), 
#     #         ax=ax, pad=0.15, orientation='vertical')
#     #     cbar.set_label('Voltage')
#     #     cbar.set_ticks(voltages)       # Example tick positions
#     #     cbar_labels  = ['{}V'.format(V) for V in voltages]
#     #     cbar.set_ticklabels(cbar_labels)  # Corresponding labels


#     if phased:
#         for voltage in voltages:            
#             data['voltages'][voltage]['X (V)'] = data['voltages'][voltage]['X (V) Phased']


#     # Plot the data
#     i = 0
#     for voltage in voltages:
#         # Calculate the EA signal
#         if smooth:
#             EA_data = cmf.EA_smooth(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])
#             # EA_data = EA_data + 1e-4
#         else:
#             EA_data = cmf.EA(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])
        

#         ax.plot(X,EA_data*1000, linewidth=linewidth, color=colors[i])
#         i += 1

#     ax.tick_params(axis='both',which='major', labelsize=12)
#     ax.axhline(y=0,color='k',linewidth=0.8)
#     ax.set_ylabel('Electroabsorption (mOD)',fontsize=text_size)
#     # ax.set_ylabel('Electroreflection (mOD)',fontsize=text_size)



#     #############################################################################################################################


#     # Get wavelength
#     X = data['Wavelength']
#     ax.set_xlabel('Wavelength (nm)')    

#     voltages = np.array(list(data['voltages'].keys()))    
#     if energy:
#         X = cmf.wavelength_to_energy(X)
#         ax.set_xlabel('Energy (eV)')    

#     max_value = 1
#     if normalize:
#             max_value = np.max(np.array(data['Processed Data']))

#     # Y = (data['Processed Data']-max_value)/(data['Processed Data'][85]-max_value)
#     Y =data['Processed Data']/max_value
#     # print(cmf.FWHM(X,data['Processed Data']))
#     ax.plot(X, Y)
#     # ax.semilogy(X, Y)
#     ax.set_ylabel('PL Intensity A.U.')

def plot_CPL(data, ax1, ax2, smooth = False, energy=True):
    # Get wavelength
    X = data['Spectrometer Triax 550:0 (?)']
    ax1.set_xlabel('Wavelength (nm)')    
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax1.set_xlabel('Energy (eV)')    


    # # Plot the data
    # if smooth:
    #     for data_key in data_keys:
    #         ax.plot(X, cmf.savitzky_golay_smoothing(data[data_key]) ,label=data_key)    
    # else:
    #     for data_key in data_keys:
    #         ax.plot(X, data[data_key] ,label=data_key)

    A = data['PC ChA (Counts) (cps)']
    B = data['PC ChB (Counts) (cps)']

    ax1.plot(X, A, label='A')
    ax1.plot(X, B, label='B')
    ax1.plot(X, A+B, label='PL')


    ax2.plot(X, cmf.difference_to_sum_ratio(A,B))



def plot_etch_a_sketch(data, ax):
    # Get wavelength
    X = data['Time (s)']
    ax.set_xlabel('Time (s)')    
  
    # Gets all of the keys except the time
    data_keys = list(data.keys())[1:]
    

    for data_key in data_keys:
        ax.plot(X, data[data_key] ,label=data_key)


    ax.legend()
    ax.set_ylabel('Raw data')



def plot_TCSPC(data, ax, normalize=False):
    # Get wavelength
    ax.set_xlabel('Time (ns)')    
    

    ax.plot(data['Time'], data['Counts'])
    ax.semilogy(data['Time'], data['Counts'])
    ax.set_ylabel('Counts')



def plot_TCSPC_Series(data, ax, colorbar=True, color_map_name='nipy_spectral', linewidth = 1):
    # Get wavelength
    ax.set_xlabel('Time (ns)')    
    

    # Getting the different voltage values
    wavelengths = np.array(list(data.keys()))
    wavelengths = sorted(wavelengths)
    print(wavelengths)


    # Create a custom colormap for the voltages 
    color_map_func = getattr(plt.cm, color_map_name)
    colors = color_map_func(np.linspace(0,1, len(wavelengths))) # <------------ Change plt.cm.__color id__ to get a different color
    # colors = color_map_func(np.linspace(0.0625, 0.875, len(wavelengths))) # <------------ Change plt.cm.__color id__ to get a different color
    custom_cmap = ListedColormap(colors)


    if colorbar == True:
        # Add a color bar next to the plot
        voltage_diff = abs(wavelengths[0]-wavelengths[1])/2
        cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=custom_cmap, 
            norm=plt.Normalize(vmin=np.min(wavelengths)-voltage_diff, vmax=np.max(wavelengths)+voltage_diff)), 
            ax=ax, pad=0.01, orientation='vertical')
        # cbar.set_label('Wavelengths')
        cbar.set_label('Temperature (K)')

        step = 1
        cbar.set_ticks(wavelengths[::step])       
        cbar_labels  = ['{}'.format(V) for V in wavelengths[::step]]
        cbar.set_ticklabels(cbar_labels)  # Corresponding labels

    # Plot the data
    i = 0
    for wavelength in wavelengths:
        ax.plot(data[wavelength]['Time'],data[wavelength]['Counts'], linewidth=linewidth, color=colors[i])
        i += 1
    
    ax.set_ylabel('TRPL Intensity A.U.')



def plot_TCSPC_Series_Maximum(data, ax, colorbar=True, color_map_name='nipy_spectral'):
    # Get wavelength
    ax.set_xlabel('Time (ns)')    
    

    # Getting the different voltage values
    wavelengths = np.array(list(data.keys()))
    wavelengths = sorted(wavelengths)
    # print(wavelengths)


    # Create a custom colormap for the voltages 
    color_map_func = getattr(plt.cm, color_map_name)
    colors = color_map_func(np.linspace(0, 1, len(wavelengths))) # <------------ Change plt.cm.__color id__ to get a different color
    # colors = color_map_func(np.linspace(0.0625, 0.875, len(wavelengths))) # <------------ Change plt.cm.__color id__ to get a different color
    custom_cmap = ListedColormap(colors)


    if colorbar == True:
        # Add a color bar next to the plot
        voltage_diff = abs(wavelengths[0]-wavelengths[1])/2
        cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=custom_cmap, 
            norm=plt.Normalize(vmin=np.min(wavelengths)-voltage_diff, vmax=np.max(wavelengths)+voltage_diff)), 
            ax=ax, pad=0.01, orientation='vertical')
        # cbar.set_label('Wavelengths')
        cbar.set_label('Temperature (K)')

        step = 1
        cbar.set_ticks(wavelengths[::step])       
        cbar_labels  = ['{}'.format(V) for V in wavelengths[::step]]
        cbar.set_ticklabels(cbar_labels)  # Corresponding labels

    # Plot the data
    i = 0
    for wavelength in wavelengths:
        index = np.argmax(data[wavelength]['Counts'])
        ax.scatter(data[wavelength]['Time'][index],data[wavelength]['Counts'][index], color=colors[i])
        i += 1
    
    ax.set_ylabel('TRPL Intensity A.U.')



def plot_TCSPC_Series_FWHM(data, ax, colorbar=False, color_map_name='nipy_spectral'):
    # Get wavelength
    ax.set_xlabel('Wavelength (nm)')    
    

    # Getting the different voltage values
    wavelengths = np.array(list(data.keys()))
    wavelengths = sorted(wavelengths)
    # print(wavelengths)


    # Create a custom colormap for the voltages 
    color_map_func = getattr(plt.cm, color_map_name)
    colors = color_map_func(np.linspace(0, 1, len(wavelengths))) # <------------ Change plt.cm.__color id__ to get a different color
    # colors = color_map_func(np.linspace(0.0625, 0.875, len(wavelengths))) # <------------ Change plt.cm.__color id__ to get a different color
    custom_cmap = ListedColormap(colors)


    if colorbar == True:
        # Add a color bar next to the plot
        voltage_diff = abs(wavelengths[0]-wavelengths[1])/2
        cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=custom_cmap, 
            norm=plt.Normalize(vmin=np.min(wavelengths)-voltage_diff, vmax=np.max(wavelengths)+voltage_diff)), 
            ax=ax, pad=0.01, orientation='vertical')
        # cbar.set_label('Wavelengths')
        cbar.set_label('Temperature (K)')

        step = 1
        cbar.set_ticks(wavelengths[::step])       
        cbar_labels  = ['{}'.format(V) for V in wavelengths[::step]]
        cbar.set_ticklabels(cbar_labels)  # Corresponding labels

    # Plot the data
    i = 0
    fwhm_list = []
    for wavelength in wavelengths:
        fwhm = cmf.FWHM(data[wavelength]['Time'],data[wavelength]['Counts'])
        fwhm_list.append([wavelength,fwhm])
        ax.scatter(wavelength,fwhm, color=colors[i])
        i += 1
    
    ax.set_ylabel('FWHM (ns)')
    return np.array(fwhm_list)



def plot_TCSPC_Series_decay_rate(data, ax, colorbar=False, color_map_name='nipy_spectral'):
    # Get wavelength
    ax.set_xlabel('Temperature (K)')    
    

    # Getting the different voltage values
    wavelengths = np.array(list(data.keys()))
    wavelengths = sorted(wavelengths)
    # print(wavelengths)


    # Create a custom colormap for the voltages 
    color_map_func = getattr(plt.cm, color_map_name)
    colors = color_map_func(np.linspace(0, 1, len(wavelengths))) # <------------ Change plt.cm.__color id__ to get a different color
    # colors = color_map_func(np.linspace(0.0625, 0.875, len(wavelengths))) # <------------ Change plt.cm.__color id__ to get a different color
    custom_cmap = ListedColormap(colors)


    if colorbar == True:
        # Add a color bar next to the plot
        voltage_diff = abs(wavelengths[0]-wavelengths[1])/2
        cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=custom_cmap, 
            norm=plt.Normalize(vmin=np.min(wavelengths)-voltage_diff, vmax=np.max(wavelengths)+voltage_diff)), 
            ax=ax, pad=0.01, orientation='vertical')
        # cbar.set_label('Wavelengths')
        cbar.set_label('Temperature (K)')

        step = 1
        cbar.set_ticks(wavelengths[::step])       
        cbar_labels  = ['{}'.format(V) for V in wavelengths[::step]]
        cbar.set_ticklabels(cbar_labels)  # Corresponding labels

    # Plot the data
    i = 0
    decay_rates = []
    for wavelength in wavelengths[:]:
        decay_rate1, decay_rate2 = cmf.TCSPC_decay_rate(data[wavelength]['Time'],data[wavelength]['Counts'])
        decay_rates.append([wavelength,decay_rate1])
        ax.scatter(wavelength,decay_rate1, color=colors[i])
        ax.scatter(wavelength,decay_rate2, color=colors[i])
        i += 1
    
    ax.set_ylabel('Decay Rate $(ns)$')
    return np.array(decay_rates)



'''
This plots the data for Photoluminescense, it gives the option to also plot it on a log plot
'''
def plot_PL_FWHM(data, ax, temperature, energy=True):

    # Get wavelength
    X = data['Wavelength']
    ax.set_ylabel('FWHM (nm)')
    
    if energy:
        X = -cmf.wavelength_to_energy(X)
        ax.set_ylabel('FWHM (eV)')
    
    fwhm = cmf.FWHM(X,data['Processed Data'])
    ax.scatter(int(temperature), fwhm)

    
    ax.set_xlabel('Temperature (K)')


    
def plot_TCSPC_PL_time(data, ax, colorbar=False, color_map_name='nipy_spectral'):
    # Get wavelength
    ax.set_xlabel('Wavelength (nm)')    
    

    # Getting the different voltage values
    wavelengths = np.array(list(data.keys()))
    wavelengths = sorted(wavelengths)

    # Create a custom colormap for the voltages 
    color_map_func = getattr(plt.cm, color_map_name)
    colors = color_map_func(np.linspace(0, 1, len(wavelengths))) # <------------ Change plt.cm.__color id__ to get a different color
    # colors = color_map_func(np.linspace(0.0625, 0.875, len(wavelengths))) # <------------ Change plt.cm.__color id__ to get a different color
    custom_cmap = ListedColormap(colors)


    if colorbar == True:
        # Add a color bar next to the plot
        voltage_diff = abs(wavelengths[0]-wavelengths[1])/2
        cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=custom_cmap, 
            norm=plt.Normalize(vmin=np.min(wavelengths)-voltage_diff, vmax=np.max(wavelengths)+voltage_diff)), 
            ax=ax, pad=0.01, orientation='vertical')
        cbar.set_label('Wavelengths')

        step = 2
        cbar.set_ticks(wavelengths[::step])       
        cbar_labels  = ['{} nm'.format(V) for V in wavelengths[::step]]
        cbar.set_ticklabels(cbar_labels)  # Corresponding labels

    PL_signal = np.zeros(len(wavelengths))

    for t in range(0,1700):
        time_array = np.array([data[wavelength]['Counts'][t] for wavelength in wavelengths])
        PL_signal += time_array
    ax.plot(wavelengths, PL_signal/np.max(PL_signal))

    # Plot the data
    i = 0
    # decay_rates = []
    # for wavelength in wavelengths[:]:
    #     decay_rate = cmf.TCSPC_decay_rate(data[wavelength]['Time'],data[wavelength]['Counts'])
    #     decay_rates.append([wavelength,decay_rate])
    #     ax.scatter(wavelength,decay_rate, color=colors[i])
    #     i += 1
    
    # ax.set_ylabel('Decay Rate $(ns^{-1})$')

