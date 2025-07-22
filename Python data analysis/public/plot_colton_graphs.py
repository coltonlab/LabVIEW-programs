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


def plot_EA_series(data, ax, colorbar=True, smooth=False, color_map_name='autumn_r'
                   , linewidth = 1, energy=True, phased=True,flip = False,text_size=14):
    # Getting the different voltage values
    voltages = np.array(sorted(list(data['voltages'].keys())))
    electric_field = cmf.electric_field_kV_per_cm(voltages)
    # print(electric_field)
    # Adds a color bar if true, otherwise defines colors for each plot item
    if colorbar == True:
        colors = color_bar(electric_field, ax, color_map_name, temp=False, pad=0.10)
    else:
        color_map_func = getattr(plt.cm, color_map_name)
        colors = color_map_func(np.linspace(0, 1, len(voltages))) 


    # Plot the data
    for i, voltage in enumerate(voltages):
        # Use phase data if true
        if phased:      
            data['voltages'][voltage]['X (V)'] = data['voltages'][voltage]['X (V) Phased']

        if flip:      
            data['voltages'][voltage]['X (V)'] = -data['voltages'][voltage]['X (V)']

        # Get wavelength
        X = data['voltages'][voltage]['Digikrom Spectr.:0 (?)']
        ax.set_xlabel('Wavelength (nm)',fontsize=text_size)    
        
        # Energy per wavelength
        if energy:
            X = cmf.wavelength_to_energy(X)
            ax.set_xlabel('Energy (eV)',fontsize=text_size)

        # Calculate the EA signal
        if smooth:
            EA_data = cmf.EA_smooth(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])
        else:
            EA_data = cmf.EA(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])
        
        ax.plot(X,EA_data, linewidth=linewidth, color=colors[i], label=f'{cmf.electric_field_kV_per_cm(voltage):.0f} kV/cm')



    ax.tick_params(axis='both',which='major', labelsize=12)
    ax.axhline(y=0,color='k',linewidth=0.8)
    return EA_data


def plot_ER_series(data, ax, colorbar=True, smooth=False, color_map_name='autumn_r'
                   , linewidth = 1, energy=True, phased=True,flip = False,text_size=14):
    # Getting the different voltage values
    voltages = np.array(list(data['voltages'].keys()))

    # Adds a color bar if true, otherwise defines colors for each plot item
    if colorbar == True:
        colors = color_bar(voltages, ax, color_map_name, temp=False, pad=0.10)
    else:
        color_map_func = getattr(plt.cm, color_map_name)
        colors = color_map_func(np.linspace(0, 1, len(voltages)))        

    # Plot the data
    for i, voltage in enumerate(voltages):
        # Use phase data if true
        if phased:      
            data['voltages'][voltage]['X (V)'] = data['voltages'][voltage]['X (V) Phased']

        if flip:      
            data['voltages'][voltage]['X (V)'] = -data['voltages'][voltage]['X (V)']

        # Get wavelength
        X = data['voltages'][voltage]['Digikrom Spectr.:0 (?)']
        ax.set_xlabel('Wavelength (nm)',fontsize=text_size)    
        
        # Energy per wavelength
        if energy:
            X = cmf.wavelength_to_energy(X)
            ax.set_xlabel('Energy (eV)',fontsize=text_size)

        # Calculate the EA signal
        if smooth:
            EA_data = cmf.reflection_smooth(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])
        else:
            EA_data = cmf.reflection(data['voltages'][voltage]['X (V)'],data['trans']['R (V)'])
        

        ax.plot(X,EA_data*1000, linewidth=linewidth, color=colors[i])

    ax.tick_params(axis='both',which='major', labelsize=12)
    ax.axhline(y=0,color='k',linewidth=0.8)


def plot_EA_temp_series(data, ax, colorbar=True, color_map_name='autumn_r', linewidth = 1, energy=True,smooth=False,text_size=14, phased=True, flip=False):
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
            # Use phase data if true
        if phased:      
            data['voltages'][temp]['X (V)'] = data['voltages'][temp]['X (V) Phased']

        if flip:      
            data['voltages'][temp]['X (V)'] = -data['voltages'][temp]['X (V)']

        # Calculate the EA signal
        if smooth:
            EA_data = cmf.EA_smooth(data['voltages'][temp]['X (V)'], data['trans'][temp]['R (V)'])
        else:
            EA_data = cmf.EA(data['voltages'][temp]['X (V)'], data['trans'][temp]['R (V)'])
        
        ax.plot(X,EA_data, linewidth=linewidth, color=colors[i])
        i += 1
    
    ax.tick_params(axis='both',which='major', labelsize=12)
    ax.axhline(y=0,color='k',linewidth=0.8)
    ax.set_ylabel('Electroabsorption (mOD)',fontsize=text_size)


