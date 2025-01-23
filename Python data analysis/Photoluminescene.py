import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np



def PL_template():
    data = {}
    legend_names = []
    fig, ax = plt.subplots()
    # for i in range(522,530):
    for i in [1107,1108,1109]:
        data, sample_name, temperature = rcf.read_CCD_data(i)
        pcg.plot_PL(data,ax=ax,energy=False, normalize=True)
        legend_names.append(sample_name)#temperature + 'K')
    ax.legend(legend_names)
    ax.set_title("1:2 PM6Y6 Electroluminescence")

    plt.show()
# PL_template()

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

def PL_fit():
    data = {}
    
    data, sample_name, temperature = rcf.read_CCD_data(585)
    x = data['Wavelength']
    y = data['Processed Data']

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit

    # Generate sample data

    # Define the function for two Gaussians
    def two_gaussians(x, a1, mu1, sigma1, a2, mu2, sigma2):
        return (a1 * np.exp(-(x - mu1)**2 / (2 * sigma1**2)) + a2 * np.exp(-(x - mu2)**2 / (2 * sigma2**2)))

    # Initial guess for the parameters
    initial_guess = [1, 2, 1.5, 1, -2, 1.0]

    # Fit the data
    params, covariance = curve_fit(two_gaussians, x, y, p0=initial_guess)

    # Extract the parameters
    a1, mu1, sigma1, a2, mu2, sigma2 = params

    # Print the fitted parameters
    print(f'Fitted parameters: a1={a1:.3f}, mu1={mu1:.3f}, sigma1={sigma1:.3f}, a2={a2:.3f}, mu2={mu2:.3f}, sigma2={sigma2:.3f}')

    # Plot the data and the fit
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label='Data', s=10)
    plt.plot(x, two_gaussians(x, *params), label='Fitted function', color='red')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Fit of Two Gaussians to Data')
    plt.show()
# PL_fit()

def PL_APO():
    data = {}
    legend_names = []

    fig, ax = plt.subplots()


    APO_data, sample_name, temperature = rcf.read_CCD_data(665)
    C029_data, sample_name, temperature = rcf.read_CCD_data(667)

    spot = 43

    for i in range(670,673):
        C029_data, sample_name, temperature = rcf.read_CCD_data(i)
        APO_coeff = APO_data['Processed Data'][spot]
        C029_coeff = C029_data['Processed Data'][spot]

        X = APO_data['Wavelength']
        ax.set_xlabel('Wavelength (nm)')    

        # ax.plot(X, APO_data['Processed Data']/APO_coeff, label='APO')
        # ax.plot(X, C029_data['Processed Data'][:186]/C029_coeff, label= sample_name)

        data = C029_data['Processed Data'][:186]/C029_coeff - APO_data['Processed Data']/APO_coeff
        ax.plot(X, data, label=f'Difference {i}')

    plt.legend()

    plt.show()
# PL_APO()

def PL_APO():
    data = {}
    legend_names = []
    fig, ax = plt.subplots()
    spot = 43

    # Finding the average of APO
    total_data = np.zeros(187) #224
    j = 0
    for i in range(663,667):
        data, sample_name, temperature = rcf.read_CCD_data(i)
        print(len(data['Processed Data']))
        total_data += data['Processed Data']
        j += 1
    APO_data = total_data/j
    APO_coeff = APO_data[spot]

    X = data['Wavelength']
    ax.plot(X, APO_data/APO_coeff, label='APO')

    # # Finding the average of 0.29
    # total_data = np.zeros(187) #224
    # j = 0
    # for i in range(667,670):
    #     data, sample_name, temperature = rcf.read_CCD_data(i)
    #     print(len(data['Processed Data']))
    #     total_data += data['Processed Data']
    #     j += 1
    # C029_data = total_data/j


    # # Finding the average of 0.2
    # total_data = np.zeros(214)
    # j = 0
    # for i in range(670,673):
    #     data, sample_name, temperature = rcf.read_CCD_data(i)
    #     print(len(data['Processed Data']))
    #     total_data += data['Processed Data']
    #     j += 1
    # C02_data = total_data/j
    # C02_coeff = C02_data[spot]
    # X = data['Wavelength']
    # ax.plot(X, C02_data/C02_coeff, label='C 0.2')


    # Finding the average of 0.1
    total_data = np.zeros(214)
    j = 0
    for i in range(673,681):
        data, sample_name, temperature = rcf.read_CCD_data(i)
        size = len(data['Processed Data'])
        if size == 214:
            total_data += data['Processed Data']
            j += 1
            X = data['Wavelength']
    C01_data = total_data/j
    C01_coeff = C01_data[spot]
    ax.plot(X, C01_data/C01_coeff, label='C 0.1')


    data = C01_data[:187]/C01_coeff - APO_data/APO_coeff
    # data = C02_data[:187]/C02_coeff - APO_data/APO_coeff
    ax.plot(X[:187], data, label=f'Difference')

    plt.legend()
    plt.show()
