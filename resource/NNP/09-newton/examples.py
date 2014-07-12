#!/usr/bin/env python2

# Author: juscodit@gmail.com

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
from math import pow
from math import exp

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

delta = 0.025

### ==============================
### Classical Newton for Rosenbrock function
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

res = classical_newton_r((0.6, 0.6))

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

### ==============================
### Classical Newton for log(exp(x) + exp(-x))
### ==============================

def gl(x):
  return (exp(x) - exp(-x)) / (exp(x) + exp(-x))

def hl(x):
  return 1 - pow(gl(x), 2)

def classical_newton_l(x0, niter):
  result = []
  hessian = []
  xk = x0
  i = 0
  while gl(xk) != 0 and i < niter:
    result.append(xk)
    hessian.append(hl(xk))
    xk = xk - gl(xk) / hl(xk)
    i += 1
  result.append(xk)
  hessian.append(hl(xk))
  return (result, hessian)

plt.figure()

x = np.arange(-2, 6, .01)
y = np.log(np.exp(x) + np.exp(-x))

(res, hessian) = classical_newton_l(1.1, 4)
print res
print hessian

for r in res:
  plt.plot(r, 0, marker='o', color='r')

tag = 'x0'
plt.annotate(tag, xy=(res[0], 0.05), xytext=(0.5, 0.2), arrowprops=dict(arrowstyle="->"))

tag = 'x1'
plt.annotate(tag, xy=(res[1], 0.05), xytext=(res[1], 0.2))

tag = 'x2'
plt.annotate(tag, xy=(res[2], 0.05), xytext=(1.5, 0.2), arrowprops=dict(arrowstyle="->"))

tag = 'x3'
plt.annotate(tag, xy=(res[3], 0.05), xytext=(res[3], 0.2))

tag = 'x4'
plt.annotate(tag, xy=(res[4], 0.05), xytext=(res[4], 0.2))

plt.plot(x, y, linewidth=2)

plt.savefig("log.png")

# plt.show()

