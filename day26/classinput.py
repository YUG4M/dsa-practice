class A:
    def __init__(self):
        self.n1 = int(input("Enter first number: "))
        self.n2 = int(input("Enter second number: "))

class B(A):
    def add(self):
        return self.n1 + self.n2

class C(B):
    def display(self):
        res = self.add()
        print(f"Result: {res}")

obj = C()
obj.display()
