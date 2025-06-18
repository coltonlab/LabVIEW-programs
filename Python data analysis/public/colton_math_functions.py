'''
This is a conveniant spot to put all of the mathematical functions that the colton group uses. 
'''
import numpy as np
from scipy.signal import savgol_filter, find_peaks
import scipy.special as sps
from scipy.optimize import minimize, curve_fit
from scipy.interpolate import CubicSpline

'''Calculates the EA signal with the input ea data and transmission data '''
def EA(voltage_X, trans):
    # newTrans = trans[35:-10]
    return -np.log(1 + voltage_X.values/trans.values)*1000



'''Calculates the EA signal with the input ea data and transmission data '''
def EA_smooth(voltage_X, trans):
    trans_smooth = savitzky_golay_smoothing(trans.values)
    voltage_X_smooth = savitzky_golay_smoothing(voltage_X.values)
    return -np.log(1 + voltage_X_smooth/trans_smooth)*1000



'''Calculates the absorption given a blank and transmission data '''
def absorption(trans, blank):
    return -np.log10(trans.values/blank.values)


def reflection(trans, total):
    return (trans.values)/total.values


'''Calculates the absorption given a blank and transmission data '''
def reflection_smooth(trans, total):
    trans_smooth = savitzky_golay_smoothing(trans.values)
    # blank_smooth = savitzky_golay_smoothing(blank.values)
    total_smooth = savitzky_golay_smoothing(total.values)
    return (trans_smooth)/total_smooth


def transmition(trans, blank):
    return trans.values/blank.values


'''Calculates the absorption given a blank and transmission data '''
def transmition_smooth(trans, blank):
    trans_smooth = savitzky_golay_smoothing(trans.values)
    blank_smooth = savitzky_golay_smoothing(blank.values)
    return trans_smooth/blank_smooth


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
    CD = (AC/DC) * (1/sps.j1(0.5236)) * (180*1000/np.pi)
    return CD



'''Calculates the absorption given a blank and transmission data '''
def circular_dichrosim(AC,DC):
    # AC = savitzky_golay_smoothing(AC)
    # DC = savitzky_golay_smoothing(DC)
    CD = (AC/DC) * (1/sps.j1(0.5236)) * (180*1000/np.pi)
    return CD



'''Converts wavelength to energy'''
def wavelength_to_energy(wavelength): 
    return 1239.84193/wavelength.values



'''Apply Savitzky-Golay smoothing to the given data.'''
def savitzky_golay_smoothing(y, window_length=10, polyorder=3):
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
def phase_data(dataAll, x_name='X (V)', y_name='Y (V)'):
    data = dataAll.copy()

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
    for i in range(4): # Increase this number to increase your tolerance. Change this number if you want 1.8e-(n-2) order of accuracy
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

    # min_angle = -97.8540506127646*np.pi/180
    print('Phased Angle: {:.2f} degrees'.format(min_angle * 180 / np.pi))

    data['X (V) Phased'] = X * np.cos(min_angle) - Y * np.sin(min_angle)
    data['Y (V) Phased'] = X * np.sin(min_angle) + Y * np.cos(min_angle)

    # import matplotlib.pyplot as plt
    # plt.plot(data['X (V) Phased'])
    # plt.plot(data['Y (V) Phased'])
    # plt.show()
    return data


''' This program uses a for loop and finds the min value for Y in 10 iterations, it then does another 10 at a smaller step size '''
def phase_data_experiemnt(data, x_name='X (V)', y_name='Y (V)'):    
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
    for i in range(4): # Increase this number to increase your tolerance. Change this number if you want 1.8e-(n-2) order of accuracy
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

    # min_angle = -97.8540506127646*np.pi/180
    # min_angle = -105.206*np.pi/180
    # min_angle = np.pi
    # min_angle = 99.83940792614993
    # min_angle = 0
    print(f'Phased Angle: {min_angle*180/np.pi}')

    data['X (V) Phased'] = X * np.cos(min_angle) - Y * np.sin(min_angle)
    data['Y (V) Phased'] = X * np.sin(min_angle) + Y * np.cos(min_angle)

    # print(-
    # data['X (V) Phased'] += 2.02e-13
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




