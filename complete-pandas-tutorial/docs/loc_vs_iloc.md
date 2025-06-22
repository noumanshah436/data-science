In **Pandas**, `.loc` and `.iloc` are both used for selecting data from a `DataFrame`, but they differ in how they interpret the indexing.

---

### ✅ `.loc` — **Label-based indexing**

* You use `.loc[]` when you want to select data **by the labels** (i.e., row/column names).
* It includes the **start and end** when slicing.

**Syntax:**

```python
df.loc[row_label, column_label]
```

**Examples:**

```python
df.loc[2]                # Get row with index label 2
df.loc[2:4]              # Get rows from label 2 to 4 (inclusive)
df.loc[:, 'name']        # All rows, column 'name'
df.loc[2:4, ['name', 'age']]  # Rows 2 to 4, specific columns
```

---

### ✅ `.iloc` — **Integer position-based indexing**

* You use `.iloc[]` when you want to select data **by the integer location** (like array indices).
* It is **zero-based** and the **end is exclusive** when slicing.

**Syntax:**

```python
df.iloc[row_index, column_index]
```

**Examples:**

```python
df.iloc[2]                # Get 3rd row (index 2)
df.iloc[2:4]              # Get 3rd and 4th rows (index 2 and 3)
df.iloc[:, 1]             # All rows, second column
df.iloc[2:4, [1, 2]]      # Rows 2 to 3, columns 1 and 2
```

---

### 🔁 Summary Table

| Feature        | `.loc[]`                       | `.iloc[]`                            |
| -------------- | ------------------------------ | ------------------------------------ |
| Index type     | Label-based (row/column names) | Integer-based (row/column positions) |
| Slice behavior | Inclusive                      | Exclusive                            |
| Use case       | Named indexes/columns          | Positional selection                 |

---

### 🧠 Quick Tip

If you get `KeyError`, you're likely using `.loc` on a label that doesn't exist.
If you get `IndexError`, you're likely using `.iloc` on a position out of bounds.

---

# Here's a clear example using a sample `DataFrame` to show how `.loc` and `.iloc` work differently.

---

### 🧪 Sample DataFrame

```python
import pandas as pd

# Create a sample DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40],
    'city': ['NY', 'LA', 'Chicago', 'Houston']
}

df = pd.DataFrame(data, index=[101, 102, 103, 104])
print(df)
```

This will produce:

```
      name  age     city
101  Alice   25       NY
102    Bob   30       LA
103 Charlie   35  Chicago
104  David   40  Houston
```

---

### ✅ `.loc` Examples (Label-based)

```python
# Get row with label 102
print(df.loc[102])
```

Output:

```
name     Bob
age        30
city      LA
Name: 102, dtype: object
```

```python
# Get rows from 102 to 104 (inclusive)
print(df.loc[102:104])
```

```python
# Get specific rows and columns by label
print(df.loc[101:103, ['name', 'city']])
```

---

### ✅ `.iloc` Examples (Integer position-based)

```python
# Get row at index 1 (second row)
print(df.iloc[1])
```

Output:

```
name     Bob
age        30
city      LA
Name: 102, dtype: object
```

```python
# Get rows at positions 1 and 2 (not including position 3)
print(df.iloc[1:3])
```

```python
# Get first and third rows, and first two columns
print(df.iloc[[0, 2], [0, 1]])
```

---

### ⚠️ Key Difference Example

```python
# This works because 102 is a label
df.loc[102]  # ✅

# This fails because 102 is out of bounds as a position
df.iloc[102]  # ❌ IndexError
```



## **Real-world use cases** of `.loc` and `.iloc` using the same `DataFrame` from earlier, and I'll include **visual explanations** (with code comments and reasoning).



### 🧪 DataFrame Reminder

```python
import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40],
    'city': ['NY', 'LA', 'Chicago', 'Houston']
}

df = pd.DataFrame(data, index=[101, 102, 103, 104])
```

```
      name  age     city
101  Alice   25       NY
102    Bob   30       LA
103 Charlie   35  Chicago
104  David   40  Houston
```

---

## 🔍 Real-World Use Cases

---

### ✅ 1. **Filter people aged 30 and above** — using `.loc`

```python
df.loc[df['age'] >= 30]
```

**Why `.loc`?**
You're filtering by condition (on a label) and retrieving matching rows.

**Output:**

```
      name  age     city
102    Bob   30       LA
103 Charlie   35  Chicago
104  David   40  Houston
```

---

### ✅ 2. **Get 2nd and 4th row by position** — using `.iloc`

```python
df.iloc[[1, 3]]
```

**Why `.iloc`?**
You’re selecting rows by their **position**, not their index labels.

**Output:**

```
      name  age     city
102    Bob   30       LA
104  David   40  Houston
```

---

### ✅ 3. **Get names of people in Chicago or Houston** — using `.loc`

```python
df.loc[df['city'].isin(['Chicago', 'Houston']), 'name']
```

**Output:**

```
103    Charlie
104      David
Name: name, dtype: object
```

---

### ✅ 4. **Update value using label** — with `.loc`

```python
df.loc[103, 'age'] = 36
```

**What this does:** Updates Charlie's age to 36.

---

### ✅ 5. **Get last two rows and first two columns** — using `.iloc`

```python
df.iloc[-2:, :2]
```

**Output:**

```
      name  age
103 Charlie   36
104  David   40
```

---

### ✅ 6. **Visual: Difference between `df.loc[102]` and `df.iloc[1]`**

```python
print(df.loc[102])   # uses label
print(df.iloc[1])    # uses position
```

Both give the same output **in this case**, but it's coincidence — if index labels were not 101, 102..., the output could differ!

---

## 🧠 Rule of Thumb

| Use Case                    | Use `.loc` | Use `.iloc` |
| --------------------------- | ---------- | ----------- |
| Filter by values in columns | ✅          | ❌           |
| Select by index label       | ✅          | ❌           |
| Select by row/column number | ❌          | ✅           |
| Update a value by label     | ✅          | ❌           |
| Slice by position           | ❌          | ✅           |
| Get last row: `df.iloc[-1]` | ❌          | ✅           |

---

Would you like a **plotting example** or to see how `.loc`/`.iloc` help in **time series or multi-index data**?
