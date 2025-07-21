a=[1,2,3,4,5,6,7,8,9,10,7,8,9,10]
b=[]
for i in range(1, len(a)):
    if a.count(i) > 1 and i not in b:
        b.append(i)
print("Duplicates: ", b)