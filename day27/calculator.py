def getData():
    a=int(input("Enter value 1: "))
    b=int(input("Enter value 2: "))
    print('''Choices: 
                1.Add
                2.Sub
                3.Product
                4.Quotient''')
    c=int(input("Select a Choice: "))
    return a, b, c

def addition(a, b):
    add= a+b
    return add

def subtraction(a, b):
    sub= a-b
    return sub

def product(a, b):
    prod= a*b
    return prod

def Quotient(a, b):
    quot= a/b
    return quot

a, b, c = getData()

if c==1:
    print(addition(a,b))
elif c==2:
    print(subtraction(a, b))
elif c==3:
    print(product(a, b))
elif c==4:
    print(Quotient(a, b))
else:
    print("Please choose one of the choices")
    getData()