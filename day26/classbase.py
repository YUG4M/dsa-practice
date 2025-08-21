class Base:
    def __init__(self):
        self._a=2
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("calling protected asset s")
        self._a=3
        print("calling modified asset, derived ", self._a)

obj= Derived()
obj2= Base()
print("Assessing Protected member of obj ", obj._a)
print("Assessing Protected member of obj2 ", obj2._a)