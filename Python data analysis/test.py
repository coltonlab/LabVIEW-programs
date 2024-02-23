import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the plot
fig, ax = plt.subplots()

# Plot the data
line1, = ax.plot(x, y1, label='Sin(x)', color='blue')
line2, = ax.plot(x, y2, label='Cos(x)', color='red')

# Create a ScalarMappable object
sm = plt.cm.ScalarMappable(cmap=plt.get_cmap('coolwarm'))
sm.set_array([])  # Set an empty array or list

# Add a color bar
cbar = fig.colorbar(sm, ax=ax, orientation='vertical', label='Color Bar')

# Show the plot
plt.show()