def FK_fit(d_1, d_2, d_3, data_to_fit):
    # Define the function to minimize
    def objective(guess):
        a, b = guess
        value = np.sum((a * d_1 + b * d_2  - data_to_fit) ** 2)
        # print(value)
        return value 

    # Initial guess for the coefficients
    initial_guess = [0.04, 0.06]

    # Use SciPy's minimize function to find the best fit coefficients
    result = minimize(objective, initial_guess)
    # print(result)

    # Extract the optimal coefficients
    a_optimal, b_optimal = result.x
    fit = a_optimal*d_1 + b_optimal*d_2
    print([result.x]/np.sum(result.x)*100)

    return fit



def difference_to_sum_ratio(A,B):
    return (A-B)/(A+B)




def FWHM(x,y):
    from scipy.interpolate import interp1d
    # Find all peaks
    peaks, _ = find_peaks(y)
    if len(peaks) == 0:
        raise ValueError("No peaks found in the data.")

    # Find the max peak
    max_peak_index = peaks[np.argmax(y[peaks])]
    peak_x = x[max_peak_index]
    peak_y = y[max_peak_index]
    
    # Half maximum
    half_max = peak_y / 2.0

    # Interpolation for more accurate crossing points
    interp = interp1d(x, y - half_max, kind='linear', bounds_error=False, fill_value='extrapolate')

    # Find where the curve crosses the half max
    sign_changes = np.where(np.diff(np.sign(y - half_max)))[0]

    # Find left and right crossing points around the peak
    left = None
    right = None
    for idx in sign_changes:
        if x[idx] < peak_x and x[idx+1] < peak_x:
            left = (x[idx], x[idx+1])
        elif x[idx] < peak_x and x[idx+1] >= peak_x:
            left = (x[idx], x[idx+1])
        elif x[idx] >= peak_x and x[idx+1] > peak_x:
            right = (x[idx], x[idx+1])
            break

    if left is None or right is None:
        raise ValueError("Unable to find FWHM crossing points.")

    # Interpolated crossing x-values
    # x_left = interp1d(x[left[0]:left[1]+1], y[left[0]:left[1]+1] - half_max)([0])[0]
    # x_right = interp1d(x[right[0]:right[1]+1], y[right[0]:right[1]+1] - half_max)([0])[0]
    x_left = left
    x_right = right

    fwhm = x_right - x_left
    return fwhm, [half_max, half_max] , [x_right, x_left]


def TCSPC_decay_rate_2(time,intensity, fit=2):
    # Define the exponential decay function
    def exponential_decay(t, I0, I1, tau, t0):
        return I0 + I1 * np.exp(-(t - t0) / tau)

    
    def exponential_decay2(t, I0, I1, tau1, t1, I2, tau2, t2):
        return I0 + I1 * np.exp(-(t - t1) / tau1) + I2 * np.exp(-(t - t2) / tau2)


    index = np.argmax(intensity)#+6 # A few points afetr the peak
    time = time[index:]
    intensity = intensity[index:]#-min(intensity)

    # if fit == 1:
    #     p1 = (intensity.max(), 5)
    #     popt, pcov = curve_fit(exponential_decay1, time, intensity, p0=p1)
    #     print(popt, pcov)
    # elif fit == 2:
    #     p2 = (intensity.max()/3, 5, intensity.max()*2/3, 1)
    #     popt, pcov = curve_fit(exponential_decay2, time, intensity, p0=p2)
    #     print(popt, pcov)
    # else:
    #     p3 = (intensity.max()*2/3, 1, intensity.max()*1/6, 5, intensity.max()*1/6, 10)
    #     popt, pcov = curve_fit(exponential_decay3, time, intensity, p0=p3)
    #     print(popt, pcov)

    p2 = (intensity.min(), intensity.max(), 2.5, 2.0, intensity.max()/100, 0.1, 2.5)
    popt2, pcov2 = curve_fit(exponential_decay2, time, intensity, p0=p2)
    # print(popt2[0]/intensity.max(),popt2[1],popt2[2]/intensity.max(),popt2[3])#, pcov2)
    print(popt2)

    # print(decay_rate+decay_rate2)

    import matplotlib.pyplot as plt
    # Plot the data and the fit
    fig = plt.figure()
    plt.plot(time, intensity, label='Data',linewidth=2 ,color='blue')
    plt.plot(time, exponential_decay2(time, *p2), label='1 Exponential Fit', color='red')
    plt.plot(time, exponential_decay2(time, *popt2), label='2 Exponential Fit', color='orange')
    plt.xlabel('Time (ns)')
    plt.ylabel('Intensity (Counts)')
    plt.legend()
    plt.show()
    return True, True #popt2[:-3], pcov2[:-3] 