def plot_CD_temp_series(data, ax, colorbar=True, color_map_name='autumn_r', linewidth = 1, energy=True,smooth=False,text_size=14, phased=True, flip=False):
    # Get wavelength
    X = data['blank']['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)')    
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)',fontsize=text_size)

    # Create a color bar
    temperatures = np.array(list(data['CD'].keys()))
    # colors = color_bar(temperatures, ax, color_map_name, temp=True)
    if colorbar == True:
        colors = color_bar(temperatures, ax, color_map_name, temp=True)
    else:
        color_map_func = getattr(plt.cm, color_map_name)
        colors = color_map_func(np.linspace(0, 1, len(temperatures)))

    # Plot the data
    i = 0
    for temp in temperatures:
            # Use phase data if true
        if phased:      
            data['CD'][temp]['X (V)'] = data['CD'][temp]['X (V) Phased']

        if flip:      
            data['CD'][temp]['X (V)'] = -data['CD'][temp]['X (V)']


        # Calculate the EA signal
        if smooth:
            EA_data = cmf.circular_dichrosim_smooth(data['CD'][temp]['X (V)'], data['trans'][temp]['R (V)'])
        else:
            EA_data = cmf.circular_dichrosim(data['CD'][temp]['X (V)'], data['trans'][temp]['R (V)'])
        
        ax.plot(X,EA_data, linewidth=linewidth, color=colors[i])
        i += 1
    
    ax.tick_params(axis='both',which='major', labelsize=12)
    ax.axhline(y=0,color='k',linewidth=0.8)
    ax.set_ylabel('Circular Dichroism (mdeg)',fontsize=text_size)


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
        cbar_labels  = [f'{V} kV/cm' for V in temperatures]

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

    ax.plot(X[15:],ABS_data[15:], color, label=legend, linestyle='dashed', alpha=0.5)
    # ax.axhline(y=0,color=color,linewidth=0.8)
    # ax.semilogy(X,ABS_data, color, label=legend)
    # ax.legend(loc='upper right')
    ax.tick_params(axis='both',which='major', labelsize=12)
    ax.set_ylabel('Absorption (OD)',fontsize = text_size, color=color)


def plot_reflection(data, ax, smooth = False, color='blue', energy=True,legend=None,value=1,text_size=14):
    # Get wavelength
    X = data['blank']['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)',fontsize = text_size)    
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)',fontsize = text_size)
    
    # Calculate the absorption signal
    if smooth:
        ABS_data = cmf.reflection_smooth(data['trans']['R (V)'], data['blank']['I (V)'])    
    else:
        ABS_data = cmf.reflection(data['trans']['R (V)'], data['blank']['I (V)'])

    ABS_data = ABS_data/value

    ax.plot(X,ABS_data, color, label=legend, linestyle='dashed', alpha=0.5)
    # ax.axhline(y=0,color=color,linewidth=0.8)
    # ax.semilogy(X,ABS_data, color, label=legend)
    # ax.legend(loc='upper right')
    ax.tick_params(axis='both',which='major', labelsize=12)



def plot_transmittance(data, ax, smooth = False, color='blue', energy=True,legend=None,value=1,text_size=14):
    # Get wavelength
    X = data['blank']['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)',fontsize = text_size)    
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)',fontsize = text_size)
    
    # Calculate the absorption signal
    if smooth:
        ABS_data = cmf.reflection_smooth(data['trans']['R (V)'], data['blank']['R (V)'])    
    else:
        ABS_data = cmf.reflection(data['trans']['R (V)'], data['blank']['R (V)'])

    ABS_data = ABS_data/value

    ax.plot(X,ABS_data, color, label=legend, linestyle='dashed', alpha=0.5)
    # ax.axhline(y=0,color=color,linewidth=0.8)
    # ax.semilogy(X,ABS_data, color, label=legend)
    # ax.legend(loc='upper right')
    ax.tick_params(axis='both',which='major', labelsize=12)

