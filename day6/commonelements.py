a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)