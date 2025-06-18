import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np


def EA_temperature_series_template(): # Needs to be updated
    # date where the data is stored
    # file_path = 'C:/Data/2024-09-23/'

    data = {}
    data['trans'] = {}
    data['voltages'] = {}

    # blank_file = file_path + 'Blank 2-MePESI 300-700nm 295K.xls'
    data['blank'] = rcf.read_trans_data(1116) 
    
    # go through the temperatures
    temperatures = [16,50,100,150,200,250]
    
    volt_file_list = [1121,1124,1127,1128,1131,1132]
    trans_file_list = [1120,1125,1126,1129,1130,1133]

    for i in range(len(temperatures)):
        data['trans'][temperatures[i]] = rcf.read_trans_data(trans_file_list[i])
        data['voltages'][temperatures[i]] = rcf.read_trans_data(volt_file_list[i])

    # for temp in temperatures:
    #     trans_file = file_path + 'Trans 2-MePESI 300-700nm {}K.xls'.format(temp)
    #     data['trans'][temp] = rcf.read_trans_data(trans_file)

    #     voltage_file = file_path + '300V EA 2-MePESI 300-700nm {}K.xls'.format(temp)
    #     data['voltages'][temp] = rcf.read_trans_data(voltage_file)


    # Create the first plot with the first y-axis
    fig1, ax1 = plt.subplots()
    pcg.plot_EA_temp_series(data, ax=ax1, color_map_name='rainbow')


    fig2, ax2 = plt.subplots()
    pcg.plot_ABS_temp_series(data, ax=ax2, color_map_name='rainbow')


    # plt.savefig(fig_name, format='png', dpi=300)

    plt.show()
"""NEAPbBr samples"""
def rac_1_1_NPB_temp_series(): 
    data = {}
    data['trans'] = {}
    data['voltages'] = {}

    # blank_file = file_path + 'Blank 2-MePESI 300-700nm 295K.xls'
    data['blank'] = rcf.read_trans_data_old(1735) 
    
    # go through the temperatures
    temperatures = [300,250,200,150,100,50,17]
    
    trans_file_list = [1736,1739,1740,1743,1745,1747,1749]
    volt_file_list = [1737,1738,1741,1742,1744,1746,1748]

    for i, temp in enumerate(temperatures):
        print(temp,i)
        data['trans'][temp] = rcf.read_trans_data_old(trans_file_list[i])
        data['voltages'][temp] = rcf.read_trans_data_old(volt_file_list[i])
    

    # Create the first plot with the first y-axis
    fig1, ax1 = plt.subplots()
    pcg.plot_EA_temp_series(data, ax=ax1, color_map_name='rainbow',smooth=False,energy=False, phased=False)

    fig2, ax2 = plt.subplots()
    pcg.plot_ABS_temp_series(data, ax=ax2, color_map_name='rainbow',smooth=False,energy=False)


    # plt.savefig(fig_name, format='png', dpi=300)

    plt.show()
rac_1_1_NPB_temp_series()

"""NEAPbBr samples"""
def S_1_1_NPB_temp_series(): 
    data = {}
    data['trans'] = {}
    data['voltages'] = {}

    # blank_file = file_path + 'Blank 2-MePESI 300-700nm 295K.xls'
    data['blank'] = rcf.read_trans_data_old(1692) 
    
    # go through the temperatures
    temperatures = [16,50,100,150,200,250,300]
    
    trans_file_list = [1693,1694,1695,1696,1697,1698,1699]
    volt_file_list = [1700,1701,1702,1703,1704,1705,1706]

    for i, temp in enumerate(temperatures):
        print(temp,i)
        data['trans'][temp] = rcf.read_trans_data_old(trans_file_list[i])
        data['voltages'][temp] = rcf.read_trans_data_old(volt_file_list[i])
    

    # Create the first plot with the first y-axis
    fig1, ax1 = plt.subplots()
    pcg.plot_EA_temp_series(data, ax=ax1, color_map_name='rainbow',smooth=False,energy=False, phased=False)

    fig2, ax2 = plt.subplots()
    pcg.plot_ABS_temp_series(data, ax=ax2, color_map_name='rainbow',smooth=False,energy=False)


    # plt.savefig(fig_name, format='png', dpi=300)

    plt.show()

"""NEAPbBr samples"""
def NEAPbBr(): # Needs to be updated
    # date where the data is stored
    # file_path = 'C:/Data/2024-09-23/'

    data = {}
    data['trans'] = {}
    data['voltages'] = {}

    # blank_file = file_path + 'Blank 2-MePESI 300-700nm 295K.xls'
    data['blank'] = rcf.read_trans_data_old(1649) 
    
    # go through the temperatures
    temperatures = [16,50,100,150,200,250,300]
    
    volt_file_list = [1652,1653,1656,1657,1660,1661,1664]
    trans_file_list = [1651,1654,1655,1658,1659,1662,1663]

    for i in range(len(temperatures)):
        data['trans'][temperatures[i]] = rcf.read_trans_data_old(trans_file_list[i])
        data['voltages'][temperatures[i]] = rcf.read_trans_data_old(volt_file_list[i])
    
    X = data['blank']['Digikrom Spectr.:0 (?)'].to_numpy()
    
    # data['voltages'][16]['X (V) Phased'][:50] += 1e-12*np.exp(-X[:50]/100) + 1e-12
    # data['voltages'][16]['X (V) Phased'][:50] += 8.726390E-13

    # Create the first plot with the first y-axis
    fig1, ax1 = plt.subplots()
    pcg.plot_EA_temp_series(data, ax=ax1, color_map_name='rainbow',smooth=False,energy=False)


    fig2, ax2 = plt.subplots()
    pcg.plot_ABS_temp_series(data, ax=ax2, color_map_name='rainbow',smooth=False,energy=False)


    # plt.savefig(fig_name, format='png', dpi=300)

    plt.show()
