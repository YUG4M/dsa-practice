# Variables
x = 10
y = 3

# Arithmetic Operators
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus or Remainder:", x % y)
print("Exponentiation or Power:", x ** y)
print("Floor Division:", x // y)

# Comparison Operators
print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal to:", x >= y)
print("Less than or equal to:", x <= y)

# Logical Operators
print("Logical AND >:", (x > 5) and (y < 5))
print("Logical OR <:", (x < 5) or (y < 5))
print("Logical NOT:", not (x < 5))

# Bitwise Operators
print("Bitwise AND &:", x & y)
print("Bitwise OR |:", x | y)
print("Bitwise XOR ^:", x ^ y)
print("Bitwise NOT ~:", ~x)
print("Left Shift <<:", x << y)
print("Right Shift >>:", x >> y)

# Assignment Operators
x += y
print("Addition Assignment (x += y):", x)
x -= y
print("Subtraction Assignment (x -= y):", x)
x *= y
print("Multiplication Assignment (x *= y):", x)
x /= y
print("Division Assignment (x /= y):", x)
x %= y
print("Modulus Assignment (x %= y):", x)
x **= y
print("Exponentiation Assignment (x **= y):", x)
x //= y
print("Floor Division Assignment (x //= y):", x)

# Identity Operators
print("Identity 'is':", x is y)
print("Identity 'is not':", x is not y)
