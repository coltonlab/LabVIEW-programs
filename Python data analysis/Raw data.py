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
    for i in [1285,1286]:
        # print(i)
        data['trans'], sample = rcf.read_trans_data(i, sample=True)
        # data['trans']['X (V)'] -= data['trans']['X (V)'][63] #+ offset[j]
        pcg.plot_data(data['trans'],ax=ax, energy=False, smooth=True)
        legend.append(sample)
        j+=1

    # for i in [1110,1111,1112,1113,1114]:
    # # for i in range(1008,1025):
    #     # print(i)
    #     data[i], sample = rcf.read_trans_data(i, sample=True)
    
    # data[1111]['X (V) Phased'] = ((data[1110]['X (V) Phased']/(data[1114]['X (V) Phased']-1.9e-11)))#/data[1110]['X (V) Phased'])**-1
    # pcg.plot_data(data[1111],ax=ax, energy=False, smooth=True)
    
    # legend.append('Diff 1')

    # data[1112]['X (V) Phased'] = +data[1114]['X (V) Phased'] - 1.9e-11
    # data[1112]['Digikrom Spectr.:0 (?)'] += 1
    # pcg.plot_data(data[1112],ax=ax, energy=False, smooth=True)
    
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

    for i in [1285,1286]:
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
data_template()