# NEAPbBr()

"""Kentucky samples (CHDA, CHMDA, 4-AMP, 4-AMPY)"""
def CHDA_temp_series(): # Needs to be updated
    # date where the data is stored

    data = {}
    data['trans'] = {}
    data['voltages'] = {}

    # blank_file = file_path + 'Blank 2-MePESI 300-700nm 295K.xls'
    data['blank'] = rcf.read_trans_data(1158) 
    
    # go through the temperatures
    temperatures = [16,50,100,150,200,250,295]
    
    volt_file_list = [1148,1149,1150,1151,1152,1153,1157]
    trans_file_list = [1137,1138,1139,1140,1141,1142,1143]

    for i in range(len(temperatures)):
        data['trans'][temperatures[i]] = rcf.read_trans_data(trans_file_list[i])
        data['voltages'][temperatures[i]] = rcf.read_trans_data(volt_file_list[i])
        data['voltages'][temperatures[i]]['X (V) Phased'] *= -1

    # for temp in temperatures:
    #     trans_file = file_path + 'Trans 2-MePESI 300-700nm {}K.xls'.format(temp)
    #     data['trans'][temp] = rcf.read_trans_data(trans_file)

    #     voltage_file = file_path + '300V EA 2-MePESI 300-700nm {}K.xls'.format(temp)
    #     data['voltages'][temp] = rcf.read_trans_data(voltage_file)


    # Create the first plot with the first y-axis
    fig1, ax1 = plt.subplots()
    pcg.plot_EA_temp_series(data, ax=ax1, color_map_name='plasma_r',energy=True,smooth=True)


    fig2, ax2 = plt.subplots()
    pcg.plot_ABS_temp_series(data, ax=ax2, color_map_name='plasma_r',energy=True)


    # plt.savefig(fig_name, format='png', dpi=300)

    plt.show()
# CHDA_temp_series()


def CHDMA_temp_series(): # Needs to be updated
    # date where the data is stored
    # file_path = 'C:/Data/2024-09-23/'

    data = {}
    data['trans'] = {}
    data['voltages'] = {}

    # blank_file = file_path + 'Blank 2-MePESI 300-700nm 295K.xls'
    data['blank'] = rcf.read_trans_data(1175) 
    
    # go through the temperatures
    temperatures = [18,50,75,100,150,200,250,295]
    # temperatures = [150,200,250,295]
    
    volt_file_list = [1188, 1186, 1195, 1185,1183,1181,1178,1177]
    trans_file_list = [1189, 1187, 1193, 1184,1182,1180,1179,1176]
    
    # volt_file_list = [1183,1181,1178,1177]
    # trans_file_list = [1182,1180,1179,1176]

    for i in range(len(temperatures)):
        data['trans'][temperatures[i]] = rcf.read_trans_data(trans_file_list[i])
        data['voltages'][temperatures[i]] = rcf.read_trans_data(volt_file_list[i])
        # data['voltages'][temperatures[i]]['X (V) Phased'] *= -1

    # for temp in temperatures:
    #     trans_file = file_path + 'Trans 2-MePESI 300-700nm {}K.xls'.format(temp)
    #     data['trans'][temp] = rcf.read_trans_data(trans_file)

    #     voltage_file = file_path + '300V EA 2-MePESI 300-700nm {}K.xls'.format(temp)
    #     data['voltages'][temp] = rcf.read_trans_data(voltage_file)


    # Create the first plot with the first y-axis
    fig1, ax1 = plt.subplots()
    pcg.plot_EA_temp_series(data, ax=ax1, color_map_name='rainbow',smooth=True,energy=True)


    fig2, ax2 = plt.subplots()
    pcg.plot_ABS_temp_series(data, ax=ax2, color_map_name='rainbow',energy=True)


    # plt.savefig(fig_name, format='png', dpi=300)

    plt.show()
# CHDMA_temp_series()

# fig1, ax1 = plt.subplots()
# fig2, ax2 = plt.subplots()

