a= int(input("Enter 1st number: "))
b= int(input("Enter 2nd number: "))
x=0
menu= """HELLO! THIS IS A SIMPLE CALCULATOR. Select function:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Remainder
6. Exponent
"""
c= int(input("Enter menu function index no.: "))
if c==1:
    x=a+b
    print("Sum: ", x)
elif c==2:
    x=a-b
    print("Difference: ", x)
elif c==3:
    x=a*b
    print("Product: ", x)
elif c==4:
    x=a/b
    print("Quotient: ", x)
elif c==5:
    x=a%b
    print("Remainder: ", x)
elif c==6:
    x=a**b
    print("Solved Exponent: ", x)
else:
    print("Error! select from 1 to 6")