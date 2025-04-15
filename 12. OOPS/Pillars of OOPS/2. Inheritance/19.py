# Mutli Level Inheritance
# Example 1:
class A:
    a=10
    b=20
class B(A):
    c=30
    d="hello"
class C(B):
    pass

print(A.a,A.b)
print(B.a,B.b,B.c,B.d)
print(C.a,C.b,C.c,C.d)