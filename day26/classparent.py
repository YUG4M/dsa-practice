class Parent():
    def __init__(self):
        self.value='inside parent'
    def show(self):
        print(self.value)
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value='inside child'
    def show(self):
        print(self.value)
obj1=Parent()
obj2=Child()
obj1.show()
obj2.show()