def plot_ref_trans_abs(dataT, dataR, ax_all, smooth = False, energy=True,):
    ((ax1, ax2), (ax3, ax4)) = ax_all
    
    # Get wavelength
    X = dataT['blank']['Digikrom Spectr.:0 (?)']
    ax1.set_xlabel('Wavelength (nm)')
    ax2.set_xlabel('Wavelength (nm)')
    ax3.set_xlabel('Wavelength (nm)')
    ax4.set_xlabel('Wavelength (nm)')
        
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax1.set_xlabel('Energy (eV)')
        ax2.set_xlabel('Energy (eV)')
        ax3.set_xlabel('Energy (eV)')
        ax4.set_xlabel('Energy (eV)')

    value = 1#.686
    # transmittance
    if smooth:
        trans = cmf.transmition_smooth(dataT['trans']['R (V)'], dataT['blank']['I (V)']*value)    
    else:
        trans = cmf.transmition(dataT['trans']['R (V)'], dataT['blank']['I (V)']*value)


    # reflectance
    if smooth:
        reflect = cmf.reflection_smooth(dataR['trans']['R (V)'],dataR['blank']['I (V)']*value)   
    else:
        reflect = cmf.reflection(dataR['trans']['R (V)'],dataR['blank']['I (V)']*value)

    # Calculate the absorption signal
    if smooth:
        ABS_data = cmf.absorption_smooth(dataT['trans']['R (V)'], dataT['blank']['R (V)']*value)    
    else:
        ABS_data = cmf.absorption(dataT['trans']['R (V)'], dataT['blank']['R (V)']*value)
    

    ax1.plot(X,trans, color='blue')
    ax1.set_title('Transmittance')

    ax2.plot(X,reflect, color='orange')
    ax2.set_title('Reflectance')

    ax3.plot(X,1-(trans+reflect), color='red')
    ax3.set_title('Absorbance')

    # Plots
    ax4.plot(X,ABS_data, color = 'green')
    ax4.set_title('Absorption (OD)')
    # ax4.plot(X,trans, label='transmitance', color='blue')
    # ax4.plot(X,reflect, label='reflectance', color='orange')
    # ax4.plot(X,1-(trans+reflect), label='sum', color='green')

    # ax1.legend()


def plot_individual_derivatives(dataT, dataR, ax_all, smooth = False, energy=True,):
    ((ax1, ax2), (ax3, ax4)) = ax_all
    
    # Get wavelength
    X = dataT['blank']['Digikrom Spectr.:0 (?)']
    ax1.set_xlabel('Wavelength (nm)')
    ax2.set_xlabel('Wavelength (nm)')
    ax3.set_xlabel('Wavelength (nm)')
    ax4.set_xlabel('Wavelength (nm)')
        
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax1.set_xlabel('Energy (eV)')
        ax2.set_xlabel('Energy (eV)')
        ax3.set_xlabel('Energy (eV)')
        ax4.set_xlabel('Energy (eV)')

    # reflectance
    if smooth:
        trans = cmf.transmition_smooth(dataT['trans']['R (V)'], dataT['blank']['I (V)'])
        reflect = cmf.reflection_smooth(dataR['trans']['R (V)'], dataR['blank']['I (V)'])   
        absorption = cmf.absorption_smooth(dataT['trans']['R (V)'], dataT['blank']['R (V)'])
    else:
        trans = cmf.transmition(dataT['trans']['R (V)'], dataT['blank']['I (V)'])
        reflect = cmf.reflection(dataR['trans']['R (V)'], dataR['blank']['I (V)'])
        absorption = ABS_data = cmf.absorption(dataT['trans']['R (V)'], dataT['blank']['R (V)'])
    
    def derivatives(x, y, ax):
        from scipy.signal import savgol_filter
        # Apply Savitzky-Golay filter
        window_size = 11  # Must be odd
        poly_order = 3

        smoothed_y = savgol_filter(y, window_size, poly_order)
        first_derivative = savgol_filter(y, window_size, poly_order, deriv=1)
        second_derivative = savgol_filter(y, window_size+4, poly_order, deriv=2)
        third_derivative = savgol_filter(y, window_size+8, poly_order, deriv=3)

        # Plot results
        ax.plot(x, y, label="Noisy Data", linestyle='dashed', alpha=0.5)
        ax.plot(x, smoothed_y, label="Smoothed Data")
        ax.plot(x, first_derivative/np.max(abs(first_derivative)), label="1st Derivative")
        ax.plot(x, second_derivative/np.max(abs(second_derivative)), label="2nd Derivative")
        ax.plot(x, third_derivative/np.max(abs (third_derivative)), label="3rd Derivative")
        ax.legend()

    derivatives(X,trans,ax1)
    derivatives(X,reflect,ax2)
    derivatives(X,1-(trans+reflect),ax3)
    derivatives(X,absorption,ax4)

    ax1.set_title('Transmittance')
    ax2.set_title('Reflectance')
    ax3.set_title('Absorbance')
    ax4.set_title('Absorption')

    # # Plots
    # ax4.plot(X,trans, label='transmitance', color='blue')
    # ax4.plot(X,reflect, label='reflectance', color='orange')
    # ax4.plot(X,1-(trans+reflect), label='sum', color='green')
    # # ax1.legend()


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


