#!/usr/bin/env python2

# Author: juscodit@gmail.com

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math
import sys

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

delta = 0.025

### ==============================
### util functions
### ==============================

def norm(v0, v1):
  return math.sqrt(v0 * v0 + v1 * v1)

### ==============================
## steepest descent for elliptical case
### ==============================

def fe(x, y):
  return 4.0 * x * x + y * y - 2.0 * x * y

def gex(x, y):
  return 8.0 * x - 2.0 * y

def gey(x, y):
  return 2.0 * y - 2.0 * x

def alpha_e(x, y, dx, dy):
  return (2.0 * dx * y + 2.0 * x * dy - 8.0 * x * dx - 2.0 * y * dy) / \
         (8.0 * dx * dx + 2.0 * dy * dy - 4.0 * dx * dy)

def steepest_e(x0, y0):
  result = []
  result.append([x0, y0])
  xk, yk = x0, y0
  gxk, gyk = gex(xk, yk), gey(xk, yk)

  i = 0
  while norm(gxk, gyk) > 0.001:
    print "step %d [%f, %f]" % (i, xk, yk)
    i += 1

    dxk, dyk = -gxk, -gyk
    ak = alpha_e(xk, yk, dxk, dyk)
    xk += ak * dxk
    yk += ak * dyk
    gxk = gex(xk, yk)
    gyk = gey(xk, yk)
    result.append([xk, yk])
   
  print "step %d [%f, %f]" % (i, xk, yk)

  return result

### ==============================
### steepest descent for Rosenbrock function
### ==============================

def fr(x, y):
  return 100.0 * (y - x * x) * (y - x * x) + (1.0 - x) * (1.0 - x)

def grx(x, y):
  return 400.0 * x * x * x - 400.0 * x * y + 2.0 * x - 2.0

def gry(x, y):
  return 200.0 * y - 200.0 * x * x

def alpha_r(x, y, dx, dy, gx, gy):
  a = 0.5
  r = 0.3
  c1 = 1e-4
  while fr(x + a * dx, y + a * dy) > fr(x, y) + c1 * a * (gx * dx + gy * dy):
    a *= r
  return a

def steepest_r(x0, y0):
  result = []
  result.append([x0, y0])
  xk, yk = x0, y0
  gxk, gyk = grx(xk, yk), gry(xk, yk)

  i = 0
  while norm(gxk, gyk) > 0.001:
    print "step %d [%f, %f]" % (i, xk, yk)
    i += 1

    dxk, dyk = -gxk, -gyk
    ak = alpha_r(xk, yk, dxk, dyk, gxk, gyk)
    xk += ak * dxk
    yk += ak * dyk
    gxk = grx(xk, yk)
    gyk = gry(xk, yk)
    result.append([xk, yk])
   
  print "step %d [%f, %f]" % (i, xk, yk)

  return result

### ==============================
### circular case
### ==============================

x = np.arange(3.0, 11.0, delta)
y = np.arange(-1.0, 5.0, delta)
X, Y = np.meshgrid(x, y)
Z = (X - 7) * (X - 7) + (Y - 2) * (Y - 2)

plt.figure()
CS = plt.contour(X, Y, Z, [12, 8, 4, 2, 1, 0.1])
plt.plot([9, 7], [0.5, 2], '--', lw=2)
plt.plot([7], [2], marker='o', color='r')
plt.plot([9], [0.5], marker='o', color='r')
plt.savefig("circular.png")

### ==============================
### elliptical case
### ==============================

x = np.arange(-3.0, 3.0, delta)
y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z = 4 * X * X + Y * Y - 2 * X * Y

## for initial point (1, 0)

plt.figure()
CS = plt.contour(X, Y, Z, [9, 6, 4, 2, 1, 0.1])

res = steepest_e(1, 0)

xp, yp = zip(*res)
plt.plot(xp, yp, '--', lw=3)
for r in res:
  plt.plot(*r, marker='o', color='r')

plt.savefig("ellip1.png")

## for initial point (-1, -2)

plt.figure()
CS = plt.contour(X, Y, Z, [9, 6, 4, 2, 1, 0.1])

res = steepest_e(-1.0, -2.0)

xp, yp = zip(*res)
plt.plot(xp, yp, '--', lw=3)

for r in res:
  plt.plot(*r, marker='o', color='r')

plt.savefig("ellip2.png")

### ==============================
### Rosenbrock function
### ==============================

x = np.arange(-1.2, 1.0, delta)
y = np.arange(-0.6, 1.2, delta)
X, Y = np.meshgrid(x, y)
Z = 100 * (Y - X * X) * (Y - X * X) + (1 - X) * (1 - X)

## for initial point (0.6, 0.6)

plt.figure()
CS = plt.contour(X, Y, Z, [15, 9, 6, 4, 2, 1, 0.1])

res = steepest_r(0.6, 0.6)

xp, yp = zip(*res)
plt.plot(xp, yp, '--', lw=3)

for r in res:
  plt.plot(*r, marker='o', color='r')

plt.savefig("rosen1.png")

## for initial point (-1.2, 1)

plt.figure()
CS = plt.contour(X, Y, Z, [15, 9, 6, 4, 2, 1, 0.1])

res = steepest_r(-1.2, 1)

xp, yp = zip(*res)
plt.plot(xp, yp, ls='--', lw=3)

for r in res:
  plt.plot(*r, marker='o', color='r')

plt.savefig("rosen2.png")

# plt.show()

