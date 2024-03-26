import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt

def savitzky_golay_smoothing(y, window_length=15, polyorder=3):
    """
    Apply Savitzky-Golay smoothing to the given data.

    Parameters:
        y (array-like): Dependent variable (e.g., measured values).
        window_length (int): Length of the window over which the polynomial is fit.
        polyorder (int): Order of the polynomial that is fit to the data within each window.

    Returns:
        array-like: Smoothed data.
    """
    smoothed_y = savgol_filter(y, window_length, polyorder)
    return smoothed_y

# Example usage:
x = np.linspace(0, 10, 100)  # Independent variable (e.g., time)
y = np.sin(x) + np.random.normal(0, 0.1, size=x.shape)  # Dependent variable (e.g., measured values)

smoothed_data = savitzky_golay_smoothing(y)

# Plot original and smoothed data
plt.plot(x, y, label='Original Data')
plt.plot(x, smoothed_data, label='Smoothed Data')
plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Savitzky-Golay Smoothing')
plt.show()