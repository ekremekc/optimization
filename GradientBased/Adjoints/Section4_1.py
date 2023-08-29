#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This exercise is for finding the optimum initial condition
@author: ee331
"""

import numpy as np
from scipy.linalg import expm, solve, inv

# Reynolds number
Re = 400 
T = 200

# Define linear operator L
L = np.array([[-1/Re, 0],
              [1, -3/Re]])

g = np.random.uniform(size = 2)
# g = np.array([0.63127, 0.77556])

# Forward propagator from t=0 to t=T
Pdir = expm(T*L)

# https://en.wikipedia.org/wiki/Matrix_exponential
qT = Pdir@g

# Calculate cost function
g2 = np.dot(g,g) # g*g' or g@g.T
qT2 = np.dot(qT,qT) # q*q' or q@q.T

J = g2/qT2

##  calculate adjoint function

# Calculate initial condition
aT = -2*qT*g2/(qT2**2)

# Backward propagator from t=T to t=0
Padj = inv(expm(T*L.T))

a0 = Padj@aT

# Impose optimality condition

g = a0*qT2/2
g = g/np.linalg.norm(g)


