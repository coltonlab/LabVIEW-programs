'''
This is a conveniant spot to put all of the mathematical functions that the colton group uses. 
'''
import numpy as np
from scipy.signal import savgol_filter
import scipy.special as sps
from scipy.optimize import minimize, curve_fit


'''Calculates the EA signal with the input ea data and transmission data '''
def EA(voltage_X, trans):
    return -np.log(1 + voltage_X.values/trans.values)



'''Calculates the EA signal with the input ea data and transmission data '''
def EA_smooth(voltage_X, trans):
    trans_smooth = savitzky_golay_smoothing(trans.values)
    voltage_X_smooth = savitzky_golay_smoothing(voltage_X.values)
    return -np.log(1 + voltage_X_smooth/trans_smooth)



'''Calculates the absorption given a blank and transmission data '''
def absorption(trans, blank):
    return -np.log10(trans.values/blank.values)

 

'''Calculates the absorption given a blank and transmission data '''
def absorption_smooth(trans, blank):
    trans_smooth = savitzky_golay_smoothing(trans.values)
    blank_smooth = savitzky_golay_smoothing(blank.values)
    return -np.log10(trans_smooth/blank_smooth)



'''Calculate CD in millidegrees'''
def circular_dichrosim(AC,DC):
    return (-32982/(np.log(10)*sps.j1(0.587*np.pi)))*(AC/DC)*(2**0.5)



'''Calculates the absorption given a blank and transmission data '''
def circular_dichrosim_smooth(AC,DC):
    AC = savitzky_golay_smoothing(AC)
    DC = savitzky_golay_smoothing(DC)
    return (-32982/(np.log(10)*sps.j1(0.587*np.pi)))*(AC/DC)*(2**0.5)



'''Calculates the absorption given a blank and transmission data '''
def circular_dichrosim_smooth(AC,DC):
    # AC = savitzky_golay_smoothing(AC)
    # DC = savitzky_golay_smoothing(DC)
    return (-32982/(np.log(10)*sps.j1(np.pi/2)))*(AC/DC)



'''Converts wavelength to energy'''
def wavelength_to_energy(wavelength): 
    return 1239.84193/wavelength.values



'''Apply Savitzky-Golay smoothing to the given data.'''
def savitzky_golay_smoothing(y, window_length=20, polyorder=3):
    """
    Parameters:
        y (array-like): Dependent variable (e.g., measured values).
        window_length (int): Length of the window over which the polynomial is fit.
        polyorder (int): Order of the polynomial that is fit to the data within each window.

    Returns:
        array-like: Smoothed data.
    """
    smoothed_y = savgol_filter(y, window_length, polyorder)
    return smoothed_y



''' This program uses a for loop and finds the min value for Y in 10 iterations, it then does another 10 at a smaller step size '''
def phase_data(data, x_name='X (V)', y_name='Y (V)'):
    
    X = data[x_name]
    Y = data[y_name]

    # Fixes any offsets
    # X -= np.mean(X)
    # Y -= np.mean(Y)

    # Calculate Y values for each angle
    min_y = float('inf')
    min_angle = 0
    BC = 3.15/2 # boundry conditions

    # # This double four loop allows us to go through 60 values of Y to get an accuracy within 1.8e-4 degrees.
    # for i in range(4): # Increase this number to increase your tolerance. Change this number if you want 1.8e-(n-2) order of accuracy
    #     angles = np.linspace(min_angle - BC , min_angle + BC, 10)  # Range from -pi/2 to pi/2 radians

    #     # Looking for the smallest abs value of Y with in 10 data points 
    #     for angle in angles:
    #         y_rotated = X * np.sin(angle) + Y * np.cos(angle)
    #         min_y_angle = np.std(y_rotated)

    #         # Keeps the smallest angle
    #         if min_y_angle < min_y:
    #             min_y = min_y_angle
    #             min_angle = angle

    #     # Makes BC smaller for a better step size
    #     BC = BC/10

    # min_angle = -97.8540506127646*np.pi/180
    # min_angle = -105.206*np.pi/180
    # min_angle = np.pi
    min_angle = 99.83940792614993
    print(f'Phased Angle: {min_angle}')

    data['X (V) Phased'] = X * np.cos(min_angle) - Y * np.sin(min_angle)
    data['Y (V) Phased'] = X * np.sin(min_angle) + Y * np.cos(min_angle)

    # print(-
    # data['X (V) Phased'] += 2.02e-13
    return data