def plot_exciton_fit(data, ax, voltage, Ex, smooth = False, color='red'):
    from scipy.signal import savgol_filter
    # Apply Savitzky-Golay filter
    y = cmf.absorption(data['trans']['R (V)'], data['blank']['R (V)'])
    # y= cmf.reflection(data['trans']['R (V)'], data['blank']['R (V)'])
    EA_data = cmf.EA(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])
    window_size = 11  # Must be odd
    poly_order = 3


    # determine the derivatives
    first_derivative = savgol_filter(y, window_size, poly_order, deriv=1)
    first_derivative /= np.max(np.abs(first_derivative))
    second_derivative = savgol_filter(y, window_size+4, poly_order, deriv=2)
    second_derivative /= np.max(np.abs(second_derivative))
    third_derivative = savgol_filter(y, window_size+8, poly_order, deriv=3)
    third_derivative /= np.max(np.abs(third_derivative))

    # Determine the x axis
    X = cmf.wavelength_to_energy(data['trans']['Digikrom Spectr.:0 (?)'])
    ax.set_xlabel('Energy (eV)')
    exciton_index = np.abs(X - Ex).argmin()


    # Fitting the data
    index_range = slice(max(0, exciton_index-20), min(len(X), exciton_index+20))  # Ensure it's within bounds
    FK_fit = cmf.FK_fit(d_1 = first_derivative[index_range], d_2 = second_derivative[index_range], d_3=third_derivative[index_range], data_to_fit = EA_data[index_range])
    
    # legend name 
    legend = 'Absorption'    

    ax.plot(X, EA_data, label='data to fit')
    # ax.plot(X, first_derivative * np.max(FK_fit), label='d_1')
    # ax.plot(X, second_derivative * np.max(FK_fit), label='d_2')
    ax.plot(X[index_range], FK_fit, label='Fit', color=color)
    ax.legend()
    ax.set_ylabel('Absorption (mOD)')


def plot_data(data, ax, smooth = False, energy=True, legend=0):
    # Get wavelength
    X = data['Digikrom Spectr.:0 (?)']
    ax.set_xlabel('Wavelength (nm)')    
    
    if energy:
        X = cmf.wavelength_to_energy(X)
        ax.set_xlabel('Energy (eV)')

  
    # Gets all of the keys except the wavelength 
    data_keys = list(data.keys())[4:]
    # data_keys = list(data.keys())[1:6]
    data_keys = ['X (V)']
    
    # Plot the data
    if smooth:
        for data_key in data_keys:
            ax.plot(X, cmf.savitzky_golay_smoothing(data[data_key]) ,label=data_key)    
            # ax.semilogy(X, cmf.savitzky_golay_smoothing(data[data_key]) ,label=data_key)  
        # ax.plot(X,data['X (V)'],label = 'X (V)')
        # ax.plot(X,data['R (V)'],label = 'R (V)')
    else:
        for data_key in data_keys:
            ax.plot(X, data[data_key] ,label=f'{data_key}')
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


def plot_CD_Carter(data, ax, energy=True, smoothed=False, smooth=False,color='blue', flip=False):
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

    # print('phased')


    if flip:      
        CD_data = -CD_data


    Y = np.zeros_like(X)

    ax.plot(X,CD_data,color)
    ax.axhline(0,color='black',linewidth=1)
    # ax.plot(X,Y)
    ax.set_ylabel('Circular Dichrosim (mdeg)')
    return CD_data


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
    limit = 2250
    X = data['Time (s)']
    ax.set_xlabel('Time (min)')    
  
    # Gets all of the keys except the time
    data_keys = list(data.keys())[1:]
    print(data_keys)

    for data_key in data_keys[2]:
        ax.plot(X[limit:]/60, data[data_key][limit:]*1e9 ,label=data_key)

    for data_key in data_keys[3:]:
        ax.plot(X[limit:]/60, data[data_key][limit:] ,label=data_key)

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
      
    

    # Getting the different voltage values
    wavelengths = np.array(list(data.keys()))
    wavelengths = sorted(wavelengths)

    # Adds a color bar if true, otherwise defines colors for each plot item
    if colorbar == True:
        colors = color_bar(wavelengths, ax, color_map_name, temp=False, pad=0.10)
    else:
        color_map_func = getattr(plt.cm, color_map_name)
        colors = color_map_func(np.linspace(0, 1, len(wavelengths)))        

    # Plot the data
    i = 0
    for wavelength in wavelengths:
        ax.plot(data[wavelength]['Time'],data[wavelength]['Counts'], linewidth=linewidth, color=colors[i])
        i += 1
    
    ax.set_xlabel('Time (ns)')  
    ax.set_ylabel('TRPL Intensity A.U.')


