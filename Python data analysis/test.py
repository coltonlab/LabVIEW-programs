import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d

# Define a sinusoidal function to fit with fixed amplitude
def sinusoidal_fixed_amplitude(x, amplitude, frequency, phase, offset):
    return amplitude * np.sin(frequency * x + phase) + offset

# Generate sample data for different polarizations
x_data = np.linspace(0, 10, 100)
polarizations = [90, 96, 105]  # Example polarizations
amplitudes = [1, 0.3, -0.7]  # Known amplitudes for each polarization

# Generate the data
data = {p: sinusoidal_fixed_amplitude(x_data, a, 1, 0, p) + np.random.normal(0, 0.1, len(x_data)) for p, a in zip(polarizations, amplitudes)}

# Fit sinusoidal curves to the data
fit_params = {}
for p, y_data in data.items():
    # Fix amplitude to the known value and fit frequency and phase
    params, _ = curve_fit(lambda x, freq, phase, offset: sinusoidal_fixed_amplitude(x, amplitudes[polarizations.index(p)], freq, phase, offset), x_data, y_data, p0=[1, 0, p])
    fit_params[p] = params

# Interpolate values
interp_x = np.linspace(0, 10, 1000)
interpolated_curves = {}

# Create interpolation function for polarizations
polarization_values = np.array(sorted(polarizations))
for p in polarization_values:
    fit_params_p = fit_params[p]
    fitted_curve = sinusoidal_fixed_amplitude(interp_x, amplitudes[polarizations.index(p)], *fit_params_p)
    interpolated_curves[p] = fitted_curve

# Create an interpolation function for the polarization axis
interp_function = interp1d(polarization_values, list(interpolated_curves.values()), axis=0, kind='linear')

# Interpolate between polarizations
interp_polarizations = np.linspace(min(polarizations), max(polarizations), 50)
interpolated_between = np.array([interp_function(p) for p in interp_polarizations])

# Calculate the variance of the derivative for each interpolated curve
def calculate_variance_of_derivative(curves, x):
    variances = []
    for curve in curves.T:
        derivative = np.gradient(curve, x)
        variance = np.var(derivative)
        variances.append(variance)
    return np.array(variances)

# Get the variances
variances = calculate_variance_of_derivative(interpolated_between, interp_x)

# Find the polarization with the smallest variance in derivative
min_variance_index = np.argmin(variances)
flattest_polarization = interp_polarizations[min_variance_index]

# Plotting
plt.figure(figsize=(14, 7))

# Plot the fitted curves for each polarization
for p in polarizations:
    plt.plot(x_data, data[p], 'o', label=f'Data Polarization {p}')
    plt.plot(x_data, sinusoidal_fixed_amplitude(x_data, amplitudes[polarizations.index(p)], *fit_params[p]), '-', label=f'Fit Polarization {p}')

# Plot the interpolated curves
for idx, p in enumerate(interp_polarizations):
    plt.plot(interp_x, interpolated_between[idx], '--', label=f'Interpolated Polarization {p:.2f}')

# Highlight the flattest polarization curve
plt.plot(interp_x, interpolated_between[min_variance_index], 'r--', linewidth=2, label=f'Flattest Curve Polarization {flattest_polarization:.2f}')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.title('Sinusoidal Curve Fitting with Fixed Amplitude and Interpolation')
plt.show()
