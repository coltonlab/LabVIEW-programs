import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np


def data_template():
    data = {}
    
    fig, ax = plt.subplots()
    data['trans'] = rcf.read_trans_data(626)

    pcg.plot_data(data['trans'],ax=ax)

    plt.show()

# data_template()



def absorption_temerature_series_template():
    # Dictionary that holds all of the data with input trans
    data = {}
    data['trans'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank'] = rcf.read_trans_data(642)

    # data['trans'][14] = rcf.read_trans_data(635) # voltage_file
    # data['trans'][50] = rcf.read_trans_data(636) # voltage_file
    # data['trans'][100] = rcf.read_trans_data(637) # voltage_file
    # data['trans'][150] = rcf.read_trans_data(638) # voltage_file
    data['trans'][200] = rcf.read_trans_data(647) # voltage_file
    data['trans'][250] = rcf.read_trans_data(646) # voltage_file
    # data['trans'][300] = rcf.read_trans_data(641) # voltage_file


    fig, ax = plt.subplots()
    pcg.plot_ABS_temp_series(data, ax=ax, color_map_name='rainbow', smooth=False)


    # plt.savefig(fig_name, format='png', dpi=300)

    plt.show()

absorption_temerature_series_template()



def absorption_template():
    data = {}

    data['blank'] = rcf.read_trans_data(645)
    data['trans'] = rcf.read_trans_data(644)

    fig, ax = plt.subplots()

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False)

    # ax.legend(trans_files)

    plt.show()

# absorption_template()
























def PM6Y6():
    data = {}

    # data['blank'] = rcf.read_trans_data(543)
    # data['trans'] = rcf.read_trans_data(544)

    # fig, ax = plt.subplots()

    # # plot data
    # pcg.plot_absorption(data, ax=ax, smooth=False)





    fig2, ax2 = plt.subplots()

    # plot data
    pcg.plot_data(data['trans'],ax=ax2)
    pcg.plot_data(data['blank'],ax=ax2)
    
    # ax.legend(trans_files)

    plt.show()



def PM6Y6():
    data = {}

    data['blank'] = rcf.read_trans_data(567)
    data['trans'] = rcf.read_trans_data(568)



    fig2, ax2 = plt.subplots()

    # plot data
    pcg.plot_data(data['trans'],ax=ax2, smooth=True)
    pcg.plot_data(data['blank'],ax=ax2)
    
    # ax.legend(trans_files)

    plt.show()


