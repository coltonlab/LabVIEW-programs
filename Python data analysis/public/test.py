import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Example data (replace with your actual data)
# x represents the independent variable (e.g., wavelength, time, etc.)
x = np.linspace(-1, 1, 100)

# 5 noisy datasets (replace with your actual y data)
noise = 0.01
y1 = np.sin(x + noise * np.random.normal(size=x.shape)) + noise * np.random.normal(size=x.shape)
y2 = np.sin(2*x + noise * np.random.normal(size=x.shape)) + noise * np.random.normal(size=x.shape)
y3 = np.sin(3*x + noise * np.random.normal(size=x.shape)) + noise * np.random.normal(size=x.shape)
y4 = np.sin(4*x + noise * np.random.normal(size=x.shape)) + noise * np.random.normal(size=x.shape)
y5 = np.sin(5*x + noise * np.random.normal(size=x.shape)) + noise * np.random.normal(size=x.shape)

# Function to compute the sum of squared differences
def sum_of_squares(params, x, *y_data):
    # params will be the intersection point we are solving for (x_intersect, y_intersect)
    x_intersect, y_intersect = params
    
    # Compute the squared differences for each dataset
    diffs = [(y - (y_intersect))**2 for y in y_data]
    return np.sum(np.concatenate(diffs))  # Sum all squared differences

# Initial guess for the intersection point (x, y)
initial_guess = [0.1, 0.1]  # Start near the middle of x and the average y-value

# Perform the optimization
result = minimize(sum_of_squares, initial_guess, args=(x, y1, y2, y3, y4, y5))

# Extract the intersection point from the result
x_intersect, y_intersect = result.x

# Print the result
print(f"Intersection point: x = {x_intersect}, y = {y_intersect}")

# Plot the datasets and the intersection point
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='Dataset 1', alpha=0.7)
plt.plot(x, y2, label='Dataset 2', alpha=0.7)
plt.plot(x, y3, label='Dataset 3', alpha=0.7)
plt.plot(x, y4, label='Dataset 4', alpha=0.7)
plt.plot(x, y5, label='Dataset 5', alpha=0.7)
plt.scatter(x_intersect, y_intersect, color='red', zorder=5, label=f'Intersection: ({x_intersect:.2f}, {y_intersect:.2f})')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Data Sets and Intersection Point')
plt.legend()
plt.show()
