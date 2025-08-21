a = [1, 2, 2, 3, 4]
b = [2, 4, 4, 6]
c=[]
for i in a:
    if i in b:
        if i not in c:
            c.append(i)
print(c)