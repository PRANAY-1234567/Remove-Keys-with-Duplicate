data = {"A": 10, "B": 20, "C": 10}
result = {}
seen = set()

for k, v in data.items():
    if v not in seen:
        result[k] = v
        seen.add(v)

print(result)
