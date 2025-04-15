# Multiple Inheritance
class A:
    a=10
    b=20
class B:
    c="hello"
    d=30
class C:
    e="hi"
    def __init__(self,a):
        self.a=a
class D(A,B,C):
    f="apple"
print(D.a,D.b)