def AMPY4_temp_series_400_600(): # Needs to be updated
    # date where the data is stored
    # file_path = 'C:/Data/2024-09-23/'

    data = {}
    data['trans'] = {}
    data['voltages'] = {}

    # blank_file = file_path + 'Blank 2-MePESI 300-700nm 295K.xls'
    data['blank'] = rcf.read_trans_data(1308) 
    
    # go through the temperatures
    temperatures = [19,50,100,150,200,250,295]
    
    volt_file_list = [1325, 1324, 1323,1322,1321,1320,1319]
    trans_file_list = [1339, 1338, 1337,1336,1335,1334,1333]

    for i in range(len(temperatures)):
        data['trans'][temperatures[i]] = rcf.read_trans_data(trans_file_list[i])
        data['voltages'][temperatures[i]] = rcf.read_trans_data(volt_file_list[i])
        data['voltages'][temperatures[i]]['X (V) Phased'] *= -1

    # for temp in temperatures:
    #     trans_file = file_path + 'Trans 2-MePESI 300-700nm {}K.xls'.format(temp)
    #     data['trans'][temp] = rcf.read_trans_data(trans_file)

    #     voltage_file = file_path + '300V EA 2-MePESI 300-700nm {}K.xls'.format(temp)
    #     data['voltages'][temp] = rcf.read_trans_data(voltage_file)


    # Create the first plot with the first y-axis
    # fig1, ax1 = plt.subplots()
    pcg.plot_EA_temp_series(data, ax=ax1, color_map_name='rainbow',colorbar=False)


    # fig2, ax2 = plt.subplots()
    pcg.plot_ABS_temp_series(data, ax=ax2, color_map_name='rainbow',colorbar=False)


    # plt.savefig(fig_name, format='png', dpi=300)

    # plt.show()
# AMPY4_temp_series_400_600()

def AMPY4_temp_series_590_700(): # Needs to be updated
    # date where the data is stored
    # file_path = 'C:/Data/2024-09-23/'

    data = {}
    data['trans'] = {}
    data['voltages'] = {}

    # blank_file = file_path + 'Blank 2-MePESI 300-700nm 295K.xls'
    data['blank'] = rcf.read_trans_data(1309) 
    
    # go through the temperatures
    temperatures = [19,50,100,150,200,250,295]
    
    volt_file_list = [1318, 1317, 1316,1315,1314,1313,1312]
    trans_file_list = [1332, 1331, 1330,1329,1328,1327,1326]

    for i in range(len(temperatures)):
        data['trans'][temperatures[i]] = rcf.read_trans_data(trans_file_list[i])
        data['voltages'][temperatures[i]] = rcf.read_trans_data(volt_file_list[i])
        data['voltages'][temperatures[i]]['X (V) Phased'] *= -1

    # for temp in temperatures:
    #     trans_file = file_path + 'Trans 2-MePESI 300-700nm {}K.xls'.format(temp)
    #     data['trans'][temp] = rcf.read_trans_data(trans_file)

    #     voltage_file = file_path + '300V EA 2-MePESI 300-700nm {}K.xls'.format(temp)
    #     data['voltages'][temp] = rcf.read_trans_data(voltage_file)

    data['voltages'][19]['X (V) Phased'][:30] += 3e-11
    data['voltages'][50]['X (V) Phased'][:30] += 2e-11
    data['voltages'][100]['X (V) Phased'][:30] += 1e-11
    # Create the first plot with the first y-axis
    # fig1, ax1 = plt.subplots()
    pcg.plot_EA_temp_series(data, ax=ax1, color_map_name='rainbow')


    # fig2, ax2 = plt.subplots()
    pcg.plot_ABS_temp_series(data, ax=ax2, color_map_name='rainbow')


    # plt.savefig(fig_name, format='png', dpi=300)

    plt.show()
# AMPY4_temp_series_590_700()


def PESI2F_temp_series(): # Needs to be updated
    # date where the data is stored
    # file_path = 'C:/Data/2024-09-23/'

    data = {}
    data['trans'] = {}
    data['voltages'] = {}
    export = 'C:/Data/Compiled Data/Kentcky Henry/Temp Series' # Folder location to export the data


    # blank_file = file_path + 'Blank 2-MePESI 300-700nm 295K.xls'
    data['blank'] = rcf.read_trans_data(1414, export_folder=export)
    
    # go through the temperatures
    temperatures = [16,50,100,150,200,250,300]
    
    volt_file_list = [1417, 1418, 1421, 1422, 1425, 1426,1429]
    trans_file_list = [1416, 1419, 1420, 1423, 1424, 1427,1428]

    for i in range(len(temperatures)):
        data['trans'][temperatures[i]] = rcf.read_trans_data(trans_file_list[i], export_folder=export)
        data['voltages'][temperatures[i]] = rcf.read_trans_data(volt_file_list[i], export_folder=export)
        # data['voltages'][temperatures[i]]['X (V) Phased'] *= -1

    # Create the first plot with the first y-axis
    fig1, ax1 = plt.subplots()
    pcg.plot_EA_temp_series(data, ax=ax1, smooth=False, color_map_name='rainbow')


    fig2, ax2 = plt.subplots()
    pcg.plot_ABS_temp_series(data, ax=ax2, color_map_name='rainbow')


    # plt.savefig(fig_name, format='png', dpi=300)

    plt.show()
# PESI2F_temp_series()


