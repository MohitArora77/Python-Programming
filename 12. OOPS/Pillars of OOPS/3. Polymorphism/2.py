# Operator Overloading :
# It is the phenomenon of using the operator to work on the user defined class or 
# user defined datatypes by invoking the magic methods.

class Arithmetic:
    def __init__(self,a):
        self.a=a
    def __add__(self,other): # Magic Method
        return self.a+other.a
    def __sub__(self,other): # Magic Method
        return self.a-other.a
ob1=Arithmetic(10)
ob2=Arithmetic(20)
print(ob1.a+ob2.a) # 30
print(type(ob1.a),type(ob2.a)) # <class 'int'>
print("ADDITION IS:",ob1+ob2) # No more because of  Type Error
print("SUBSTRACTION IS:",ob1-ob2) # Type Error
print(type(ob1)) # <class '__main__.Arthmetic'>
# we cannot perform operation on user defined class and user defined datatype.
# can be solved using magic method -> concept called Operator Overloading
# we can perform operation on  in-build defined class and in-build defined datatype.