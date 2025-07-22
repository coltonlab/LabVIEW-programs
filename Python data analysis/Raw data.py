import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np


def data_template():
    data = {}
    
    fig, ax = plt.subplots()
    legend = []

    j=0
    # offset = [1.4202172e-12,4.2003812e-12,1.0245343e-11]
    # Just add the row numbers that you want to add to the scan. <------------------
    for i in [1384,1385]:
        # print(i)
        data['trans'], sample = rcf.read_trans_data(i, sample=True)
        # data['trans']['X (V)'] -= data['trans']['X (V)'][63] #+ offset[j]
        pcg.plot_data(data['trans'],ax=ax, energy=False, smooth=True)
        legend.append(sample)
        j+=1

    
    
    # legend.append('Diff 2')

    # data[1113]['X (V) Phased'] = +data[1113]['X (V) Phased'] - data[1110]['X (V) Phased'] - 2.43e-11
    # pcg.plot_data(data[1113],ax=ax, energy=False, smooth=True)
    
    # legend.append('Diff 3')

    # data['trans'], sample = rcf.read_trans_data(971, sample=True)
    # pcg.plot_data(data['trans'],ax=ax, energy=False, smooth=True)
    # legend.append(sample)

    # legend.append('Diff 2')

    # data[1113]['X (V) Phased'] = +data[1113]['X (V) Phased'] - data[1110]['X (V) Phased'] - 2.43e-11
    # pcg.plot_data(data[1113],ax=ax, energy=False, smooth=True)
    
    # legend.append('Diff 3')

    # data['trans'], sample = rcf.read_trans_data(971, sample=True)
    # pcg.plot_data(data['trans'],ax=ax, energy=False, smooth=True)
    # legend.append(sample)
    ax.axhline(y=0,color='k',linewidth=0.8) 


    ax.legend(legend)
    plt.show()
# data_template()

def data_template():
    data = {}
    
    fig, ax = plt.subplots()
    legend = []

    for i in [1384]:
    # for i in range(1259,1267):
        # print(i)
        data['trans'], sample = rcf.read_trans_data(i, sample=True)
        if i == 1285:
            data['trans']['X (V)'] *= 3

        pcg.plot_data(data['trans'],ax=ax, energy=True, smooth=False)
        # legend.append(sample)


    ax.axhline(y=0,color='k',linewidth=0.8) 

    ax.legend(legend)
    plt.show()
# data_template()

def data_template_test_phase():
    data = {}
    
    fig, ax = plt.subplots()
    legend = []

    j=0
    # offset = [1.4202172e-12,4.2003812e-12,1.0245343e-11]
    # Just add the row numbers that you want to add to the scan. <------------------
    # for i in range(1557,1560):
    #     # print(i)
    #     data['trans'], sample = rcf.read_trans_data(i, sample=True)
    #     # data['trans']['X (V)'] -= data['trans']['X (V)'][63] #+ offset[j]
    #     pcg.plot_data(data['trans'],ax=ax, energy=True, smooth=False)
    #     # legend.append(sample)
    #     j+=1
    files = range(1589,1600)
    files = range(1589,1599)
    # files = np.array([1589,1590])

    for i, file in enumerate(files):
        print(i, file)
        try:
            data[i], sample = rcf.read_trans_data(file, sample=True)
            pcg.plot_data(data[i],ax=ax, energy=False, smooth=False, legend=i)
        except:
            print('file does not exist')
        # legend.append(sample)
        



    ax.axhline(y=0,color='k',linewidth=0.8) 


    # ax.legend(legend)
    plt.show()
# data_template_test_phase()

def data_template_voltage_series():
    data = {}
    
    fig, ax = plt.subplots()
    legend = []

    j=0
    # data = rcf.read_voltage_series_data(1562)
    data = rcf.read_voltage_series_data(1563)

    for i in data.keys():
        pcg.plot_data(data[i],ax=ax, energy=True, smooth=False)
        # legend.append(sample)
        j+=1



    ax.axhline(y=0,color='k',linewidth=0.8) 


    # ax.legend(legend)
    plt.show()
# data_template_voltage_series()

def data_template():
    data = {}
    
    fig, ax = plt.subplots()
    legend = []

    data['blank'] = rcf.read_trans_data_old(1752)
    data['trans'] = rcf.read_trans_data_old(1753)

    corrected_df = data['blank']- data['trans']
    corrected_df['Digikrom Spectr.:0 (?)'] = data['blank']['Digikrom Spectr.:0 (?)']

    pcg.plot_data(data['blank'],ax=ax, energy=False, smooth=True)
    pcg.plot_data(data['trans'],ax=ax, energy=False, smooth=True)
    pcg.plot_data(corrected_df,ax=ax, energy=False, smooth=True)

    ax.axhline(y=0,color='k',linewidth=0.8) 

    ax.legend(legend)
    # plt.show()
    ax.set_title('Windows vacummed down')
    plt.show()
