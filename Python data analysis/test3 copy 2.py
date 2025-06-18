import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# Define function to fit (example: quadratic)
def func(x, a, b, c):
    return a * x**2 + b * x + c

# Example data
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2.2, 2.8, 3.6, 5.1, 7.3])
y_err = np.array([0.2, 0.3, 0.25, 0.3, 0.4])  # Measurement uncertainties

# Perform curve fitting
popt, pcov = opt.curve_fit(func, x_data, y_data, sigma=y_err, absolute_sigma=True)

# Generate x values for smooth curve
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = func(x_fit, *popt)

# Calculate confidence intervals
perr = np.sqrt(np.diag(pcov))  # Standard deviation (errors) of fit parameters

# Monte Carlo error propagation for confidence band
n_samples = 1000  # Number of Monte Carlo samples
params_samples = np.random.multivariate_normal(popt, pcov, n_samples)
y_samples = np.array([func(x_fit, *params) for params in params_samples])

# Compute confidence bounds (e.g., 95% CI)
y_lower = np.percentile(y_samples, 2.5, axis=0)
y_upper = np.percentile(y_samples, 97.5, axis=0)

# Plot data with error bars
plt.errorbar(x_data, y_data, yerr=y_err, fmt='o', label="Data", capsize=5)

# Plot fitted curve
plt.plot(x_fit, y_fit, label="Fitted Curve", color='red')

# Plot confidence interval as shaded region
plt.fill_between(x_fit, y_lower, y_upper, color='red', alpha=0.3, label="95% Confidence Interval")

# Formatting
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Curve Fit with Confidence Interval")
plt.legend()
plt.grid(True)

# Show plot
plt.show()
