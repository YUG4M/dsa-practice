data = [("Alice", 10), ("Bob", 5), ("Alice", 40), ("Bob", 20)]
result = {}

for name, marks in data:
    if name in result:
        result[name] += marks
    else:
        result[name] = marks

print(result)
