#!/usr/bin/env python2

# Author: juscodit@gmail.com

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
from math import pow
from math import exp

delta = 0.025

### ==============================
### Ellipse function (f(x) = x1^2 + 50 x2^2)
### ==============================

def func(p):
  return p[0] ** 2 + 50 * p[1] ** 2

def gr(p):
  x, y = p
  dx = 2 * x
  dy = 100 * y
  return np.array([dx, dy])

def he(p):
  return np.matrix([[2, 0], [0, 100]])

# descent direction
def nddir(p):
  hessian = he(p)
  heinv = np.linalg.inv(hessian)
  return np.squeeze(np.asarray(np.negative(np.dot(heinv, gr(p)))))

# step length at point @p with respect to descent direction @dd
def alpha(p, dd):
  a, r, c1 = 1, 0.3, 1e-4

  g = gr(p)
  p1 = p + a * dd
  while func(p1) > func(p) + c1 * a * np.dot(g, dd):
    a *= r
    p1 = p + a * dd

  return a

def steepest_descent(p0):
  result = []
  result.append(p0)
  pk = p0

  i = 0
  while np.linalg.norm(gr(pk)) > 0.001:
    print "step %d [%f, %f]" % (i, pk[0], pk[1])
    i += 1
    dd = -gr(pk)
    a = alpha(pk, dd)
    pk = pk + a * dd
    result.append(pk)

  print "step %d [%f, %f]" % (i, pk[0], pk[1])

  return result

def classical_newton(p0):
  result = []
  result.append(p0)
  pk = p0

  i = 0
  while np.linalg.norm(gr(pk)) > 0.001:
    print "step %d [%f, %f]" % (i, pk[0], pk[1])
    i += 1
    dd = nddir(pk)
    # a = alpha(pk, dd)
    pk = pk + dd
    result.append(pk)
  
  print "step %d [%f, %f]" % (i, pk[0], pk[1])

  return result

# initial point
p0 = (-2.5, 0.05)

# get result of classical newton
nres = classical_newton(p0)

# get result of steepest descent
sres = steepest_descent(p0)

x = np.arange(-3, 3, delta)
y = np.arange(-0.7, 0.7, delta)
X, Y = np.meshgrid(x, y)
Z = X ** 2 + 50 * Y ** 2

# plot figure for classicl newton
fig = plt.figure()
plt.contour(X, Y, Z, [13, 9, 6, 4, 2, 1, 0.1])
plt.annotate("", xytext=nres[0], xy=nres[1], arrowprops=dict(arrowstyle='->', linewidth=3, color="red"))
for r in nres:
  plt.plot(*r, marker='o', color='g')

plt.text(p0[0] - 0.3, p0[1] + 0.02, "(%.1f, %.1f)" % (p0[0], p0[1]), color="purple", fontsize=10)
plt.text(-1.5, 0.1, "1 step", fontsize=20)

plt.savefig("newton.png")

# plot figure for steepest descent
fig = plt.figure()
plt.contour(X, Y, Z, [13, 9, 6, 4, 2, 1, 0.1])
for i in xrange(len(sres) - 1):
  plt.annotate("", xytext=sres[i], xy=sres[i+1], arrowprops=dict(arrowstyle="-"))
for r in sres:
  plt.plot(*r, marker='o', color='g')

plt.text(p0[0] - 0.3, p0[1] + 0.02, "(%.1f, %.1f)" % (p0[0], p0[1]), color="purple", fontsize=10)
plt.text(-1.5, 0.15, "%d step" % len(sres), fontsize=20)

plt.savefig("steepest.png")

### ==============================
### Function x^2 and 10x^2
### ==============================

