"""
NumPy: vstack vs column_stack (with visualization)

- np.vstack((a, b)) stacks arrays vertically (row-wise).
- np.column_stack((a, b)) stacks arrays as columns (column-wise).

This script explains the difference with examples and a plot.
"""

import numpy as np
import matplotlib.pyplot as plt

# Define arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# vstack: stack as rows
stacked = np.vstack((a, b))

# column_stack: stack as columns
cstacked = np.column_stack((a, b))

print("vstack result:\n", stacked)
print("column_stack result:\n", cstacked)

# vstack result:
#  [[1 2 3]
#  [4 5 6]]
# column_stack result:
#  [[1 4]
#  [2 5]
#  [3 6]]

# # Visualization
# fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# # Plot vstack result
# axes[0].imshow(stacked, cmap="Blues", aspect="auto")
# axes[0].set_title("vstack result (rows)")
# for i in range(stacked.shape[0]):
#     for j in range(stacked.shape[1]):
#         axes[0].text(j, i, stacked[i, j], ha='center', va='center', color='black')

# # Plot column_stack result
# axes[1].imshow(cstacked, cmap="Greens", aspect="auto")
# axes[1].set_title("column_stack result (columns)")
# for i in range(cstacked.shape[0]):
#     for j in range(cstacked.shape[1]):
#         axes[1].text(j, i, cstacked[i, j], ha='center', va='center', color='black')

# plt.tight_layout()
# plt.show()
