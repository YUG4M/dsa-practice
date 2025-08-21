class A:
    def Fun1(self):
        print("Fun1")
class B(A):
    def Fun2(self):
        print("Fun2")
class C(B):
    def Fun3(self):
        print("Fun3")
obj = C()
obj.Fun1()
obj.Fun2()
obj.Fun3()
