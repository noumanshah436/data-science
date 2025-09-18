"""
NumPy: reshape

- reshape() changes the shape of an array without changing the data.
- The total number of elements must remain the same.

Example 1: Reshaping 1D into 2D
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print("Original shape:", arr.shape)

reshaped = arr.reshape(2, 3)
print("Reshaped (2x3):\n", reshaped)


# Original shape: (6,)
# Reshaped (2x3):
#  [[1 2 3]
#  [4 5 6]]