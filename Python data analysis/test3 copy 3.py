import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

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
    # Plot all datasets
    for x, y in zip(x_datasets, y_datasets):
        plt.plot(x, y)
    plt.title("Click on the approximate peak positions")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    # Collect click input
    if num_peaks is None:
        print("Click on peaks, then close the window when done.")
        clicks = plt.ginput(n=-1, timeout=0)
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

            print(f"x range: {sel_x - search_window/2} to {sel_x + search_window/2}, points found: {len(x_win)}")

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

x1 = np.linspace(0, 10, 50)
x2 = x1 + 0.01*np.random.randn(50)
x3 = x1 + 0.02*np.random.randn(50)

y1 = np.sin(x1)**2
y2 = np.sin(x2)**2 + 0.1
y3 = np.sin(x3)**2 - 0.1

x_datasets, y_datasets = [x1, x2, x3], [y1, y2, y3]

selected_x, refined_x, matched_y = select_and_find_nearby_peaks(
    x_datasets, y_datasets, num_peaks=6, search_window=2, peak_type='both'
)


# Plot all curves
for x, y in zip(x_datasets, y_datasets):
    plt.plot(x, y)
    plt.scatter(selected_x, [y[np.argmin(np.abs(x - sel_x))] for sel_x in selected_x], color='red', zorder=5)
    plt.scatter(refined_x, matched_y, color='black', zorder=10)

plt.title("Click on desired peak positions")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()


