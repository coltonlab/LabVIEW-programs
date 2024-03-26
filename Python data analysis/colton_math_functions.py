'''
This is a conveniant spot to put all of the mathematical functions that the colton group uses. 
'''
import numpy as np
from scipy.signal import savgol_filter
import scipy.special as sps



def EA(voltage_X, trans):
    '''Calculates the EA signal with the input ea data and transmission data '''
    return -np.log(1 + voltage_X.values/trans.values)

def EA_smooth(voltage_X, trans):
    '''Calculates the EA signal with the input ea data and transmission data '''
    trans_smooth = savitzky_golay_smoothing(trans.values)
    voltage_X_smooth = savitzky_golay_smoothing(voltage_X.values)
    return -np.log(1 + voltage_X_smooth/trans_smooth)


def absorption(trans, blank):
    '''Calculates the absorption given a blank and transmission data '''
    return -np.log10(trans.values/blank.values)

def absorption_smooth(trans, blank):
    '''Calculates the absorption given a blank and transmission data '''
    trans_smooth = savitzky_golay_smoothing(trans.values)
    blank_smooth = savitzky_golay_smoothing(blank.values)
    return -np.log10(trans_smooth/blank_smooth)


def circular_dichrosim(AC,DC):
    '''Calculate CD in millidegrees'''
    return (-32982/(np.log(10)*sps.j1(np.pi/2)))*(AC/DC)


def wavelength_to_energy(wavelength): 
    '''Converts wavelength to energy'''
    return 1239.84193/wavelength.values


def savitzky_golay_smoothing(y, window_length=11, polyorder=3):
    """
    Apply Savitzky-Golay smoothing to the given data.

    Parameters:
        y (array-like): Dependent variable (e.g., measured values).
        window_length (int): Length of the window over which the polynomial is fit.
        polyorder (int): Order of the polynomial that is fit to the data within each window.

    Returns:
        array-like: Smoothed data.
    """
    smoothed_y = savgol_filter(y, window_length, polyorder)
    return smoothed_y
























