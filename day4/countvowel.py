a= "Hello World"
b=['a', 'e', 'i', 'o', 'u']
c=[]
for i in a.lower():
    if i in b:
        c.append(i)
print(len(c))