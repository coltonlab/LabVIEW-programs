import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Example data
data = np.random.rand(10, 10) * 10  # Random data scaled to 0-10
levels = np.linspace(0, 10, 11)  # Define boundaries for colors
midpoints = (levels[:-1] + levels[1:]) / 2  # Midpoints for centered ticks

# Create colormap and normalize based on the levels
cmap = plt.cm.viridis
norm = mcolors.BoundaryNorm(levels, cmap.N)

# Plot the data
fig, ax = plt.subplots()
cax = ax.imshow(data, cmap=cmap, norm=norm)

# Add color bar with centered ticks
cbar = fig.colorbar(cax, ax=ax, ticks=midpoints)
cbar.set_ticklabels([f"{v:.1f}" for v in midpoints])  # Optional: format tick labels

plt.show()
