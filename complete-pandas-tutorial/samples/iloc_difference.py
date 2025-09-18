# iloc_difference.py

import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Ali", "Sara", "John", "Zara"],
    "Age": [22, 25, 24, 23],
    "CGPA": [3.1, 3.8, 3.5, 3.7]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df, "\n")

# Using iloc with single column index -> Series
print("df.iloc[2:4, 1] -> Series\n")
print(df.iloc[2:4, 1])
print("Type:", type(df.iloc[2:4, 1]), "\n")

# Using iloc with column slice -> DataFrame
print("df.iloc[2:4, 1:2] -> DataFrame\n")
print(df.iloc[2:4, 1:2])
print("Type:", type(df.iloc[2:4, 1:2]))
