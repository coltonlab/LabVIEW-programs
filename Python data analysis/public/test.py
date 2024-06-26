import numpy as np
from scipy.optimize import minimize

# Define your data sets
data1 = np.array([1, 2, 3, 4, 5])
data2 = np.array([6, 7, 8, 9, 10])
data3 = np.array([7, 10, 13, 16, 19])  # The resulting data3

# Define the function to minimize
def objective(x):
    a, b = x
    return np.sum((a * data1 + b * data2 - data3) ** 2)

# Initial guess for the coefficients
initial_guess = [1, 1]

# Use SciPy's minimize function to find the best fit coefficients
result = minimize(objective, initial_guess)

# Extract the optimal coefficients
a_optimal, b_optimal = result.x

print("Optimal coefficients:")
print("a =", a_optimal)
print("b =", b_optimal)