# PL_APO()

def PL_laser_power_series():
    data = {}
    
    fig, ax = plt.subplots()
    legend_names = []

    rows = range(863,869)
    
    for i in rows:
        data, sample_name, temperature = rcf.read_CCD_data(i)
        pcg.plot_PL(data, ax=ax, energy=False,normalize=False)
        
        legend_name = f'{temperature} $W/cm^2$'
        legend_names.append(legend_name)


    ax.set_title(sample_name)
    ax.legend(legend_names)

    plt.show()
# PL_laser_power_series()

def PL_temperature_series():
    data = {}
    legend_names = []
    fig, ax = plt.subplots()
    
    for i in range(736,744):
    # for i in range(721,728):
        data, sample_name, temperature = rcf.read_CCD_data(i)
        pcg.plot_PL(data,ax=ax,energy=False, normalize=False)
        legend_names.append(temperature)
    ax.legend(legend_names)

    plt.show()
# PL_temperature_series()

def PL_temperature_series_FWHM():
    data = {}
    legend_names = []
    fig, ax = plt.subplots()
    fig2, ax2 = plt.subplots()
    
    files = [736,737,738,741]
    files = [736,739,740,742,743]
    # for i in range(736,744):
    for i in files:
        data, sample_name, temperature = rcf.read_CCD_data(i)
        pcg.plot_PL_FWHM(data,ax=ax, temperature=temperature, energy=False)
        pcg.plot_PL(data,ax=ax2, energy=False)
        legend_names.append(temperature)
    ax2.legend(legend_names)
    ax.set_title(sample_name)
    ax2.set_title(sample_name)
    
    
    plt.show()
# PL_temperature_series_FWHM()


def PL_4_AMPY():
    data = {}
    legend_names = []
    fig, ax = plt.subplots()
    # for i in range(522,530):
    for i in [1233,1234]:
        data, sample_name, temperature = rcf.read_CCD_data(i)
        pcg.plot_PL(data,ax=ax,energy=False)
        legend_names.append(sample_name)#temperature + 'K')
    ax.legend(legend_names)
    ax.set_title("4-AMPY 10ms")

    # plt.show()
# PL_4_AMPY()



def PL_4_AMPY_300ms():
    data = {}
    legend_names = []
    fig, ax = plt.subplots()
    # for i in range(522,530):
    for i in [1236,1235]:
        data, sample_name, temperature = rcf.read_CCD_data(i)
        pcg.plot_PL(data,ax=ax,energy=False)
        legend_names.append(sample_name)#temperature + 'K')
    ax.legend(legend_names)
    ax.set_title("4-AMPY 300ms")

    plt.show()
# PL_4_AMPY_300ms()


def PL_GaAs():
    data = {}
    legend_names = []
    fig, ax = plt.subplots()
    # for i in range(522,530):
    for i in [1242]:
        data, sample_name, temperature = rcf.read_CCD_data(i)
        pcg.plot_PL(data,ax=ax,energy=False, normalize=True)
        legend_names.append(sample_name)#temperature + 'K')
    ax.legend(legend_names)
    ax.set_title("GaAs PL")

    plt.show()
# PL_GaAs()


