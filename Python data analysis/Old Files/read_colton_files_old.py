"""
Script Name: read_colton_files (rcf)
Author: Carter Shirley
Date: February 14, 2024
Description: You input a filename (voltage series or trans/single voltage) and will return back a dataframe with the raw data and the 
phased data. the data can be called by using the name of the headers. The voltage series function will make a dictionary where you can 
input the voltage (integer) and get the dataframe for that voltage.
"""

import pandas as pd
import numpy as np

def delete_line(filename, line):
    ''' This function replaces "Check Status.vi" for -Check Status.vi- to get ride of an error. Currently only used for the voltage series data''' 
    with open(filename, 'r+') as file:
        lines = file.readlines()
        lines[line] = '-Check Status.vi- method not implemented for this class.\n' # Replace the content of line
        file.seek(0)
        file.writelines(lines)

def phase_data(data):
    ''' This program uses a for loop and finds the min value for Y in 10 iterations, it then does another 10 at a smaller step size '''
    X = data['X (V)']
    Y = data['Y (V)']

    # Fixes any offsets
    X -= np.mean(data['X (V)'])
    Y -= np.mean(data['Y (V)'])

    # Calculate Y values for each angle
    min_y = float('inf')
    min_angle = 0
    BC = 3.15/2 # boundry conditions

    # This double four loop allows us to go through 60 values of Y to get an accuracy within 1.8e-4 degrees.
    for i in range(5): # Increase this number to increase your tolerance. Change this number if you want 1.8e-(n-2) order of accuracy
        angles = np.linspace(min_angle - BC , min_angle + BC, 10)  # Range from -pi/2 to pi/2 radians

        # Looking for the smallest abs value of Y with in 10 data points 
        for angle in angles:
            y_rotated = X * np.sin(angle) + Y * np.cos(angle)
            min_y_angle = np.sum(np.abs(y_rotated))

            # Keeps the smallest angle
            if min_y_angle < min_y:
                min_y = min_y_angle
                min_angle = angle

        # Makes BC smaller for a better step size
        BC = BC/10

    data['X (V) Phased'] = X * np.cos(min_angle) - Y * np.sin(min_angle)
    data['Y (V) Phased'] = X * np.sin(min_angle) + Y * np.cos(min_angle)

    return data

def phase_CD_data(data):
    '''Phases CD data, because the columns are called something different'''
    X = data['X830 (V)']
    Y = data['Y830 (V)']

    # Calculate Y values for each angle
    min_y = float('inf')
    min_angle = 0
    BC = 3.15/2 # boundry conditions

    # This double four loop allows us to go through 60 values of Y to get an accuracy within 1.8e-4 degrees.
    for i in range(6): # Increase this number to increase your tolerance. Change this number if you want 1.8e-(n-2) order of accuracy
        angles = np.linspace(min_angle - BC , min_angle + BC, 10)  # Range from -pi/2 to pi/2 radians

        # Looking for the smallest abs value of Y with in 10 data points 
        for angle in angles:
            y_rotated = X * np.sin(angle) + Y * np.cos(angle)
            min_y_angle = np.sum(np.abs(y_rotated))

            # Keeps the smallest angle
            if min_y_angle < min_y:
                min_y = min_y_angle
                min_angle = angle

        # Makes BC smaller for a better step size
        BC = BC/10

    data['X (V) Phased'] = X * np.cos(min_angle) - Y * np.sin(min_angle)
    data['Y (V) Phased'] = X * np.sin(min_angle) + Y * np.cos(min_angle)

    return data


def read_trans_data(filename, header = False):
    ''' read_trans_data reads in the data and places it in a data frame. The data can be called by the name of the header '''
    # read in the data and skip the starting lines and ending lines
    row_skip = range(0,14) # The number of rows to skip is different for the 
    data = pd.read_csv(filename, engine='python' ,skiprows=row_skip, skipfooter=3, sep='\t', dtype=float)

    # Phases the data and makes another column with the phased data 
    data = phase_data(data)

    # This returns headers along with the data i.e. [Digikrom Spectr.:0 (?), X (V), Y (V), R (V), X (V) Phased, Y (V) Phased]
    if header == True:
        # Gives the headers in the data 
        headers = list(data.columns)

        return data, headers

    return data

def read_voltage_series_data(filename):
    ''' read_voltage_series_data reads in the data and exports the phased dataframe splitted into individual voltages in a dictionary'''
    # Removes the error by having the "Check Status.vi" be replaced
    delete_line(filename, 5)

    # read in the data and skip the starting lines and ending lines
    row_skip = range(0,13)
    
    # reads in the actual data into a dataframe
    data = pd.read_csv(filename, engine='python' ,skiprows=row_skip, skipfooter=3, sep='\t')

    # Phases the data and makes another column with the phased data 
    data = phase_data(data)

    # Finds all of the voltages that were scanned over in the data
    voltages = np.int16(np.unique(data['O-scope 2024B:0 (?)']))

    # Initialize an empty dictionary
    data_by_voltage = {}

    # Making a dictionary variable for each voltage
    for voltage in voltages:
        data_by_voltage[voltage] = data[data['O-scope 2024B:0 (?)'].isin([voltage])]
    
    # Returns the data by voltage and a list of voltages to unpack the dictionary
    return data_by_voltage

def read_CD_data(filename):
    '''Reads in the data and exports the phased dataframe'''

    # read in the data and skip the starting lines and ending lines
    row_skip = 16
    
    # reads in the actual data into a dataframe
    data = pd.read_csv(filename, engine='python' ,skiprows=row_skip, skipfooter=3, sep='\t')

    # Phases the data and makes another column with the phased data 
    data = phase_CD_data(data)
    
    # Returns the data
    return data

