def steepest_gradient_x2(x0):
  def func(x):
    return x ** 2

  def gr(x):
    return 2 * x

  def alpha(x, d):
    a, r, c1 = 1, 0.3, 1e-4
    while func(x + a * d) > func(x) + c1 * a * gr(x) * d:
      a *= r
    return a

  def ddir(x):
    return -gr(x)

  result = []
  xk = x0
  i = 1
  while np.linalg.norm(gr(xk)) > 0.001:
    print "step %d [%f] loss [%f]" % (i, xk, func(xk))
    i += 1
    result.append((xk, func(xk)))
    dd = ddir(xk)
    a = alpha(xk, dd)
    xk = xk + a * dd

  result.append((xk, func(xk)))

  return result

def steepest_gradient_10x2(x0):
  def func(x):
    return 10 * x ** 2

  def gr(x):
    return 20 * x

  def alpha(x, d):
    a, r, c1 = 1, 0.3, 1e-4
    while func(x + a * d) > func(x) + c1 * a * gr(x) * d:
      a *= r
    return a

  def ddir(x):
    return -gr(x)

  result = []
  xk = x0
  i = 1
  while np.linalg.norm(gr(xk)) > 0.001:
    print "step %d [%f] loss [%f]" % (i, xk, func(xk))
    i += 1
    result.append((xk, func(xk)))
    dd = ddir(xk)
    a = alpha(xk, dd)
    xk = xk + a * dd

  result.append((xk, func(xk)))

  return result

x = np.arange(-1.6, 1.6, delta)
y1 = x ** 2
y2 = 10 * x ** 2

# plot for steepest descent on x^2
fig = plt.figure()
plt.plot(x, y1, linewidth=2)
plt.ylim(0, 2.8)
sg_x2_res = steepest_gradient_x2(-1.5)

for i in xrange(len(sg_x2_res) - 1):
  plt.annotate("", xytext=sg_x2_res[i], xy=sg_x2_res[i+1], arrowprops=dict(arrowstyle="->"))
for r in sg_x2_res:
  plt.plot(*r, marker='o', color='g')

plt.text(-1.0, 2.5, "$f(x) = x^2$", fontsize=25)
plt.text(-1.0, 2.15, "%d step" % len(sg_x2_res), fontsize=20)
plt.savefig('steepest_x2.png')

# plot for steepest descent on 10x^2
fig = plt.figure()
plt.plot(x, y2, linewidth=2)
plt.ylim(0, 28)
sg_10x2_res = steepest_gradient_10x2(-1.5)

for i in xrange(len(sg_10x2_res) - 1):
  plt.annotate("", xytext=sg_10x2_res[i], xy=sg_10x2_res[i+1], arrowprops=dict(arrowstyle="->"))
for r in sg_10x2_res:
  plt.plot(*r, marker='o', color='g')

plt.text(-1.0, 25, "$f(x) = 10 x^2$", fontsize=25)
plt.text(-1.0, 21.5, "%d step" % len(sg_10x2_res), fontsize=20)
plt.savefig('steepest_10x2.png')

# plot for curvature axis

x = np.arange(-3, 3, delta)
y = np.arange(-3, 3, delta)
X, Y = np.meshgrid(x, y)
Z = 4 * X ** 2 + 2 * Y ** 2 - 4 * X * Y

w, v = np.linalg.eig(np.array([[8, -4], [-4, 4]]))

print w, v[0], v[1]

plt.figure(figsize=(4, 4))
plt.contour(X, Y, Z, [13, 9, 6, 4, 2, 1, 0.1])
plt.annotate("", xytext=(0, 0), xy=(v[0, 1], v[1, 1]), arrowprops=dict(arrowstyle="->", color="red", linewidth=2))
plt.annotate("", xytext=(0, 0), xy=(v[0, 0], v[1, 0]), arrowprops=dict(arrowstyle="->", color="red", linewidth=2))
plt.plot(0, 0, marker='o', color='r')
plt.text(-2.5, 2.2, "$f(x) = 4x_1^2 + 2x_2^2 - 4x_1 x_2$", fontsize=13)
plt.text(0.7, 0.9, "curvature axis", color="red", fontsize=10)
plt.savefig('axis.png')

plt.show()