def plot_TCSPC_Series_Maximum(data, ax, colorbar=True, color_map_name='nipy_spectral'):
    # Get wavelength
    ax.set_xlabel('Time (ns)')    
    
    # Getting the different voltage values
    wavelengths = np.array(list(data.keys()))
    wavelengths = sorted(wavelengths)

    # Adds a color bar if true, otherwise defines colors for each plot item
    if colorbar == True:
        colors = color_bar(wavelengths, ax, color_map_name, temp=False, pad=0.10)
    else:
        color_map_func = getattr(plt.cm, color_map_name)
        colors = color_map_func(np.linspace(0, 1, len(wavelengths)))        


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

    # Adds a color bar if true, otherwise defines colors for each plot item
    if colorbar == True:
        colors = color_bar(wavelengths, ax, color_map_name, temp=False, pad=0.10)
    else:
        color_map_func = getattr(plt.cm, color_map_name)
        colors = color_map_func(np.linspace(0, 1, len(wavelengths)))        

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


def plot_TCSPC_Series_decay_rate_4(data, ax, colorbar=False, color_map_name='nipy_spectral', color='blue'):
    # Get wavelength
    ((ax1, ax2), (ax3, ax4)) = ax
    
    # Getting the different voltage values
    wavelengths = np.array(list(data.keys()))
    wavelengths = sorted(wavelengths)

    # Adds a color bar if true, otherwise defines colors for each plot item
    if colorbar == True:
        colors = color_bar(wavelengths, ax, color_map_name, temp=False, pad=0.10)
    else:
        color_map_func = getattr(plt.cm, color_map_name)
        colors = color_map_func(np.linspace(0, 1, len(wavelengths)))        

    # Plot the data
    i = 0
    decay_rates = []
    for wavelength in wavelengths[:]:
        popt, pcov = cmf.TCSPC_decay_rate(data[wavelength]['Time'],data[wavelength]['Counts'], fit=1)

        decay_intensities = popt[::2]
        total_intensity = np.sum(decay_intensities)
        decay_rates = 1/popt[1::2]
        # X = np.ones(len(decay_rates))*float(wavelength)
        X = float(wavelength)
        # std = np.sqrt(np.diag(pcov))
                
        # decay_rates.append([wavelength,decay_rate1])
        # ax1.scatter(X,decay_rates, color=color)
        # ax2.scatter(X[0], decay_intensities[0]/total_intensity, color=color) # come bachk to this

        ax1.scatter(X, decay_rates[0], color=color)
        ax2.scatter(X, decay_intensities[0]/total_intensity*100, color=color) # come bachk to this
        ax3.scatter(X, decay_rates[1], color=color)
        ax4.scatter(X, decay_intensities[1]/total_intensity*100, color=color) # come bachk to this
    
    # ((ax1, ax2), (ax3, ax4)) = ax
    ax1.set_ylabel('Slow Decay')
    ax3.set_ylabel('Fast Decay')
    ax1.set_title('Decay Rate $(ns^{-1})$')
    # ax.set_ylabel('Decay Rate $(ns^{-1})$')
    # ax.set_xlabel('Wavelength (nm)')  
    return True


