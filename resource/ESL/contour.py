#!/usr/bin/env python2
"""
Illustrate simple contour plotting, contours on an image with
a colorbar for the contours, and labelled contours.

See also contour_image.py.
"""
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

delta = 0.025
x = np.arange(-8.0, 11.0, delta)
y = np.arange(-8.0, 20.0, delta)
X, Y = np.meshgrid(x, y)

R = np.abs(X) + np.abs(Y)

plt.figure()
CS = plt.contour(X, Y, R, [8, 6, 4, 2, 1, 0.1], colors="k")

plt.savefig("l1contour.svg")

plt.show()

