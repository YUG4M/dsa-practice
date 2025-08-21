words = ["listen", "silent", "hello", "world", "drowl", "abc"]
sorted_map = {}

for word in words:
    key = ''.join(sorted(word))
    if key in sorted_map:
        sorted_map[key].append(word)
    else:
        sorted_map[key] = [word]

unique = []
for group in sorted_map.values():
    if len(group) == 1:
        unique.append(group[0])

print(unique)