def plot_TCSPC_Series_decay_rate(data, ax, colorbar=False, color_map_name='nipy_spectral', color='blue'):
    # Get wavelength
    wavelengths = np.array(list(data.keys()))
    wavelengths = sorted(wavelengths)

    # Adds a color bar if true, otherwise defines colors for each plot item
    if colorbar == True:
        colors = color_bar(wavelengths, ax, color_map_name, temp=False, pad=0.10)
    else:
        color_map_func = getattr(plt.cm, color_map_name)
        colors = color_map_func(np.linspace(0, 1, len(wavelengths)))        

    # Plot the data
    i = 0
    decay_rates = []
    for wavelength in wavelengths[:]:
        popt, pcov = cmf.TCSPC_decay_rate(data[wavelength]['Time'],data[wavelength]['Counts'], fit=1)
        I0, I1, tau, t0 = popt
        print(popt)
        decay_intensities = tau
        decay_rates = tau
        X = float(wavelength)
        # std = np.sqrt(np.diag(pcov))
                
        # decay_rates.append([wavelength,decay_rate1])
        ax.scatter(X, decay_rates, color=color)
        # ax2.scatter(X[0], decay_intensities[0]/total_intensity, color=color) # come bachk to this

        # ax1.scatter(X, decay_rates[0], color=color)
        # ax2.scatter(X, decay_intensities[0]/total_intensity*100, color=color) # come bachk to this
        # ax3.scatter(X, decay_rates[1], color=color)
        # ax4.scatter(X, decay_intensities[1]/total_intensity*100, color=color) # come bachk to this
    
    # # ((ax1, ax2), (ax3, ax4)) = ax
    # ax1.set_ylabel('Slow Decay')
    # ax3.set_ylabel('Fast Decay')
    # ax.set_ylabel('Decay Rate $(ns^{-1})$')
    ax.set_ylabel('Lifetime (ns)')
    ax.set_xlabel('Wavelength (nm)')  
    return True

'''
This plots the data for Photoluminescense, it gives the option to also plot it on a log plot
'''
def plot_PL_FWHM(data, ax, temperature, energy=True, color=True):

    # Get wavelength
    X = data['Wavelength']
    ax.set_ylabel('FWHM (nm)')
    
    if energy:
        X = -cmf.wavelength_to_energy(X)
        ax.set_ylabel('FWHM (eV)')
    
    fwhm, y_range, x_range = cmf.FWHM(X,data['Processed Data'])
    ax.plot(x_range,y_range, label=fwhm, color=color)
    ax.legend()
    
    # ax.set_xlabel('Temperature (K)')


def plot_TCSPC_PL_time(data, ax, colorbar=False, color_map_name='nipy_spectral'):
    # Get wavelength
    ax.set_xlabel('Wavelength (nm)')    
    

    # Getting the different voltage values
    wavelengths = np.array(list(data.keys()))
    wavelengths = sorted(wavelengths)

    # Adds a color bar if true, otherwise defines colors for each plot item
    if colorbar == True:
        colors = color_bar(wavelengths, ax, color_map_name, temp=False, pad=0.10)
    else:
        color_map_func = getattr(plt.cm, color_map_name)
        colors = color_map_func(np.linspace(0, 1, len(wavelengths)))        

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

'''
This plots the data for Photoluminescense, it gives the option to also plot it on a log plot
'''
def plot_impedance_spectroscopy(data, headers):
    files = list(data.keys())
    
    n_subplots = len(headers) - 1
    # Get wavelength
    fig, ax = plt.subplots(1, n_subplots, sharex=True, sharey=False)
    i = 0

    for header in headers[1:]:
        
        ax[i].set_title(header)

        for file in files:
            # print(data[file]['sample'][0])
            X = data[file][headers[0]]
            Y = data[file][header]
            ax[i].loglog(X, Y, label=file)


        i += 1
    plt.legend()
    plt.show()

                
def plot_EA_amplitude(data, ax, colorbar=True, smooth=False, color_map_name='autumn_r', linewidth = 1, energy=True, phased=True,flip = False,text_size=14):
    # Getting the different voltage values
    voltages = np.array(list(data['voltages'].keys()))

    # Adds a color bar if true, otherwise defines colors for each plot item
    if colorbar == True:
        colors = color_bar(cmf.electric_field_kV_per_cm(voltages), ax, color_map_name, temp=False, pad=0.10)
    else:
        color_map_func = getattr(plt.cm, color_map_name)
        colors = color_map_func(np.linspace(0, 1, len(voltages)))        

    # Plot the data
    x_datasets = []
    y_datasets = []
    for i, voltage in enumerate(voltages):
        # Use phase data if true
        if phased:      
            data['voltages'][voltage]['X (V)'] = data['voltages'][voltage]['X (V) Phased']

        if flip:      
            data['voltages'][voltage]['X (V)'] = -data['voltages'][voltage]['X (V)']

        # Get wavelength
        X = data['voltages'][voltage]['Digikrom Spectr.:0 (?)']
        ax.set_xlabel('Wavelength (nm)',fontsize=text_size)    
        
        x_datasets.append(X.values)
        # Energy per wavelength
        if energy:
            X = cmf.wavelength_to_energy(X)
            ax.set_xlabel('Energy (eV)',fontsize=text_size)

        # Calculate the EA signal
        if smooth:
            EA_data = cmf.EA_smooth(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])
        else:
            EA_data = cmf.EA(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])
        
        
        y_datasets.append(EA_data)
        ax.plot(X,EA_data, color=colors[i])


    selected_x, refined_x, matched_y = cmf.select_and_find_nearby_peaks(x_datasets, y_datasets, num_peaks=6, search_window=5, peak_type='both')

    # Plot all curves
    for x, y in zip(x_datasets, y_datasets):
        ax.scatter(selected_x, [y[np.argmin(np.abs(x - sel_x))] for sel_x in selected_x], color='red', zorder=5)
        ax.scatter(refined_x, matched_y, color='black', zorder=5)

    ax.tick_params(axis='both',which='major', labelsize=12)
    ax.axhline(y=0,color='k',linewidth=0.8)

    return selected_x, refined_x, matched_y


