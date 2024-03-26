"""
Script Name: plot_colton_graphs
Author: Carter Shirley
Date: February 20, 2024
Description: This code takes in a dictionary with the data inside it and gives out a plot.  

"""

import read_colton_files as rcf
import colton_math_functions as cmf
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


def plot_EA_series(data, ax, colorbar=True, smooth=False, color_map_name='autumn_r', linewidth = 1):
    # Get wavelength
    wavelength = data['trans']['Digikrom Spectr.:0 (?)']
    energy = cmf.wavelength_to_energy(wavelength)

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
        

        ax.plot(energy,EA_data*1000, linewidth=linewidth, color=colors[i])
        i += 1
    
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('Electroabsorption (mOD)')

def plot_EA_temp_series(data, ax, colorbar=True, color_map_name='autumn_r', linewidth = 1):
    # Get wavelength
    wavelength = data['blank']['Digikrom Spectr.:0 (?)']
    energy = cmf.wavelength_to_energy(wavelength)

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
        
        ax.plot(energy,EA_data*1000, linewidth=linewidth, color=colors[i])
        i += 1
    
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('Electroabsorption (mOD)')

def plot_ABS_temp_series(data, ax, colorbar=True, color_map_name='autumn_r', linewidth = 1):
    # Get wavelength
    wavelength = data['blank']['Digikrom Spectr.:0 (?)']
    energy = cmf.wavelength_to_energy(wavelength)

    # Getting the different voltage values
    temperatures = np.array(list(data['trans'].keys()))

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
        ABS_data = cmf.absorption(data['trans'][temp]['R (V)'], data['blank']['R (V)'])
        
        ax.plot(energy,ABS_data, linewidth=linewidth, color=colors[i])
        i += 1
    
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('Absorption (OD)')

def plot_EA_voltage(data, ax, smooth=False, voltage='', color='blue'):
    # Get wavelength
    wavelength = data['trans']['Digikrom Spectr.:0 (?)']
    energy = cmf.wavelength_to_energy(wavelength)    
    
    # Calculate the EA signal
    if smooth:
        EA_data = cmf.EA_smooth(data['voltage']['X (V) Phased'], data['trans']['R (V)'])
    else:
        EA_data = cmf.EA(data['voltage']['X (V) Phased'], data['trans']['R (V)'])
    
    
    # legend name 
    legend = '{}V'.format(voltage)    

    ax.plot(energy,EA_data*1000, label=legend, color=color)
    plt.legend()
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('Electroabsorption (mOD)')

def plot_absorption(data, ax, smooth = False, color='blue'):
    # Get wavelength
    wavelength = data['trans']['Digikrom Spectr.:0 (?)']
    energy = cmf.wavelength_to_energy(wavelength)    
    
    # Calculate the absorption signal
    if smooth:
        ABS_data = cmf.absorption_smooth(data['trans']['R (V)'], data['blank']['R (V)'])    
    else:
        ABS_data = cmf.absorption(data['trans']['R (V)'], data['blank']['R (V)'])


    # legend name 
    legend = 'Absorption'    

    ax.plot(energy,ABS_data, label=legend, color=color)
    # ax.legend()
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('Absorption (OD)')
    


def plot_data(data, ax, smooth = False):
    # Get wavelength
    wavelength = data['Digikrom Spectr.:0 (?)']
    energy = cmf.wavelength_to_energy(wavelength)    
    
    # Gets all of the keys except the wavelength 
    data_keys = list(data.keys())[1:]
    
    # Plot the data
    if smooth:
        for data_key in data_keys:
            ax.plot(energy, cmf.savitzky_golay_smoothing(data[data_key]) ,label=data_key)    
    else:
        for data_key in data_keys:
            ax.plot(energy, data[data_key] ,label=data_key)

    ax.legend()
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('Raw data')



def plot_CD(data, ax):
    # Get wavelength
    wavelength = data['Digikrom Spectr.:0 (?)']
    energy = cmf.wavelength_to_energy(wavelength)    
    
    # Calculate the EA signal
    CD_data = cmf.circular_dichrosim(data['X (V) Phased'], data['Keithley (V)'])
    
    ax.plot(energy,CD_data)
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('Circular Dichrosim (mdeg)')