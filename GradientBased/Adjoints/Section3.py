"""
This exercise is finding the best control variable set to minimize cost function
@author: ee331
"""

import numpy as np
from scipy.linalg import solve

# Reynolds number
Re = 40 

# Define linear operator L
L = np.array([[-1/Re, 0],
              [1, -3/Re]])

# Define control variable randomly
# np.random.seed(100)
g = np.random.uniform(size = 2)
# g = np.array([0.63127, 0.77556])

# Solve the direct equation
q = solve(L, -g)

g2 = np.dot(g,g) # g*g' or g@g.T
q2 = np.dot(q,q) # q*q' or q@q.T

# Solve the adjoint equation
a = solve(L.T, -2*q*g2/(q2**2))

# define cost function to be minimized
J = g2/q2

# define energy amplification
R = 1/J

# Now we start updating g using direct and adjoint solutions
# update g using optimality
g = q2*a/2
g = g/np.linalg.norm(g)

# Solve the direct equation
q = solve(L, -g)

g2 = np.dot(g,g) # g*g' or g@g.T
q2 = np.dot(q,q) # q*q' or q@q.T

# Solve the adjoint equation
a = solve(L.T, -2*q*g2/(q2**2))

# define cost function to be minimized
J = g2/q2

# define energy amplification
R = 1/J



