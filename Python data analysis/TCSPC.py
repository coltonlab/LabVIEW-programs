import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np



def TCSPC_template():
    data = {}
    legend_names = []
    fig, ax = plt.subplots()

    files = range(801,815)
    # files = [803]


    for file in files:

        data, sample_name, temperature = rcf.read_TCSPC_data(file)

        ax.plot(data['Time'][:494],data['Counts'][:494], label=temperature)
        print(f'{temperature}: {max(data['Counts'][:494])}')
        # ax.semilogy(data['Time'],data['Counts'], label=temperature)
        # pcg.plot_PL(data,ax=ax,energy=False, /normalize=False)

        # legend_names.append(f' #{i}')
    ax.legend()


    plt.show()

# TCSPC_template()


def TCSPC_template():
    data = {}
    legend_names = []
    fig, ax = plt.subplots()

    files = range(817,858) # ZnO


    for file in files:
        single_data, sample_name, temperature = rcf.read_TCSPC_data(file)
        print(temperature)
        data[temperature] = single_data


    # ax.legend()
    # pcg.plot_TCSPC_Series(data=data,ax=ax)
    # pcg.plot_TCSPC_Series_Maximum(data=data,ax=ax)
    ZnO_decay_rates = pcg.plot_TCSPC_Series_FWHM(data=data,ax=ax)
    # ZnO_decay_rates = pcg.plot_TCSPC_Series_decay_rate(data=data,ax=ax)
    ax.set_title(sample_name)

    #########################################################
    data = {}
    legend_names = []
    fig2, ax2 = plt.subplots()

    files = range(799,812) # APO

    for file in files:
        single_data, sample_name, temperature = rcf.read_TCSPC_data(file)
        print(temperature)
        data[temperature] = single_data

    APO_decay_rates = pcg.plot_TCSPC_Series_FWHM(data=data,ax=ax)
    # APO_decay_rates = pcg.plot_TCSPC_Series_decay_rate(data=data,ax=ax2)
    ax2.set_title(sample_name)

    ###############################################
    fig3, ax3 = plt.subplots()
    ax3.scatter(APO_decay_rates[:,0], APO_decay_rates[:,1],color='blue', label='APO')
    ax3.scatter(ZnO_decay_rates[1:,0], ZnO_decay_rates[1:,1],color='red', label='ZnO Ferritian')
    ax3.legend()
    ax3.set_ylabel('FWHM (ns)')
    ax3.set_xlabel('Wavelength (nm)')
    plt.show()

# TCSPC_template()


def TCSPC_template():
    data = {}
    legend_names = []
    

    files1 = range(799,812) # ZnO
    # files = [820,821,822]
    files2 = range(817,858) # ZnO
    
    # files = list(files1)+list(files2)

    for file in files1:
        single_data, sample_name, temperature = rcf.read_TCSPC_data(file)
        single_data['Counts'] = single_data['Counts'][:494]
        single_data['Time'] = single_data['Time'][:494]
        print(temperature)
        data[temperature] = single_data

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    # fig3, ax3 = plt.subplots()
    fig4, ax4 = plt.subplots()
    fig5, ax5 = plt.subplots()


    pcg.plot_TCSPC_Series(data=data,ax=ax1)
    pcg.plot_TCSPC_Series_Maximum(data=data,ax=ax2)
    # ZnO_decay_rates = pcg.plot_TCSPC_Series_FWHM(data=data,ax=ax3)
    APO_decay_rates = pcg.plot_TCSPC_Series_decay_rate(data=data,ax=ax4, color_map_name='cool')
    # pcg.plot_TCSPC_PL_time(data=data,ax=ax)




    data = {}
    for file in files2:
        single_data, sample_name, temperature = rcf.read_TCSPC_data(file)
        single_data['Counts'] = single_data['Counts'][:494]
        single_data['Time'] = single_data['Time'][:494]
        print(temperature)
        data[temperature] = single_data


    ZnO_decay_rates = pcg.plot_TCSPC_Series_decay_rate(data=data,ax=ax4,color_map_name='Wistia')


    plt.show()


# def PL_template():
#     data = {}
#     legend_names = []
#     # fig, ax = plt.subplots()
#     for i in range(862, 863):
#         data, sample_name, temperature = rcf.read_CCD_data(i)
#         pcg.plot_PL(data,ax=ax,energy=False, normalize=True)
#         legend_names.append(temperature)
#     ax.legend(legend_names)

#     # plt.show()
# PL_template() 

TCSPC_template()






