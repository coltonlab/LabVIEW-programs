from pandas import DataFrame
import numpy as np
import public.colton_math_functions as cmf


def Export_EA_series_data(data, filename, smooth_abs=False, smooth_ea=False, remote=False, flip=False, phased=False): 
    """
    Exports EA data to a CSV file.
    Parameters:
    - data: Dictionary containing the data to be exported.
    - filename: Name of the file to save the data.
    - smooth_ABS: Boolean indicating whether to smooth the absorption data.
    - smooth_EA: Boolean indicating whether to smooth the EA data.
    - remote: Boolean indicating whether to save the file remotely.
    - flip: Boolean indicating whether to flip the voltage data.
    - phased: Boolean indicating whether to use phased data.
    """
    # create a dictionary to hold the EA calculations
    EA_calculations = {}
    EA_calculations['Energy (eV)'] = cmf.wavelength_to_energy(data['trans']['Digikrom Spectr.:0 (?)'])

    # Getting the different voltage values
    voltages = np.array(sorted(list(data['voltages'].keys())))
    electric_field = cmf.electric_field_kV_per_cm(voltages)

    # Calculate the absorption signal
    if smooth_abs:
        EA_calculations['Absorption (OD)'] = cmf.absorption_smooth(data['trans']['R (V)'], data['blank']['R (V)'])    
    else:
        EA_calculations['Absorption (OD)'] = cmf.absorption(data['trans']['R (V)'], data['blank']['R (V)'])

    # Plot the data
    for i, voltage in enumerate(voltages):
        # Use phase data if true
        if phased:      
            data['voltages'][voltage]['X (V)'] = data['voltages'][voltage]['X (V) Phased']

        # Flip the data if true
        if flip:      
            data['voltages'][voltage]['X (V)'] = -data['voltages'][voltage]['X (V)']

        # Calculate the EA signal
        if smooth_ea:
            EA_calculations[f'EA {electric_field:.0f} kV/cm (mOD)'] = cmf.EA_smooth(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])
        else:
            EA_calculations[f'EA {electric_field:.0f} kV/cm (mOD)'] = cmf.EA(data['voltages'][voltage]['X (V)'], data['trans']['R (V)'])
        
    # Add the electric field values    
    df = DataFrame(EA_calculations)

    # Export to CSV
    if remote:
        df.to_csv(f"'\\2.coltonlab.byu.edu\\C$\\Data\\Compiled Data\\{filename}", index=False)
    else:
        df.to_csv(f"C:\\Data\\Compiled Data\\{filename}", index=False)


def Export_ABS_temp_data(data, filename, smooth=False, remote=False):
# create a dictionary to hold the EA calculations
    ABS_calculations = {}
    ABS_calculations['Energy (eV)'] = cmf.wavelength_to_energy(data['trans']['Digikrom Spectr.:0 (?)'])

    # Getting the different voltage values
    temperatures = np.array(list(data['trans'].keys()))


    # calculate the data
    for i, temp in enumerate(temperatures):
        # Calculate the absorption signal
        if smooth:
            ABS_calculations[f'Absorption (OD) {temp}K'] = cmf.absorption_smooth(data['trans'][temp]['R (V)'], data['blank']['R (V)'])
        else:
            ABS_calculations[f'Absorption (OD) {temp}K'] = cmf.absorption(data['trans'][temp]['R (V)'], data['blank']['R (V)'])

        
    # Add the electric field values    
    df = DataFrame(ABS_calculations)

    # Export to CSV
    if remote:
        df.to_csv(f"'\\2.coltonlab.byu.edu\\C$\\Data\\Compiled Data\\{filename}", index=False)
    else:
        df.to_csv(f"C:\\Data\\Compiled Data\\{filename}", index=False)




def Export_EA_temp_data(data, filename, smooth=False, remote=False, flip=False, phased=False):
    # create a dictionary to hold the EA calculations
    EA_calculations = {}
    EA_calculations['Energy (eV)'] = cmf.wavelength_to_energy(data['trans']['Digikrom Spectr.:0 (?)'])

    # Getting the different voltage values
    temperatures = np.array(list(data['trans'].keys()))

    # Plot the data
    for i, temp in enumerate(temperatures):
        if phased:      
            data['voltages'][temp]['X (V)'] = data['voltages'][temp]['X (V) Phased']

        if flip:      
            data['voltages'][temp]['X (V)'] = -data['voltages'][temp]['X (V)']

        # Calculate the EA signal
        if smooth:
            EA_calculations[f'EA (mOD) {temp}K'] = cmf.EA_smooth(data['voltages'][temp]['X (V)'], data['trans'][temp]['R (V)'])
        else:
            EA_calculations[f'EA (mOD) {temp}K'] = cmf.EA(data['voltages'][temp]['X (V)'], data['trans'][temp]['R (V)'])
        
    # Add the electric field values    
    df = DataFrame(EA_calculations)

    # Export to CSV
    if remote:
        df.to_csv(f"'\\2.coltonlab.byu.edu\\C$\\Data\\Compiled Data\\{filename}", index=False)
    else:
        df.to_csv(f"C:\\Data\\Compiled Data\\{filename}", index=False)



def Export_CD_temp_data(data, filename, smooth=False, remote=False, flip=False, phased=False):
    # create a dictionary to hold the EA calculations
    CD_calculations = {}
    CD_calculations['Energy (eV)'] = cmf.wavelength_to_energy(data['trans']['Digikrom Spectr.:0 (?)'])

    # Getting the different voltage values
    temperatures = np.array(list(data['trans'].keys()))

    # Plot the data
    for i, temp in enumerate(temperatures):
        if phased:      
            data['voltages'][temp]['X (V)'] = data['voltages'][temp]['X (V) Phased']

        if flip:      
            data['voltages'][temp]['X (V)'] = -data['voltages'][temp]['X (V)']

        # Calculate the EA signal
        if smooth:
            CD_calculations[f'CD (mdeg) {temp}K'] = cmf.circular_dichrosim_smooth(data['CD'][temp]['X (V)'], data['trans'][temp]['R (V)'])
        else:
            CD_calculations[f'CD (mdeg) {temp}K'] = cmf.circular_dichrosim(data['CD'][temp]['X (V)'], data['trans'][temp]['R (V)'])
        
    # Add the electric field values    
    df = DataFrame(CD_calculations)

    # Export to CSV
    if remote:
        df.to_csv(f"'\\2.coltonlab.byu.edu\\C$\\Data\\Compiled Data\\{filename}", index=False)
    else:
        df.to_csv(f"C:\\Data\\Compiled Data\\{filename}", index=False)



