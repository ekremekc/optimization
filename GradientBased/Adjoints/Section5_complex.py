# -*- coding: utf-8 -*-
"""
Author: ee331
"""
# Complex adjoint operator

import numpy as np

p = np.array([[1+1j],
              [2-2j]])

q = np.array([[3+3j],
              [4-4j]])

M = np.array([[3+1j, 4+2j],
              [5-1j, 6-3j]])

# When we do multiplication, we have to transpose the first vector (transforming from 2x1 to 1x2) 
# to get a scalar after performing multiplication

complex_scalar = np.dot(np.conjugate(p.T), M@q)


# we will check now if the complex_scalar equals to p^*@M@q == (M^H@p)^*@q

complex_scalar_check = np.dot(np.conjugate((np.conjugate(M.T)@p).T), q)

assert complex_scalar == complex_scalar_check