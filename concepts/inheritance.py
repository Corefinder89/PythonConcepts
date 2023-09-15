# Inheritance
class A:
    def sum(self,a,b):
        print(a + b)

class B:
    def sum(self,a,b):
        print(a - b)

class C(B,A):
    # def child_method(self):
    #     super().sum(4,5)
    #     super().difference(5,4)
    def child_method(self):
        super().sum(3,4)

class D(A,B):
    def child_method(self):
        super().sum(3,4)
        super().difference(4,3)

class E:
    def __init__(self, emp_id, emp_name):
        self.emp_id=emp_id
        print(self.emp_id)
        self.emp_name=emp_name
        print(self.emp_name)

class F(E):
    def __init__(self, emp_id, emp_name):
        super().__init__(emp_id, emp_name)

f = F(12, "chaitanya")
f = F()
f.some_method()

class A -> some_method1()
class B -> some_method2()
class C -> some_method3()

class Selenium(A,B,C):
    def some_method(self):
        super().some_method1()
        super().some_method2()
        super().some_method3()
