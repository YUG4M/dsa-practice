x=[2,5,23,65,1,43,87,12,24]
y=[1,2,3,4,5]
a= input("Choose array x or y: ")
if a == 'x':
    a=x
elif a == 'y':
    a=y
else:
    print("Error")
isTrue= True
for i in range(1,len(a)):
    if a[i] < a[i-1]:
        isTrue= False
        break
if isTrue:
    print("SORTED")
else:
    print("NOT SORTED")