# data_template()


def data_template_atm():
    data = {}
    
    fig, ax = plt.subplots()
    legend = []

    data['blank'] = rcf.read_trans_data_old(1755)
    data['trans'] = rcf.read_trans_data_old(1754)

    corrected_df = data['blank']- data['trans']
    corrected_df['Digikrom Spectr.:0 (?)'] = data['blank']['Digikrom Spectr.:0 (?)']

    # pcg.plot_data(data['blank'],ax=ax, energy=False, smooth=True)
    # pcg.plot_data(data['trans'],ax=ax, energy=False, smooth=True)
    pcg.plot_data(corrected_df,ax=ax, energy=False, smooth=True)

    ax.axhline(y=0,color='k',linewidth=0.8) 

    ax.legend(legend)
    ax.set_title('Windows at atm pressure')
    # plt.show()
# data_template_atm()



def data_template_No_cryo():
    data = {}
    
    fig, ax = plt.subplots()
    legend = []

    data['blank'] = rcf.read_trans_data_old(1760)
    data['trans'] = rcf.read_trans_data_old(1762)
    # data['blank'] = rcf.read_trans_data_old(1761)
    # data['trans'] = rcf.read_trans_data_old(1763)
    corrected_df = (data['blank'] + data['trans'])/2
    corrected_df['Digikrom Spectr.:0 (?)'] = data['blank']['Digikrom Spectr.:0 (?)']

    # pcg.plot_data(data['blank'],ax=ax, energy=False, smooth=True)
    # pcg.plot_data(data['trans'],ax=ax, energy=False, smooth=True)
    pcg.plot_data(corrected_df,ax=ax, energy=False, smooth=True)

    ax.axhline(y=0,color='k',linewidth=0.8) 

    ax.legend(legend)
    ax.set_title('No cryostat windows')
    plt.show()
# data_template_No_cryo()



def difference_quarter_subtract():
    import public.colton_math_functions as cmf
    data = {}
    
    fig, ax = plt.subplots()
    legend = []

    data['blank'] = rcf.read_trans_data_old(1977)
    data['trans'] = rcf.read_trans_data_old(1978)
    # data['blank'] = rcf.read_trans_data_old(1761)
    # data['trans'] = rcf.read_trans_data_old(1763)

    corrected_df = (data['blank']/min(data['blank']['X (V)']) - data['trans']/min(data['trans']['X (V)']))
    corrected_df['Digikrom Spectr.:0 (?)'] = data['blank']['Digikrom Spectr.:0 (?)']

    pcg.plot_data(data['blank'],ax=ax, energy=False, smooth=False)
    pcg.plot_data(data['trans'],ax=ax, energy=False, smooth=False)


    pcg.plot_data(corrected_df,ax=ax, energy=False, smooth=False)

    ax.axhline(y=0,color='k',linewidth=0.8) 

    ax.legend(['Right','left','diff'])
    plt.show()
difference_quarter_subtract()

def difference_quarter():
    import public.colton_math_functions as cmf
    data = {}
    
    fig, ax = plt.subplots()
    legend = []

    data['blank'] = rcf.read_trans_data_old(1977)
    data['trans'] = rcf.read_trans_data_old(1978)
    # data['blank'] = rcf.read_trans_data_old(1761)
    # data['trans'] = rcf.read_trans_data_old(1763)

    # corrected_df = (data['blank'] - data['trans'])
    # corrected_df['Digikrom Spectr.:0 (?)'] = data['blank']['Digikrom Spectr.:0 (?)']

    # pcg.plot_data(data['blank'],ax=ax, energy=False, smooth=False)
    # pcg.plot_data(data['trans'],ax=ax, energy=False, smooth=False)
    
    # transR = cmf.transmition(data['trans']['R (V)'], data['blank']['R (V)'])
    transX = cmf.transmition(data['trans']['X (V)'], data['blank']['X (V)'])
    # transY = cmf.transmition(data['trans']['Y (V)'], data['blank']['Y (V)'])
    X = data['blank']['Digikrom Spectr.:0 (?)']
    # pcg.plot_data(transX,ax=ax, energy=False, smooth=False)
    # pcg.plot_data(transY,ax=ax, energy=False, smooth=False)
    # pcg.plot_data(transR,ax=ax, energy=False, smooth=False)
    ax.plot(X, transX)
    # ax.plot(X, transY)
    # ax.plot(X, transR)
    ax.axhline(y=0,color='k',linewidth=0.8) 

    ax.legend(['X','Y','R'])
    plt.show()
# difference_quarter()