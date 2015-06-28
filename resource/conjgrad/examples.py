#!/usr/bin/env python2

# Author: juscodit@gmail.com

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import copy
from math import pow, exp

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

delta = 0.025

### ==============================
### f(x) = 4x_1^2 + x_2^2
### ==============================

def CD1():
  return [(-1, -1), (0, -1), (0, 0)]

x = np.arange(-2, 2, delta)
y = np.arange(-2, 2, delta)
X, Y = np.meshgrid(x, y)
Z = 4 * X * X + Y * Y

plt.figure()
plt.contour(X, Y, Z, [15, 9, 6, 4, 2, 1, 0.1])

res = CD1()

xp, yp = zip(*res)
plt.plot(xp, yp, '--', lw=2)

for r in res:
  plt.plot(*r, marker='o', color='r')

plt.savefig("cd1.png")

### ==============================
### f(x) = 4x_1^2 + x_2^2 - 2 x_1 x_2
### ==============================

def grad(p):
  return (8 * p[0] - 2 * p[1], 2 * p[1] - 2 * p[0])

def CD2(p):
  result = [p]
  epsilon = 1e-2

  while np.linalg.norm(grad(p)) > epsilon:
    p = (0.25 * p[1], p[1])
    result.append(p)
    p = (p[0], p[0])
    result.append(p)

  return result

def CG(p):
  epsilon = 1e-2
  H = np.matrix([[8, -2], [-2, 2]])
  result = [p]
  g = np.array(grad(p))
  d = -copy.copy(g)
  while np.linalg.norm(g) > epsilon:
    alpha = -float(np.dot(g, d)) / np.dot(d, np.asarray(np.dot(H, d)).reshape(2))
    old_g = copy.copy(g)
    p = p + alpha * d
    result.append(tuple(p))
    g = np.array(grad(p))
    d = -g + np.dot(g, g) / np.dot(old_g, old_g) * d

  return result

plt.figure()
Z = 4 * X * X + Y * Y - 2 * X * Y
plt.contour(X, Y, Z, [15, 9, 6, 4, 2, 1, 0.1])

cd2_res = CD2((-1, -1))

xp, yp = zip(*cd2_res)
plt.plot(xp, yp, '--', lw=2)

for r in cd2_res:
  plt.plot(*r, marker='o', color='r')

plt.savefig("cd2.png")

plt.figure()
Z = 4 * X * X + Y * Y - 2 * X * Y
plt.contour(X, Y, Z, [15, 9, 6, 4, 2, 1, 0.1])

cg_res = CG((-1, -1))

xp, yp = zip(*cg_res)
plt.plot(xp, yp, '--', lw=2)

for r in cg_res:
  plt.plot(*r, marker='o', color='r')

plt.savefig("cg.png")
