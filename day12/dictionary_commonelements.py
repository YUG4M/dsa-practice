dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 100, 'c': 400, 'd': 300}

common = {}

for key in dict1:
    if key in dict2 and dict1[key] == dict2[key]:
        common[key] = dict1[key]

print(common)
