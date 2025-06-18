from scipy.signal import savgol_filter
import numpy as np
import matplotlib.pyplot as plt

# Generate some noisy data
x = np.linspace(0, 10, 100)
y = np.sin(x) + 0.0051 * np.random.normal(size=len(x))

# Apply Savitzky-Golay filter
window_size = 11  # Must be odd
poly_order = 3

smoothed_y = savgol_filter(y, window_size, poly_order)
first_derivative = savgol_filter(y, window_size, poly_order, deriv=1)
second_derivative = savgol_filter(y, window_size+4, poly_order, deriv=2)
third_derivative = savgol_filter(y, window_size+8, poly_order, deriv=3)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Noisy Data", linestyle='dashed', alpha=0.5)
plt.plot(x, smoothed_y, label="Smoothed Data")
plt.plot(x, first_derivative/np.max(first_derivative), label="1st Derivative")
plt.plot(x, second_derivative/np.max(second_derivative), label="2nd Derivative")
plt.plot(x, third_derivative/np.max(third_derivative), label="3rd Derivative")
plt.legend()
plt.show()


# # Plot results
# plt.figure(figsize=(10, 6))
# plt.plot(x, y, label="Noisy Data", linestyle='dashed', alpha=0.5)

# for i in range(0,12,4):
#     print(window_size+i)
#     derivative = savgol_filter(y, window_size+i+2, poly_order, deriv=3)
#     plt.plot(x, derivative/np.max(derivative), label=f"Window {window_size+i}")
# plt.legend()
# plt.show()