def plot_peak_amplitude(data, ax, refined_x, matched_y, energy=True, color_map_name='plasma_r'):
    # import numpy as np
    # import matplotlib.pyplot as plt
    # import colton_math_functions as cmf  # assuming this is where electric_field_kV_per_cm is defined

    voltages = np.array(list(data['voltages'].keys()))
    electric_field = cmf.electric_field_kV_per_cm(voltages)

    color_map_func = getattr(plt.cm, color_map_name)
    colors = color_map_func(np.linspace(0, 1, len(voltages)))


    # print(matched_y, len(matched_y))
    # print(voltages, len(voltages))
    # for j in range(len(matched_y)):

    for i, y_values in enumerate(matched_y):
        x_average = np.mean(refined_x[i])
        print(y_values, len(y_values))
        # for i, voltage in enumerate(voltages):
        #     y_values = np.abs(y_values)
        #     valid = y_values > 0  # Avoid log(0)

        #     if np.sum(valid) < 2:
        #         continue  # Need at least 2 points to fit

        #     ef_valid = electric_field[valid]
        #     y_valid = y_values[valid]

        #     log_ef = np.log(ef_valid)
        #     log_y = np.log(y_valid)

        #     p, cov = np.polyfit(log_ef, log_y, 1, cov=True)
        #     slope, intercept = p
        #     slope_err, _ = np.sqrt(np.diag(cov))

        #     if slope_err < 0.2:
        #         slope_sign = np.sign(y_values[0])  # original sign
        #         peak_label = f'{x_average:.2f} eV' if energy else f'{x_average:.0f} nm'
        #         ax.loglog(electric_field, y_values, color=colors[i],
        #                 label=f'{peak_label} (slope = {slope * slope_sign:.2f})')
                

        p, cov = np.polyfit(np.log(electric_field), np.log(np.abs(y_values)), 1, cov=True)
        slope, intercept = p
        slope_err, intercept_err = np.sqrt(np.diag(cov))
        if slope_err < 0.2:
            print('Slope: {:.2f} ± {:.2f}'.format(slope, slope_err))
            ax.loglog(cmf.electric_field_kV_per_cm(voltages),y_values, color=colors[i], label='{:.2f} eV (slope = {:.2f})'.format(x_average, slope*np.sign(y_values[0])))


    ax.legend()
    ax.set_xlabel('Electric Field (kV/cm)')
    ax.set_ylabel('Peak Amplitude (a.u.)')