''' This program uses a for loop and finds the min value for Y in 10 iterations, it then does another 10 at a smaller step size '''
def phase_data_experiemnt(data, x_name='X (V)', y_name='Y (V)'):
    
    X = data[x_name].values
    Y = data[y_name].values

    # Fixes any offsets
    # X -= np.mean(X)
    # Y -= np.mean(Y)


    # Calculate Y values for each angle
    min_y = float('inf')
    min_angle = 0
    BC = 3.15/2 # boundry conditions

    # This double four loop allows us to go through 60 values of Y to get an accuracy within 1.8e-4 degrees.
    for i in range(4): # Increase this number to increase your tolerance. Change this number if you want 1.8e-(n-2) order of accuracy
        angles = np.linspace(min_angle - BC , min_angle + BC, 10)  # Range from -pi/2 to pi/2 radians

        # Looking for the smallest abs value of Y with in 10 data points 
        for angle in angles:
            x_rotated = X * np.cos(angle) - Y * np.sin(angle)
            y_rotated = X * np.sin(angle) + Y * np.cos(angle)
            min_y_angle = np.std(x_rotated - y_rotated)

            # Keeps the smallest angle
            if min_y_angle < min_y:
                min_y = min_y_angle
                min_angle = angle #+ 3.14/180*45

        # Makes BC smaller for a better step size
        BC = BC/10
    print(min_angle*180/3.1415)
    print(np.average(x_rotated-y_rotated))
    # X -= x_rotated-y_rotated
    Y += x_rotated-y_rotated


    # Calculate Y values for each angle
    min_y = float('inf')
    min_angle = 0
    BC = 3.15/2 # boundry conditions

    # This double four loop allows us to go through 60 values of Y to get an accuracy within 1.8e-4 degrees.
    for i in range(4): # Increase this number to increase your tolerance. Change this number if you want 1.8e-(n-2) order of accuracy
        angles = np.linspace(min_angle - BC , min_angle + BC, 10)  # Range from -pi/2 to pi/2 radians

        # Looking for the smallest abs value of Y with in 10 data points 
        for angle in angles:
            x_rotated = X * np.cos(angle) - Y * np.sin(angle)
            y_rotated = X * np.sin(angle) + Y * np.cos(angle)
            min_y_angle = np.std(y_rotated)

            # Keeps the smallest angle
            if min_y_angle < min_y:
                min_y = min_y_angle
                min_angle = angle #+ 3.14/180*45

        # Makes BC smaller for a better step size
        BC = BC/10
    print(min_angle)
    print(np.average(x_rotated-y_rotated))
    # X += x_rotated-y_rotated
    # Y += x_rotated-y_rotated

    data['X (V) Phased'] = X * np.cos(min_angle) - Y * np.sin(min_angle)
    data['Y (V) Phased'] = X * np.sin(min_angle) + Y * np.cos(min_angle)

    return data


