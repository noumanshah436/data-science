"""
NumPy: linspace

- np.linspace(start, stop, num) creates evenly spaced numbers between start and stop.
- num defines how many points.

Example 1: Generate 5 values from 0 to 1
"""

import numpy as np

lin = np.linspace(0, 1, 5)
print("Linspace:", lin)
# Linspace: [0.   0.25 0.5  0.75 1.  ]