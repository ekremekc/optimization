# -*- coding: utf-8 -*-
"""
Author: ee331
"""
# Real adjoint operator

import numpy as np

p = np.array([[1],
              [2]])

q = np.array([[3],
              [4]])

M = np.array([[3, 4],
              [5, 6]])

# When we do multiplication, we have to transpose the first vector (transforming from 2x1 to 1x2) 
# to get a scalar after performing multiplication

real_scalar = np.dot(p.T, M@q)

# we will check now if the real_scalar equals to p@M@q = M.T@p@q

real_scalar_check = np.dot((M.T@p).T, q)

assert real_scalar == real_scalar_check