a=[1,2,3,4,5,6,7,8,9,10,7,8,9,10]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)