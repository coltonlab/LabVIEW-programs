import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np



def PL_template():
    data = {}
    
    fig, ax = plt.subplots()
    data['trans'] = rcf.read_CCD_data(445)

    pcg.plot_PL(data['trans'],ax=ax,energy=False)

    plt.show()





def PL_test():
    data = {}
    
    # fig, ax = plt.subplots()
    legend_names = []

    rows = range(609,612)
    fig, ax = plt.subplots()
    
    for i in rows:
    
        data, sample_name, temperature = rcf.read_CCD_data(i)
        pcg.plot_PL(data, ax=ax, energy=True,normalize=False)
        legend_name = temperature# + 'K'
        legend_names.append(legend_name)


    ax.set_title(sample_name)
    ax.legend(legend_names)
    plt.show()

PL_test()













def comparison():
    from scipy.interpolate import interp1d
    from public.colton_math_functions import savitzky_golay_smoothing

    data1, sample_name, temperature = rcf.read_CCD_data(541)
    data2, sample_name, temperature = rcf.read_PMT_data(539)

    # Example data
    x1 = data1['Wavelength']  # X-values for data1
    y1 = data1['Processed Data']  # Y-values for data1

    x2 = data2['Spectrometer Triax 550:0 (?)']
    y2 = data2['A, B average (cps)']


    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()

    # Interpolating data2 at x1 points
    f2 = interp1d(x2, y2, kind='cubic', fill_value='extrapolate')
    y2_interpolated =  savitzky_golay_smoothing(f2(x1))


    # ax1.plot(x1,y1)

    ax2.plot(x2,y2)
    ax2.plot(x1,y2_interpolated)


    comp = y2_interpolated/y1
    ax1.set_yscale('log')
    ax1.plot(x1[15:],comp[15:])

    plt.show()

    # # Interpolating data1 at x2 points
    f1 = interp1d(x1, y1, kind='cubic', fill_value='extrapolate')
    y1 = f1(x1)

    # # Comparison at x1 points
    # comparison_at_x1 = y1 / y2_interpolated
    # print("Comparison at x1 points:", comparison_at_x1)

    # # Comparison at x2 points
    # comparison_at_x2 = y1_interpolated / y2
    # print("Comparison at x2 points:", comparison_at_x2)




# comparison()










