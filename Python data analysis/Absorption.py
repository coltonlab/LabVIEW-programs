import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np


def data_template():
    data = {}
    
    fig, ax = plt.subplots()
    legend = []


    # for i in [711,712,715,716,717,718]:
    for i in [746,747,748]:
    # for i in range(702,707):
        print(i)
        data['trans'], sample = rcf.read_trans_data(i, sample=True)
        pcg.plot_data(data['trans'],ax=ax, energy=False, smooth=False)
        legend.append(sample)

    ax.legend(legend)
    plt.show()

# data_template()



def absorption_temerature_series_template():
    # Dictionary that holds all of the data with input trans
    data = {}
    data['trans'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank1'] = rcf.read_trans_data(642)

    data['trans'][15] = rcf.read_trans_data(651) # voltage_file
    data['trans'][50] = rcf.read_trans_data(650) # voltage_file
    data['trans'][100] = rcf.read_trans_data(649) #voltage_file
    data['trans'][150] = rcf.read_trans_data(648) # voltage_file
    fig, ax = plt.subplots()
    # pcg.plot_ABS_temp_series(data, ax=ax, color_map_name='rainbow', smooth=True, colorbar=False)   


    # data['trans'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    # data['blank2'] = rcf.read_trans_data(627)

    data['trans'][200] = rcf.read_trans_data(647) # voltage_file
    data['trans'][250] = rcf.read_trans_data(646) # voltage_file
    data['trans'][300] = rcf.read_trans_data(652) # voltage_file
    
    pcg.plot_ABS_temp_series(data, ax=ax, color_map_name='rainbow', smooth=True, colorbar=True)


    # plt.savefig(fig_name, format='png', dpi=300)

    plt.show()

# absorption_temerature_series_template()



def absorption_template():
    data = {}

    data['blank'] = rcf.read_trans_data(750)
    data['trans'] = rcf.read_trans_data(751)


    fig, ax = plt.subplots()

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False)


    # plt.ylim([0,1])

    # ax.legend(trans_files)

    plt.show()

absorption_template()







import public.colton_math_functions as cmf
def data_template():
    data = {}
    
    fig, ax = plt.subplots()
    legend = []

    data['back window'] = cmf.savitzky_golay_smoothing(rcf.read_trans_data(715)['X (V)'])
    data['front window'] = cmf.savitzky_golay_smoothing(rcf.read_trans_data(716)['X (V)'])
    data['no windows'] = cmf.savitzky_golay_smoothing(rcf.read_trans_data(717)['X (V)'])
    data['both windows'] = cmf.savitzky_golay_smoothing(rcf.read_trans_data(718)['X (V)'])

   
    back_window_diff = data['no windows'] - data['back window']
    front_window_diff = data['no windows'] - data['front window']
    both_windows_diff = data['no windows'] - data['both windows']

    plt.plot(back_window_diff, label='back_window_diff')
    plt.plot(front_window_diff, label='front_window_diff')
    plt.plot(both_windows_diff, label='both_windows_diff')

    plt.legend()
    plt.show()

# data_template()















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


