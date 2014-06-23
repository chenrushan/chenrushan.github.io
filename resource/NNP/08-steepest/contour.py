#!/usr/bin/env python
"""
Illustrate simple contour plotting, contours on an image with
a colorbar for the contours, and labelled contours.

See also contour_image.py.
"""
import matplotlib
#matplotlib.use('svg')
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

delta = 0.025
x = np.arange(3.0, 11.0, delta)
y = np.arange(-1.0, 5.0, delta)
X, Y = np.meshgrid(x, y)
Z = (X - 7) * (X - 7) + (Y - 2) * (Y - 2)

plt.figure()
CS = plt.contour(X, Y, Z, [16, 12, 8, 4, 2, 1, 0.1])
plt.plot([7], [2], marker='o', color='r')
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Simplest default with labels')
plt.savefig("test.svg")

plt.show()