def TCSPC_decay_rate(time,intensity, fit=2):
    # Define the exponential decay function
    def exponential_decay(t, I0, I1, tau, t0):
        return I0 + I1 * np.exp(-(t - t0) / tau)

    index = np.argmax(intensity)#+10 # A few points afetr the peak
    time = time[index:]
    intensity = intensity[index:]#-min(intensity)


    p1 = (intensity.min(), intensity.max()*1.5, 2.5, 2.0)
    popt1, pcov1 = curve_fit(exponential_decay, time, intensity, p0=p1)




    # Compute fitted y values
    y_fit = exponential_decay(time, *popt1)

    # Compute residuals
    residuals = (intensity - y_fit)

    # Compute chi-squared
    chi_squared = np.std(residuals)

    # Print results
    print(f"Chi-squared: {chi_squared:.3f}")

    # print(decay_rate+decay_rate2)

    import matplotlib.pyplot as plt
    # Plot the data and the fit
    fig = plt.figure()
    plt.plot(time, intensity, label='Data',linewidth=2 ,color='blue')
    plt.plot(time, exponential_decay(time, *popt1), label='Exponential Fit', color='orange')
    # plt.plot(time, exponential_decay(time, *p1), label='Exponential Fit', color='red')
    plt.xlabel('Time (ns)')
    plt.ylabel('Intensity (Counts)')
    plt.legend()
    plt.title(f'{chi_squared}')
    # plt.show()
    return popt1, pcov1 


def electric_field_kV_per_cm(V):
    """
    Calculate electric field in kV/cm between IDE fingers.

    Parameters:
    V : float
        Applied voltage in volts.

    Returns:
    E : float
        Electric field in kV/cm.
    """
    gap_microns=50
    return (V / gap_microns) * 10




def refine_peak_positions(x, y, energy=True, window=5, resolution=1000):
    """
    Refines peak positions using cubic spline interpolation.
    
    Parameters:
        x (np.array): x-axis data (e.g., energy or voltage)
        y (np.array): y-axis data (e.g., electroabsorption)
        peak_indices (array-like): indices of rough peaks (e.g., from find_peaks)
        window (int): number of points to include on each side of peak
        resolution (int): number of interpolated points within window

    Returns:
        List of (x_peak_refined, y_peak_refined)
    """
    # If energy, then back to wavelength since we need even spacing in wavelength
    if energy:
        x = 1239.84193/x

    pos_peak_indices, _ = find_peaks(y, width=3)
    neg_peak_indices, _ = find_peaks(-y, width=3)
    
    refined_peaks_x = []
    refined_peaks_y = []
    
    x = np.asarray(x)
    y = np.asarray(y)

    for i in pos_peak_indices:
        if i < window or i + window >= len(x):
            continue  # skip edge cases

        x_win = x[i - window : i + window + 1]
        y_win = y[i - window : i + window + 1]

        spline = CubicSpline(x_win, y_win)
        x_dense = np.linspace(x_win[0], x_win[-1], resolution)
        y_dense = spline(x_dense)

        idx_max = np.argmax(y_dense)  # use abs if you want both pos/neg peaks
        refined_peaks_x.append(x_dense[idx_max])
        refined_peaks_y.append(y_dense[idx_max])

    for i in neg_peak_indices:
        if i < window or i + window >= len(x):
            continue  # skip edge cases

        x_win = x[i - window : i + window + 1]
        y_win = -y[i - window : i + window + 1]

        spline = CubicSpline(x_win, y_win)
        x_dense = np.linspace(x_win[0], x_win[-1], resolution)
        y_dense = spline(x_dense)

        idx_max = np.argmax(y_dense)  # use abs if you want both pos/neg peaks
        refined_peaks_x.append(x_dense[idx_max])
        refined_peaks_y.append(-y_dense[idx_max])

    refined_peaks_x = np.array(refined_peaks_x)
    refined_peaks_y = np.array(refined_peaks_y)

    sorted_indices = np.argsort(refined_peaks_x)
    x_sorted = refined_peaks_x[sorted_indices]
    y_sorted = refined_peaks_y[sorted_indices]

    if energy:
        x_sorted = 1239.84193/x_sorted  # Convert back to energy


    return x_sorted, y_sorted