def PL_4_AMPY_excitation():
    data = {}
    legend_names = []
    fig, ax = plt.subplots()
    # for i in range(522,530):
    for i in [1237,1238,1239,1240,1241]:
        data, sample_name, temperature = rcf.read_CCD_raw_data(i)
        pcg.plot_PL(data,ax=ax,energy=True)
        legend_names.append(sample_name)#temperature + 'K')
    ax.legend(legend_names)
    ax.set_title("4-AMPY")

    plt.show()
# PL_4_AMPY_excitation()




def PL_4_AMPY_excitation():
    data = {}
    legend_names = []
    fig, ax = plt.subplots()
    # for i in range(522,530):
    for i in range(1376,1383):
        data, sample_name, temperature = rcf.read_CCD_data(i)
        pcg.plot_PL(data,ax=ax,energy=True)
        legend_names.append(temperature + 'K')
    ax.legend(legend_names)
    ax.set_title("Nilave 50-50")

    plt.show()
# PL_4_AMPY_excitation()


def PL_template():
    data = {}
    legend_names = []
    fig, ax = plt.subplots()
    # for i in range(522,530):
    for i in range(1400-1,1406+2):
        data, sample_name, temperature = rcf.read_CCD_data(i)
        pcg.plot_PL(data,ax=ax,energy=False, normalize=True)
        legend_names.append(sample_name)#temperature + 'K')
    ax.legend(legend_names)
    ax.set_title("1:2 PM6Y6 Electroluminescence")

    plt.show()
# PL_template()



def PL_template():
    data = {}
    legend_names = []
    fig, ax = plt.subplots()
    # for i in range(522,530):
    for i in [1455,1456,1457,1458]:
        data, sample_name = rcf.read_CCD_data(i, sample=True)
        print(sample_name)
        print(list(data.keys()))
        pcg.plot_PL(data,ax=ax,energy=False, normalize=False)
        legend_names.append(sample_name)#temperature + 'K')
    ax.legend(legend_names)
    ax.set_title("All APO Ferritin plots")

    plt.show()
# PL_template()






def PL_template():
    data = {}
    legend_names = []
    fig, ax = plt.subplots()
    # for i in range(522,530):


    def PL_average(data, keys):
        sum = 0
        for i in keys:
            sum += np.log10(data[i]['Processed Data'])
        average = sum/len(keys)
        return 10**average


    files_APO = [1497, 1498, 1499]
    for i in files_APO:
        data[i], sample_name = rcf.read_CCD_data(i, sample=True)

    data['APO_average'] = data[i].copy()
    data["APO_average"]['Processed Data'] = PL_average(data, files_APO)

    files_ZnO = [1500, 1501, 1502, 1503]
    for i in files_ZnO:
        data[i], sample_name = rcf.read_CCD_data(i, sample=True)

    data["ZnO_average"] = data[i].copy()
    data["ZnO_average"]['Processed Data'] = PL_average(data, files_ZnO)

    factor_point = 42
    print(data["APO_average"]['Wavelength'][factor_point])
    factor = data["APO_average"]['Processed Data'][factor_point]/data["ZnO_average"]['Processed Data'][factor_point]

    data["ZnO_average"]['Processed Data']*=factor

    data["Diff"] = data[i].copy()
    data["Diff"]['Processed Data'] = (data["ZnO_average"]['Processed Data'] -  data["APO_average"]['Processed Data'])*5

    pcg.plot_PL(data["APO_average"],ax=ax,energy=False, normalize=False)
    pcg.plot_PL(data["ZnO_average"],ax=ax,energy=False, normalize=False)
    pcg.plot_PL(data["Diff"],ax=ax,energy=False, normalize=False)

# for i in [1497, 1498, 1499]:
#         data, sample_name = rcf.read_CCD_data(i, sample=True)
#         print(data)
#         # print(sample_name)
#         # print(list(data.keys()))
#         pcg.plot_PL(data,ax=ax,energy=False, normalize=False)
#         legend_names.append(sample_name)#temperature + 'K')
    ax.legend(['APO Average', 'ZnO Average Scaled', 'Differance x 5'])
#     ax.set_title("All APO Ferritin plots")











    plt.show()
PL_template()