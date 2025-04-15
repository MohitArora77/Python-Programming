#  Inheritance
#  Heirarchichal Inheritance : Single parent class -> multiple child class

class Parent:
    a=20
class C1(Parent):
    pass
class C2(Parent):
    y=200
class C3(Parent):
    pass
class C4(Parent):
    pass

print(C1.a)
print(C2.a,C2.y)
print(C3.a)
print(C4.a)