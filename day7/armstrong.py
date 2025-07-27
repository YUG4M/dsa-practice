def is_armstrong(n):
    digits = str(n)
    total = sum(int(d)**len(digits) for d in digits)
    return total == n
x=int(input("Enter a number: "))
print(is_armstrong(x))