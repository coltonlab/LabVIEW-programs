"""
Script Name: read_colton_files (rcf)
Author: Carter Shirley
Date: February 14, 2024
Description: You input the row number that is in the file "C:/Data/All Scan Notes.xlsx" and it will look up the file name and import the 
data and return back a dataframe with the raw data and the phased data.
"""

import pandas as pd
import numpy as np
from public.colton_math_functions import phase_data


''' 
get_filename is a function that opens All Scan Notes.xlsx and looks for the file names and dates that are listed in there.
'''
def get_filename(excel_file_row):    
    offset = -2
    excel_file_row += offset

    # excel_filename = '//2.coltonlab.byu.edu/C$/Data/All Scan Notes New.xlsx'
    excel_filename = 'C:/Data/All Scan Notes New.xlsx'
    all_scan_notes = pd.read_excel(excel_filename)

    date = str(all_scan_notes['Date'][excel_file_row])[:10]
    sample = str(all_scan_notes['Sample'][excel_file_row])
    # scan_type = str(all_scan_notes['Type of Scan'][excel_file_row])
    # temperature = str(all_scan_notes['Temp (K)'][excel_file_row])
    file = str(all_scan_notes['File'][excel_file_row])

    if date[:4] != '2025':
        subfolder = f'Data/{date[:4]}'
    else:
        subfolder = 'Data'


    # file_path  = f'//2.coltonlab.byu.edu/C$/{subfolder}/{date}/{file}'
    file_path = f"C:/{subfolder}/{date}/{file}"

    return file_path, sample



'''
This function replaces "Check Status.vi" for -Check Status.vi- to get ride of an error. Currently only used for the voltage series data
'''
def delete_line(filename, line):
    with open(filename, 'r+') as file:
        lines = file.readlines()
        lines[line] = '-Check Status.vi- method not implemented for this class.\n' # Replace the content of line
        file.seek(0)
        file.writelines(lines)



'''
read_trans_data reads in the data and phases in accordance to the way the data is outputted.
'''
def read_trans_data(excel_row, sample = False):
    filename, sample_name = get_filename(excel_row)
    print(filename)
    # read in the data and skip the starting lines and ending lines
    row_skip = range(0,15) # The number of rows to skip is different for the data
    data = pd.read_csv(filename, engine='python' ,skiprows=row_skip, skipfooter=3, sep='\t', dtype=float)

    # Phases the data and makes another column with the phased data 
    data = phase_data(data)

    

    if sample:
        # Gives the same_name of the data 
        return data, sample_name

    return data



'''
read_voltage_series_data reads in the data and phases all off the voltages at once. It then seperates all of the voltages into a different data frames
and outputs them all in a dictionary with the voltage as the dictionary keys.
'''
def read_voltage_series_data(excel_row, sample = False):
    filename, sample_name = get_filename(excel_row)
    
    # Removes the error by having the "Check Status.vi" be replaced
    delete_line(filename, 5)

    # read in the data and skip the starting lines and ending lines
    row_skip = range(0,14)
    
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

    print(data_by_voltage)
    if sample:
        # Gives the same_name of the data 
        return data_by_voltage, sample_name
    
    # Returns the data by voltage and a list of voltages to unpack the dictionary
    return data_by_voltage



'''
read_lockin_Fluke_data reads in the data and phases in accordance to the way the data is outputted.
'''
def read_lockin_fluke_data(excel_row, sample = False):
    filename, sample_name = get_filename(excel_row)

    # read in the data and skip the starting lines and ending lines
    row_skip = range(0,14) # The number of rows to skip is different for the data
    data = pd.read_csv(filename, engine='python' ,skiprows=row_skip, skipfooter=3, sep='\t', dtype=float)

    # Phases the data and makes another column with the phased data 
    data = phase_data(data, x_name='X830 (V)', y_name='Y830 (V)')

    
    if sample:
        # Gives the same_name of the data 
        return data, sample_name

    return data



'''
read_lockin_keithley_data reads in the data and phases in accordance to the way the data is outputted.
'''
def read_lockin_keithley_data(excel_row, sample = False):
    filename, sample_name = get_filename(excel_row)

    # read in the data and skip the starting lines and ending lines
    row_skip = range(0,16) # The number of rows to skip is different for the data
    data = pd.read_csv(filename, engine='python' ,skiprows=row_skip, skipfooter=3, sep='\t', dtype=float)

    # Phases the data and makes another column with the phased data 
    data = phase_data(data, x_name='X830 (V)', y_name='Y830 (V)')


    if sample:
        # Gives the same_name of the data 
        return data, sample_name

    return data



'''
read_CCD data reads in the data which is to be understood as a raser scan.
'''
def read_CCD_data(excel_row, sample = False):
    filename, sample_name = get_filename(excel_row)

    # read in the data and skip the starting lines and ending lines
    row_skip = range(0,10) # The number of rows to skip is different for the data
    data = pd.read_csv(filename, engine='python' ,skiprows=row_skip, skipfooter=3, sep='\t', dtype=float)


    if sample:
        # Gives the same_name of the data 
        return data, sample_name
    
    print(filename)

    return data



'''
read_PMT data reads in the data that the photon counter reads out.
'''
def read_PMT_data(excel_row, sample = False):
    filename, sample_name = get_filename(excel_row)

    # read in the data and skip the starting lines and ending lines
    row_skip = range(0,9) # The number of rows to skip is different for the data
    data = pd.read_csv(filename, engine='python' ,skiprows=row_skip, skipfooter=3, sep='\t', dtype=float)


    if sample:
        # Gives the same_name of the data 
        return data, sample_name
    
    print(filename)

    return data



'''
read_PMT data reads in the data that the photon counter reads out.
'''
def read_PMT_data(excel_row, sample = False):
    filename, sample_name = get_filename(excel_row)

    # read in the data and skip the starting lines and ending lines
    row_skip = range(0,9) # The number of rows to skip is different for the data
    data = pd.read_csv(filename, engine='python' ,skiprows=row_skip, skipfooter=3, sep='\t', dtype=float)


    if sample:
        # Gives the same_name of the data 
        return data, sample_name
    
    print(filename)

    return data



'''
read_PMT data reads in the data that the photon counter reads out.
'''
def read_impedance_data(excel_row, headers):
    filename, sample_name = get_filename(excel_row)

    # read in the data and skip the starting lines and ending lines
    row_skip = range(0,3) # The number of rows to skip is different for the data
    data = pd.read_csv(filename, engine='python' ,skiprows=row_skip, skipfooter=0, dtype=float, names=headers)
    # data['sample'] = sample_name
    
    print(filename)

    return data













