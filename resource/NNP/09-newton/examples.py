#!/usr/bin/env python2

# Author: juscodit@gmail.com

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
from math import pow

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

# Rosenbrock function for point @p
def fr(p):
  return 100.0 * pow((p[1] - pow(p[0], 2)), 2) + pow((1.0 - p[0]), 2)

# gradient at point @p
def gr(p):
  x, y = p
  drx = 400.0 * pow(x, 3) - 400.0 * x * y + 2.0 * x - 2.0
  dry = 200.0 * y - 200.0 * pow(x, 2)
  return np.array([drx, dry])

# hessian matrix
def hr(p):
  x, y = p
  m11 = 1200.0 * pow(x, 2) - 400.0 * y + 2.0
  m12 = -400.0 * x
  m21 = -400.0 * x
  m22 = 200.0
  return np.matrix([[m11, m12], [m21, m22]])

# descent direction
def ddr(p):
  hessian = hr(p)
  heinv = np.linalg.inv(hessian)
  return np.squeeze(np.asarray(np.negative(np.dot(heinv, gr(p)))))

# step length at point @p with respect to descent direction @dd
def alpha_r(p, dd):
  a, r, c1 = 1, 0.3, 1e-4

  g = gr(p)
  p1 = p + a * dd
  while fr(p1) > fr(p) + c1 * a * np.dot(g, dd):
    a *= r
    p1 = p + a * dd

  return a

def classical_newton_r(p0):
  result = []
  result.append(p0)
  pk = p0

  i = 0
  while np.linalg.norm(gr(pk)) > 0.001:
    print "step %d [%f, %f]" % (i, pk[0], pk[1])
    i += 1
    dd = ddr(pk)
    a = alpha_r(pk, dd)
    pk = pk + a * dd
    result.append(pk)
  
  print "step %d [%f, %f]" % (i, pk[0], pk[1])

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
### quadratic approximation for Rosenbrock function at some point
### ==============================

x = np.arange(-1.2, 1.0, delta)
y = np.arange(-0.6, 1.2, delta)
X, Y = np.meshgrid(x, y)
Z = 100 * (Y - X * X) * (Y - X * X) + (1 - X) * (1 - X)

p = (-0.5, 0)
gp = gr(p)
hp = hr(p)
Zapp = fr(p) + (gp[0] * (X - p[0]) + gp[1] * (Y - p[1])) + \
       0.5 * (hp[0, 0] * (X - p[0]) * (X - p[0]) + 
              hp[0, 1] * (X - p[0]) * (Y - p[1]) +
              hp[1, 0] * (Y - p[1]) * (X - p[0]) +
              hp[1, 1] * (Y - p[1]) * (Y - p[1]))

plt.figure()
plt.contour(X, Y, Z, [15, 9, 6, 4, 2, 1, 0.1])
plt.contour(X, Y, Zapp, [10, 8, 6, 4, 2, 1], colors='green', linewidths=0.7)
plt.plot(*p, marker='o', color='r')

plt.savefig("rosen3.png")

### ==============================
### Rosenbrock function
### ==============================

x = np.arange(-1.2, 1.0, delta)
y = np.arange(-0.6, 1.2, delta)
X, Y = np.meshgrid(x, y)
Z = 100 * (Y - X * X) * (Y - X * X) + (1 - X) * (1 - X)

## for initial point (0.6, 0.6)

plt.figure()
plt.contour(X, Y, Z, [15, 9, 6, 4, 2, 1, 0.1])

# res = classical_newton_r((0.6, 0.6))
res = classical_newton_r((-0.5, 0))

xp, yp = zip(*res)
plt.plot(xp, yp, '--', lw=3)

for r in res:
  plt.plot(*r, marker='o', color='r')

plt.savefig("rosen1.png")

## for initial point (-1.2, 1)

plt.figure()
plt.contour(X, Y, Z, [15, 9, 6, 4, 2, 1, 0.1])

res = classical_newton_r((-1.2, 1))

xp, yp = zip(*res)
plt.plot(xp, yp, ls='--', lw=3)

for r in res:
  plt.plot(*r, marker='o', color='r')

plt.savefig("rosen2.png")

# plt.show()

