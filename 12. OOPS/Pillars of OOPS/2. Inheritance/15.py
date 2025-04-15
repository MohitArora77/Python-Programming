# Inheritance
# --1> Single level Inheritance

class A: 
    a=10
    b=20
    
class B(A):
    c="hello"
    a=100 
    
print(A.a,A.b)
print(B.a,B.b,B.c) # In Case of a class B will give priority to its own class members first  