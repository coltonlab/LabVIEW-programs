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
import read_colton_files as rcf

def get_filename(excel_file_row):    
    offset = 2
    excel_file_row += offset

    excel_filename = '//2.coltonlab.byu.edu/C$/Data/All Scan Notes.xlsx'
    all_scan_notes = pd.read_excel(excel_filename)



    date = str(all_scan_notes['Date'][excel_file_row])[:10]
    # sample = str(all_scan_notes['Sample'][excel_file_row])
    # scan_type = str(all_scan_notes['Type of Scan'][excel_file_row])
    # temp = str(all_scan_notes['Temp (K)'][excel_file_row])
    file = str(all_scan_notes['File'][excel_file_row])

    file_path  = f'//2.coltonlab.byu.edu/C$/Data/{date}/{file}'
    # file_path = f"C:/Data/{date}/{file}"

    return file_path

data = rcf.read_trans_data(get_filename(376))
print(data)




