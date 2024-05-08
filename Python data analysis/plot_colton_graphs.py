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


def plot_EA_series(data, ax, colorbar=True, color_map_name='autumn_r', linewidth = 1):
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
        cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=custom_cmap, norm=plt.Normalize(vmin=0, vmax=np.max(voltages))), ax=ax, pad=0.15, orientation='vertical')
        cbar.set_label('Voltage')


    # Plot the data
    i = 0
    for voltage in voltages:
        EA_data = cmf.EA(data['voltages'][voltage]['X (V) Phased'], data['trans']['R (V)'])
        
        ax.plot(energy,-EA_data*1000, linewidth=linewidth, color=colors[i])
        i += 1
    
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('Electroabsorption (mOD)')




def plot_EA_voltage(data, ax, voltage=''):
    # Get wavelength
    wavelength = data['trans']['Digikrom Spectr.:0 (?)']
    energy = cmf.wavelength_to_energy(wavelength)    
    
    # Calculate the EA signal
    EA_data = cmf.EA(data['voltage']['X (V) Phased'], data['trans']['R (V)'])
    
    # legend name 
    legend = '{}V'.format(voltage)    

    ax.plot(energy,EA_data*1000, label=legend)
    plt.legend()
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('Electroabsorption (mOD)')




def plot_absorption(data, ax, color='blue'):
    # Get wavelength
    wavelength = data['trans']['Digikrom Spectr.:0 (?)']
    energy = cmf.wavelength_to_energy(wavelength)    
    
    # Calculate the absorption signal
    ABS_data = cmf.absorption(data['trans']['R (V)'], data['blank']['R (V)'])    
     
    # legend name 
    legend = 'Absorption'    

    ax.plot(energy,ABS_data, label=legend, color=color)
    # ax.legend()
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('Absorption (OD)')
    







