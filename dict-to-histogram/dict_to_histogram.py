"Converts a dict to a histogram"

import numpy as np
import matplotlib.pyplot as plt

def dict_histogram(d, bin_size, lower=None, higher=None):
    if bin_size < np.finfo(float).eps:
        raise ValueError("bin_size should not be 0.")
    
    bin_size_inv = 1.0 / bin_size
        
    if not lower:
        lower = np.floor(min(d.keys()) * bin_size_inv) * bin_size
    
    if not higher:
        higher = np.ceil(max(d.keys()) * bin_size_inv) * bin_size
    
    if lower >= higher:
        raise ValueError("lower should be smaller than higher.")
    
    bins = np.arange(lower, higher, bin_size)
    indices = ((np.array(d.keys()) - lower) * bin_size_inv).astype(int)
    
    return np.bincount(indices, weights=d.values()), bins

from data import time_diff

WIDTH = 500

plt.subplot(2, 1, 1)
hist, bins = dict_histogram(time_diff.time_diff, WIDTH)
plt.bar(bins, hist + 1, width=WIDTH, color='b', edgecolor='none')
plt.xlabel(r'$t_n - t_{n-1}$ (s)')
plt.ylabel(r'$\# + 1$')
plt.title("Time diff (bin_size={})".format(WIDTH))
plt.yscale('log')

plt.subplot(2, 1, 2)
hist, bins = dict_histogram(time_diff.time_diff_from_now, WIDTH)
plt.bar(bins, hist + 1, width=WIDTH, color='g', edgecolor='none')
plt.xlabel(r"now() - $t_{n}$ (s)")
plt.ylabel(r'$\# + 1$')
plt.title("Time diff from now (bin_size={})".format(WIDTH))
plt.yscale('log')

plt.subplots_adjust(hspace=0.25)
plt.show()
