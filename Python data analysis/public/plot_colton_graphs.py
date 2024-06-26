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
import numpy as np


def plot_EA_series(data, ax, colorbar=True, smooth=False, color_map_name='autumn_r', linewidth = 1, energy=True):
    # Get wavelength
    X = data['trans']['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)')    


    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)')



    # Getting the different voltage values
    voltages = np.array(list(data['voltages'].keys()))

    # Create a custom colormap for the voltages 
    color_map_func = getattr(plt.cm, color_map_name)
    colors = color_map_func(np.linspace(0, 1, len(voltages))) # <------------ Change plt.cm.__color id__ to get a different color
    custom_cmap = ListedColormap(colors)

    if colorbar == True:
        # Add a color bar next to the plot
        voltage_diff = abs(voltages[0]-voltages[1])/2
        cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=custom_cmap, 
            norm=plt.Normalize(vmin=np.min(voltages)-voltage_diff, vmax=np.max(voltages)+voltage_diff)), 
            ax=ax, pad=0.15, orientation='vertical')
        cbar.set_label('Voltage')
        cbar.set_ticks(voltages)       # Example tick positions
        cbar_labels  = ['{}V'.format(V) for V in voltages]
        cbar.set_ticklabels(cbar_labels)  # Corresponding labels

    # Plot the data
    i = 0
    for voltage in voltages:
        # Calculate the EA signal
        if smooth:
            EA_data = cmf.EA_smooth(data['voltages'][voltage]['X (V) Phased'], data['trans']['R (V)'])
        else:
            EA_data = cmf.EA(data['voltages'][voltage]['X (V) Phased'], data['trans']['R (V)'])
        

        ax.plot(X,EA_data*1000, linewidth=linewidth, color=colors[i])
        i += 1
    
    ax.set_ylabel('Electroabsorption (mOD)')
    # ax.set_ylabel('Electrorelection (mOD)')

def plot_EA_temp_series(data, ax, colorbar=True, color_map_name='autumn_r', linewidth = 1, energy=True):
    # Get wavelength
    X = data['Wavelength']
    ax.set_xlabel('Wavelength (nm)')    
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)')



    # Getting the different voltage values
    temperatures = np.array(list(data['voltages'].keys()))

    # Create a custom colormap for the voltages 
    color_map_func = getattr(plt.cm, color_map_name)
    colors = color_map_func(np.linspace(0, 1, len(temperatures))) # <------------ Change plt.cm.__color id__ to get a different color
    custom_cmap = ListedColormap(colors)

    if colorbar == True:
        # Add a color bar next to the plot
        cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=custom_cmap, norm=plt.Normalize(vmin=0, vmax=np.max(temperatures)*1.05)), ax=ax, pad=0, orientation='vertical')
        cbar.set_label('Temperatures (K)')
        cbar.set_ticks(temperatures)

    # Plot the data
    i = 0
    for temp in temperatures:
        EA_data = cmf.EA(data['voltages'][temp]['X (V) Phased'], data['trans'][temp]['R (V)'])
        
        ax.plot(X,EA_data*1000, linewidth=linewidth, color=colors[i])
        i += 1
    
    ax.set_ylabel('Electroabsorption (mOD)')

def plot_ABS_temp_series(data, ax, colorbar=True, color_map_name='autumn_r', linewidth = 1, energy=True, smooth=False):
    # Get wavelength
    X = data['blank']['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)')    
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)')



    # Getting the different voltage values
    temperatures = np.array(list(data['trans'].keys()))

    # Create a custom colormap for the temperatures 
    color_map_func = getattr(plt.cm, color_map_name)
    colors = color_map_func(np.linspace(0, 1, len(temperatures))) # <------------ Change plt.cm.__color id__ to get a different color
    custom_cmap = ListedColormap(colors)

    if colorbar == True:
        # Add a color bar next to the plot
        cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=custom_cmap, norm=plt.Normalize(vmin=0, vmax=np.max(temperatures)*1.05)), ax=ax, pad=0, orientation='vertical')
        cbar.set_label('Temperatures (K)')
        cbar.set_ticks(temperatures)


    # Plot the data
    i = 0
    for temp in temperatures:

        # Calculate the EA signal
        if smooth:
            ABS_data = cmf.absorption_smooth(data['trans'][temp]['R (V)'], data['blank']['R (V)'])
        else:
            ABS_data = cmf.absorption(data['trans'][temp]['R (V)'], data['blank']['R (V)'])
        
        ax.plot(X,ABS_data, linewidth=linewidth, color=colors[i])
        i += 1
    
    ax.set_ylabel('Absorption (OD)')


def plot_EA_voltage(data, ax, voltage, smooth=False, color='blue', energy=True):
    # Get wavelength
    X = data['trans']['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)')    
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)')


    
    # Calculate the EA signal
    if smooth:
        EA_data = cmf.EA_smooth(data['voltages'][voltage]['X (V) Phased'], data['trans']['R (V)'])
    else:
        EA_data = cmf.EA(data['voltages'][voltage]['X (V) Phased'], data['trans']['R (V)'])
    
    
    # legend name 
    legend = '{}V'.format(voltage)    

    ax.plot(X,EA_data*1000, label=legend, color=color)
    plt.legend()
    ax.set_ylabel('Electroabsorption (mOD)')




def plot_absorption(data, ax, smooth = False, color='blue', energy=True):
    # Get wavelength
    X = data['blank']['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)')    
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)')


    
    # Calculate the absorption signal
    if smooth:
        ABS_data = cmf.absorption_smooth(data['trans']['R (V)'], data['blank']['R (V)'])    
    else:
        ABS_data = cmf.absorption(data['trans']['R (V)'], data['blank']['R (V)'])


    # legend name 
    legend = 'Absorption'    

    ax.plot(X,ABS_data, label=legend, color=color)
    # ax.legend()
    ax.set_ylabel('Absorption (OD)')
    



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

    ax.plot(X[:-order], derivative, label=legend, color=color)
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
    data_keys = list(data.keys())[1:]
    
    # Plot the data
    if smooth:
        for data_key in data_keys:
            ax.plot(X, cmf.savitzky_golay_smoothing(data[data_key]) ,label=data_key)    
    else:
        for data_key in data_keys:
            ax.plot(X, data[data_key] ,label=data_key)

    ax.legend()
    ax.set_ylabel('Raw data')



def plot_CD(data, ax, energy=True):
    # Get wavelength
    X = data['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)')      
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)')


    # Calculate the EA signal
    CD_data = cmf.circular_dichrosim(data['X (V) Phased'], data['Keithley (V)'])
    
    ax.plot(X,CD_data)
    ax.set_ylabel('Circular Dichrosim (mdeg)')




def plot_PL(data, ax, energy=True, normalize=False):
    # Get wavelength
    X = data['Wavelength']
    ax.set_xlabel('Wavelength (nm)')    
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)')    

    max_value = 1
    if normalize:
            max_value = max(data['Processed Data'])
    
    ax.plot(X, data['Processed Data']/max_value)
    # ax.semilogy(X, data['Processed Data'])
    ax.set_ylabel('Counts')



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











