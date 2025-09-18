"""
NumPy: np.array

- np.array() creates a NumPy array from a list or tuple.
- Arrays are more powerful than lists: they support vectorized operations.

Example 1: Creating 1D and 2D arrays
"""

import numpy as np

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)
print("1D shape:", arr1.shape) # (5, )

# 2D array
arr2 = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
    ]
)
print("2D Array:\n", arr2)
print("2D shape:\n", arr2.shape)  # 2, 3
