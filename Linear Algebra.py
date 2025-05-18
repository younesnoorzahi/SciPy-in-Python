import numpy as np
from scipy import linalg

A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])

# Solve linear system Ax = b
x = linalg.solve(A, b)
print(x)  # Output: [-4.  4.5]