''' This program uses a for loop and finds the min value for Y in 10 iterations, it then does another 10 at a smaller step size '''
def phase_data_experiemnt_bad(data, x_name='X (V)', y_name='Y (V)'):
    X = data[x_name]
    Y = data[y_name]

    def std_phase(guess, offset):
        angle = guess
        x_rotated = X * np.cos(angle) - Y * np.sin(angle)
        y_rotated = X * np.sin(angle) + Y * np.cos(angle)
        return np.std(x_rotated - (y_rotated + offset))
    

    # Initial guess for the coefficients
    std_guess = 2*np.pi/360*55
    offset = 0
    # Use SciPy's minimize function to find the best fit coefficients
    result_phase = minimize(std_phase, std_guess, args=(offset))
    print(result_phase)
    min_angle = result_phase.x
    # print(result_phase)


    X_offset, Y_offset = 0, 0
    factor = 1e-6 # This helps since the numbers are so small - change to mean(X)?


    # # Fixes any offsets that occur - I don't know if this can be used
    # def offset(guess):
    #     X_new = X - guess[0]*factor
    #     Y_new = Y - guess[1]*factor

    #     y_rotated = X_new * np.sin(min_angle) + Y_new * np.cos(min_angle)
    #     return np.sum(abs(y_rotated))
    

    # # Initial guess for the coefficients
    # offset_guess = [np.mean(X)/factor,np.mean(Y)/factor]

    # # Use SciPy's minimize function to find the best fit coefficients
    # result_offset = minimize(offset, offset_guess)#, bounds=[(0, None)])
    # X_offset, Y_offset = result_offset.x
    # # print(result_offset)


    X = X - X_offset*factor
    Y = Y - Y_offset*factor

    data['X (V) Phased'] = X * np.cos(min_angle) - Y * np.sin(min_angle)
    data['Y (V) Phased'] = X * np.sin(min_angle) + Y * np.cos(min_angle)

    return data





from scipy.interpolate import UnivariateSpline

def finite_difference_derivative(x, y, order=1, dx=1):
    """
    Compute the derivative of a dataset using finite difference method.

    Parameters:
        x (array_like): Independent variable values.
        y (array_like): Dependent variable values.
        order (int, optional): Order of the finite difference method. Default is 1.
        dx (float, optional): Step size between points. Default is 1.

    Returns:
        ndarray: Array containing the derivative values.
    """
    derivative = np.diff(y, n=order) / (dx ** order)
    return derivative




def FK_fit(d_1, d_2, data_to_fit):
    # Define the function to minimize
    def objective(guess):
        a, b = guess
        value = np.sum((a * d_1 + b * d_2 - data_to_fit) ** 2)
        # print(value)
        return value 

    # Initial guess for the coefficients
    initial_guess = [0.4, 0.6]

    # Use SciPy's minimize function to find the best fit coefficients
    result = minimize(objective, initial_guess)
    print(result)

    # Extract the optimal coefficients
    a_optimal, b_optimal = result.x
    fit = a_optimal * d_1 + b_optimal * d_2


    return fit



def difference_to_sum_ratio(A,B):
    return (A-B)/(A+B)




def FWHM(x,y):
    # Find the maximum value of the peak
    max_y = np.max(y)

    # Calculate half maximum
    half_max = max_y / 2

    # Find the indices where the y-values are closest to the half maximum
    indices = np.where(y >= half_max)[0]

    # Get the x-values at those indices
    x1 = x[indices[0]]
    x2 = x[indices[-1]]

    # Calculate FWHM
    fwhm = x2 - x1
    return fwhm


def TCSPC_decay_rate(time,intensity):
    # Define the exponential decay function
    def exponential_decay(t, I1, I2, tau, tau2):
        return I1 * np.exp(-t / tau) + I2 * np.exp(-t / tau2)

    index = np.argmax(intensity)+6
    time = time[index:]
    intensity = intensity[index:]#-min(intensity)
                

    # Perform the curve fit
    popt, pcov = curve_fit(exponential_decay, time, intensity, p0=(intensity.max()*2/3, intensity.max()/3, 1.0, 0.5))

    # Extract the fitted parameters
    I0_fit1, I0_fit2, tau_fit, tau_fit_2 = popt
    # print(y0-min(intensity))

    # Calculate the decay rate
    decay_rate = tau_fit
    decay_rate2 = tau_fit_2

    # print(f'{I0_fit1} exp(-t / {tau_fit})    +     {I0_fit2} * exp(-t / {tau_fit_2})')
    # print(decay_rate+decay_rate2)

    import matplotlib.pyplot as plt
    # Plot the data and the fit
    fig = plt.figure(6)
    plt.plot(time, intensity, label='Fit',linewidth=2 ,color='blue')
    plt.plot(time, exponential_decay(time, *popt), label='Fit', color='red')
    plt.xlabel('Time (t)')
    plt.ylabel('Intensity (I)')
    plt.legend()
    return decay_rate, decay_rate2