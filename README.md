🗂 Remove Keys with Duplicate Values in a Dictionary (Python)
📌 Description

This program removes keys from a dictionary if their values are duplicates, keeping only the first occurrence of each value.
It is useful for cleaning data where unique values are required.

🧩 Problem Statement

Given a dictionary:

{"A": 10, "B": 20, "C": 10}


Remove keys that have duplicate values.

✅ Code
data = {"A": 10, "B": 20, "C": 10}
result = {}
seen = set()

for k, v in data.items():
    if v not in seen:
        result[k] = v
        seen.add(v)

print(result)

🧠 Explanation

data.items() returns key-value pairs

seen keeps track of values already added

For each (key, value), check if the value is in seen

If not, add it to result and mark it as seen

Duplicate values are skipped, keeping only the first key with that value

🖨 Example Output
{'A': 10, 'B': 20}

🛠 Concepts Used

Dictionaries

Loops

Sets

Conditional statements

Key-value manipulation

🎯 Use Cases

Data cleaning
Removing duplicates in datasets
Interview preparation
Dictionary manipulation practice

🚀 Possible Improvements

Keep last occurrence instead of first

Handle more complex nested dictionaries

Convert into a function for reuse

Optimize for large datasets

👨‍💻 Author

Pranay Jadhao

<img width="671" height="623" alt="image" src="https://github.com/user-attachments/assets/ced69a30-c3ee-4d8a-aa13-2abd61ce1dee" />
