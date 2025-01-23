import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np

# def average_impedance(data, files, weight):
#     average_data = 0
#     for index, file in enumerate(files):
#         )
    

def impedance_spectroscopy_template():
    # Dictionary that holds all of the data with input trans
    data = {}

    # headers=['F (Hz)','Z','R','L','C']
    headers=['F (Hz)','Z','R','C']
    # files = range(1482, 1490)
    files = [1505,1506]
    files = range(1507,1511)
    # files = range(1474, 1480)

    for file in files:
        data[file] = rcf.read_impedance_data(file, headers=headers)
        # print(file)

    weight = [30,30,10]
    # average_impedance(data, files, weight)

    pcg.plot_impedance_spectroscopy(data, headers)


impedance_spectroscopy_template()