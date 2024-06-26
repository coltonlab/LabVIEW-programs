'''
This is a conveniant spot to put all of the mathematical functions that the colton group uses. 
'''
import numpy as np
from scipy.signal import savgol_filter
import scipy.special as sps
from scipy.optimize import minimize


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
    return (-32982/(np.log(10)*sps.j1(np.pi/2)))*(AC/DC)



'''Converts wavelength to energy'''
def wavelength_to_energy(wavelength): 
    return 1239.84193/wavelength.values



'''Apply Savitzky-Golay smoothing to the given data.'''
def savitzky_golay_smoothing(y, window_length=11, polyorder=3):
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
def phase_data_old(data, x_name='X (V)', y_name='Y (V)'):
    
    X = data[x_name]
    Y = data[y_name]

    # Fixes any offsets
    # X -= np.mean(X)
    # Y -= np.mean(Y)

    # Calculate Y values for each angle
    min_y = float('inf')
    min_angle = 0
    BC = 3.15/2 # boundry conditions

    # This double four loop allows us to go through 60 values of Y to get an accuracy within 1.8e-4 degrees.
    for i in range(5): # Increase this number to increase your tolerance. Change this number if you want 1.8e-(n-2) order of accuracy
        angles = np.linspace(min_angle - BC , min_angle + BC, 10)  # Range from -pi/2 to pi/2 radians

        # Looking for the smallest abs value of Y with in 10 data points 
        for angle in angles:
            y_rotated = X * np.sin(angle) + Y * np.cos(angle)
            min_y_angle = np.std(y_rotated)

            # Keeps the smallest angle
            if min_y_angle < min_y:
                min_y = min_y_angle
                min_angle = angle

        # Makes BC smaller for a better step size
        BC = BC/10

    data['X (V) Phased'] = X * np.cos(min_angle) - Y * np.sin(min_angle)
    data['Y (V) Phased'] = X * np.sin(min_angle) + Y * np.cos(min_angle)

    return data



''' This program uses a for loop and finds the min value for Y in 10 iterations, it then does another 10 at a smaller step size '''
def phase_data(data, x_name='X (V)', y_name='Y (V)'):
    X = data[x_name]
    Y = data[y_name]

    def std_phase(guess):
        angle = guess

        y_rotated = X * np.sin(angle) + Y * np.cos(angle)
        return np.std(y_rotated)*1e13

    # Initial guess for the coefficients
    std_guess = 0

    # Use SciPy's minimize function to find the best fit coefficients
    result_phase = minimize(std_phase, std_guess)
    min_angle = result_phase.x
    # print(result_phase)


    X_offset, Y_offset = 0, 0
    factor = 1e-6 # This helps since the numbers are so small - change to mean(X)?


    # Fixes any offsets that occur - I don't know if this can be used
    def offset(guess):
        X_new = X - guess[0]*factor
        Y_new = Y - guess[1]*factor

        y_rotated = X_new * np.sin(min_angle) + Y_new * np.cos(min_angle)
        return np.sum(abs(y_rotated))
    

    # Initial guess for the coefficients
    offset_guess = [np.mean(X)/factor,np.mean(Y)/factor]

    # Use SciPy's minimize function to find the best fit coefficients
    result_offset = minimize(offset, offset_guess)#, bounds=[(0, None)])
    X_offset, Y_offset = result_offset.x
    # print(result_offset)


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


