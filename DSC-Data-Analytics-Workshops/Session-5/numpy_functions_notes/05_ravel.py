"""
NumPy: ravel

- ravel() flattens an array into 1D.

Example 1: Flatten a 2D array
"""

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print("Original:\n", arr)
print("Raveled:", arr.ravel())


# Original:
#  [[1 2 3]
#  [4 5 6]]
# Raveled: [1 2 3 4 5 6]