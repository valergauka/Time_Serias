import matplotlib.pyplot as plt
import numpy as np
from get_speeds import get_speeds

def visualize_speeds(df, period, speed_bins):
    speed_matrix = np.zeros((len(period), len(speed_bins)))

    for i, time_interval in enumerate(period):
        speeds = get_speeds(df, str(time_interval.start_time), str(time_interval.end_time))
        hist, _ = np.histogram(speeds, bins=speed_bins)
        speed_matrix[i, :] = hist

    fig, ax = plt.subplots(figsize=(12, 8))
    im = ax.imshow(speed_matrix, cmap='viridis', aspect='auto', extent=[0, len(speed_bins), 0, len(period)])
    plt.colorbar(im, ax=ax, label='Number of Buses')
    ax.set_xticks(np.arange(0, len(speed_bins) + 1, 5))
    ax.set_xticklabels(speed_bins[::5])
    ax.set_xlabel('Speed (mph)')
    ax.set_yticks(np.arange(0, len(period) + 1, 5))
    ax.set_yticklabels([str(period[i]) for i in range(0, len(period), 5)])
    ax.set_ylabel('Time Interval')

    plt.show()
    return im
