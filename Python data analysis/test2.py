import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Example data
polarizations = np.array([0, 45, 90])  # Polarizations in degrees

# Each row corresponds to a polarization and each column to a data point
data = np.array([
    [10, 11, 12, 13, 14],  # Data for 0 degrees
    [20, 21, 22, 23, 24],  # Data for 45 degrees
    [30, 31, 32, 33, 34]   # Data for 90 degrees
])

# Define the new polarizations you want to interpolate
new_polarizations = np.linspace(0, 90, num=100)  # Interpolation between 0 and 90 degrees

# Prepare an array to hold interpolated results
interpolated_data = np.zeros((len(new_polarizations), data.shape[1]))

# Perform interpolation for each column (data point)
for i in range(data.shape[1]):
    interp_function = interp1d(polarizations, data[:, i], kind='linear', fill_value='extrapolate')
    interpolated_data[:, i] = interp_function(new_polarizations)

# Plotting the results
plt.figure(figsize=(12, 8))

# Plot each interpolated data series
for i in range(data.shape[1]):
    plt.plot(new_polarizations, interpolated_data[:, i], label=f'Interpolated Data Point {i+1}')

# Scatter plot original data for each data point
for i in range(data.shape[1]):
    plt.scatter(polarizations, data[:, i], marker='o', label=f'Original Data Point {i+1}')

plt.xlabel('Polarization (degrees)')
plt.ylabel('Data Value')
plt.title('Interpolation of Data Across Polarizations')
plt.legend()
plt.grid(True)
plt.show()
