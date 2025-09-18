"""
NumPy: transpose (.T)

- transpose() swaps array axes.
- For 2D arrays, it flips rows and columns.

Example 1: Transpose a 2D array
"""

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print("Original:\n", arr)
print("Transposed:\n", arr.T)


# Original:
#  [[1 2 3]
#  [4 5 6]]
# Transposed:
#  [[1 4]
#  [2 5]
#  [3 6]]