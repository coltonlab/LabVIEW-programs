'''
This is a conveniant spot to put all of the mathematical functions that the colton group uses. 
'''
import numpy as np

''' calculates the EA signal with the input ea data and transmission data '''
def EA(voltage_X, trans):
    return -np.log(1 + voltage_X.values/trans.values)


''' calculates the absorption given a blank and transmission data '''
def absorption(trans, blank):
    return -np.log(trans.values/blank.values)


def wavelength_to_energy(wavelength): 
    return 1239.84193/wavelength.values

