import numpy as np

def match_peaks_across_curves(peak_sets, max_distance=0.05):
    """
    Match peaks across multiple curves by proximity in x.

    Parameters:
        peak_sets: list of np.array, each containing peak x-positions for one curve
        max_distance: max allowed difference between peaks to be considered a match

    Returns:
        matches: list of lists of matched peak x-positions, one per curve
                 e.g. [[1.01, 1.03, 1.00], [1.52, 1.53, 1.54]]
                 where each sublist is a group of matched peaks across curves
    """
    reference = peak_sets[0]
    num_curves = len(peak_sets)
    matches = []

    for xi in reference:
        group = [xi]  # start with reference peak
        valid = True

        for k in range(1, num_curves):
            xk = peak_sets[k]
            diffs = np.abs(xk - xi)
            if len(diffs) == 0 or np.min(diffs) > max_distance:
                valid = False
                break
            closest = xk[np.argmin(diffs)]
            group.append(closest)

        if valid:
            matches.append(group)

    return matches




def select_and_find_nearby_peaks(x_datasets, y_datasets, num_peaks=None, search_window=0.2, peak_type="both"):
    """
    User selects approximate peak locations on a plot.
    The function finds the nearest local peak (max or min) in each dataset near each click.

    Parameters:
        x_datasets: list of np.array — one for each curve
        y_datasets: list of np.array — one for each curve
        num_peaks: int or None — how many peaks to select (clicks)
        search_window: float — x-range to search around each click (in x-units)
        peak_type: 'max', 'min', or 'both'

    Returns:
        selected_x: list of clicked x-values
        refined_x_groups: list of lists of actual peak x-values (one per dataset, per peak)
        matched_y_groups: list of lists of actual peak y-values (same shape)
    """
    import matplotlib.pyplot as plt
    # Plot all datasets
    for x, y in zip(x_datasets, y_datasets):
        plt.plot(x, y)
    plt.title("Click on 6 approximate peak positions")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    # Collect click input
    if num_peaks is None:
        print("Click on peaks, then close the window when done.")
        clicks = plt.ginput(n=-1, timeout=0)
        print("Clicked positions:", clicks)
    else:
        print(f"Click on {num_peaks} peaks.")
        clicks = plt.ginput(n=num_peaks, timeout=0)

    plt.close()

    selected_x = [pt[0] for pt in clicks]
    refined_x_groups = []
    matched_y_groups = []

    for sel_x in selected_x:
        refined_x = []
        matched_y = []

        for x, y in zip(x_datasets, y_datasets):
            # Find indices within the search window
            mask = (x >= sel_x - search_window/2) & (x <= sel_x + search_window/2)
            if not np.any(mask):
                refined_x.append(np.nan)
                matched_y.append(np.nan)
                continue

            x_win = x[mask]
            y_win = y[mask]

            # print(f"x range: {sel_x - search_window/2} to {sel_x + search_window/2}, points found: {len(x_win)}")

            # Determine peaks (max or min)
            peak_indices = []
            if peak_type in ['max', 'both']:
                peaks, _ = find_peaks(y_win)
                peak_indices.extend(peaks)
            if peak_type in ['min', 'both']:
                inv_peaks, _ = find_peaks(-y_win)
                peak_indices.extend(inv_peaks)

            if peak_indices:
                # Choose the peak closest to clicked x
                peak_xs = x_win[peak_indices]
                closest_idx = np.argmin(np.abs(peak_xs - sel_x))
                true_idx = peak_indices[closest_idx]
                refined_x.append(x_win[true_idx])
                matched_y.append(y_win[true_idx])
            else:
                # No peak found
                refined_x.append(np.nan)
                matched_y.append(np.nan)

        refined_x_groups.append(refined_x)
        matched_y_groups.append(matched_y)

    return selected_x, refined_x_groups, matched_y_groups