def plot_EA_amplitude_all(data, ax, colorbar=True, smooth=False, color_map_name='autumn_r', linewidth = 1, energy=True, phased=True,flip = False,text_size=14):
    # Getting the different voltage values
    voltages = np.array(list(data['voltages'].keys()))

    # Adds a color bar if true, otherwise defines colors for each plot item
    if colorbar == True:
        colors = color_bar(cmf.electric_field_kV_per_cm(voltages), ax, color_map_name, temp=False, pad=0.10)
    else:
        color_map_func = getattr(plt.cm, color_map_name)
        colors = color_map_func(np.linspace(0, 1, len(voltages)))        

    # Plot the data

    for i, voltage in enumerate(voltages):
        # Use phase data if true
        if phased:      
            data['voltages'][voltage]['X (V)'] = data['voltages'][voltage]['X (V) Phased']

        if flip:      
            data['voltages'][voltage]['X (V)'] = -data['voltages'][voltage]['X (V)']

        # Get wavelength
        X = data['voltages'][voltage]['Digikrom Spectr.:0 (?)']
        ax.set_xlabel('Wavelength (nm)',fontsize=text_size)    
        
        # Energy per wavelength
        if energy:
            X = cmf.wavelength_to_energy(X)
            ax.set_xlabel('Energy (eV)',fontsize=text_size)

        # Calculate the EA signal
        if smooth:
            EA_data = cmf.EA_smooth(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])
        else:
            EA_data = cmf.EA(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])
        
        
        ax.plot(X,EA_data, color=colors[i])
        data['voltages'][voltage]['EA'] = EA_data

    size = len(EA_data)
    EA_data_array = np.zeros([len(voltages), size])
    for i, voltage in enumerate(voltages):
        EA_data_array[i,:] = np.array(data['voltages'][voltage]['EA'])
    
        # print(EA_data_array[:,0])

    electric_field = cmf.electric_field_kV_per_cm(voltages)
    slopes = np.zeros(size)
    slope_errs = np.zeros(size)
    for i in range(size):  
        p, cov = np.polyfit(np.log(electric_field), np.log(np.abs(EA_data_array[:,i])), 1, cov=True)
        slopes[i], intercept = p
        slope_errs[i], intercept_err = np.sqrt(np.diag(cov))


    # Scatter plot with error bars
    ax.errorbar(X, slopes, yerr=slope_errs, fmt='o', capsize=0.25, label='Data points')
    ax.axhline(y=2, color='black', linestyle='-.', linewidth=0.5)


        # if slope_err < 0.2:
        #     print('Slope: {:.2f} ± {:.2f}'.format(slope, slope_err))
        #     ax.loglog(cmf.electric_field_kV_per_cm(voltages),y_values, color=colors[i], label='{:.2f} eV (slope = {:.2f})'.format(x_average, slope*np.sign(y_values[0])))



    # # color_map_func = getattr(plt.cm, color_map_name)
    # # colors = color_map_func(np.linspace(0, 1, len(voltages)))


    # # print(matched_y, len(matched_y))
    # # print(voltages, len(voltages))
    # # for j in range(len(matched_y)):

    # for i in len:
    #     x_average = np.mean(refined_x[i])
    #     print(y_values, len(y_values))
         

    #     p, cov = np.polyfit(np.log(electric_field), np.log(np.abs(y_values)), 1, cov=True)
    #     slope, intercept = p
    #     slope_err, intercept_err = np.sqrt(np.diag(cov))
    #     if slope_err < 0.2:
    #         print('Slope: {:.2f} ± {:.2f}'.format(slope, slope_err))
    #         ax.loglog(cmf.electric_field_kV_per_cm(voltages),y_values, color=colors[i], label='{:.2f} eV (slope = {:.2f})'.format(x_average, slope*np.sign(y_values[0])))


    return data


def plot_PL_temp_series(data, ax, colorbar=True, color_map_name='cool', energy=True, smooth=False, log=False):
    # Create a color bar
    temperatures = np.array(list(data.keys()))
    # colors = color_bar(temperatures, ax, color_map_name, temp=True)
    if colorbar == True:
        colors = color_bar(temperatures, ax, color_map_name, temp=True)
    else:
        color_map_func = getattr(plt.cm, color_map_name)
        colors = color_map_func(np.linspace(0, 1, len(temperatures)))

    # Plot the data
    for i, temp in enumerate(temperatures):
        X = data[temp]['Wavelength']
        Y = data[temp]['Processed Data']
        
        # Energy if desired
        ax.set_xlabel('Wavelength (nm)')    
        if energy:
            X = cmf.wavelength_to_energy(X)
            ax.set_xlabel('Energy (eV)')    


        # FWHM not implemented yet
        # print(cmf.FWHM(X,data['Processed Data']))

        # smooth the data?
        if smooth:
            # # Specify the x-values you want to connect with a straight line
            # x1 = 860
            # x2 = 890

            # # Find the indices in X closest to x1 and x2
            # i1 = np.argmin(np.abs(X - x1))
            # i2 = np.argmin(np.abs(X - x2))

            # # Create straight line values between Y[i1] and Y[i2]
            # x_segment = X[i1:i2 + 1]
            # y_start = Y[i1]
            # y_end = Y[i2]
            # y_segment = np.linspace(y_start, y_end, len(x_segment))
            # Y[i1:i2 + 1] = y_segment

            Y = cmf.savitzky_golay_smoothing(y=Y)
            # print('smooth has not been implemented yet')

        # plot the data
        if log == True:
            ax.semilogy(X, Y, color=colors[i])
        else:
            ax.plot(X, Y, color=colors[i])

        

    ax.set_ylabel('PL Intensity A.U.')




