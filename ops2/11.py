#  Operator Overloading
# It is the phenomenon of making the opertor to work on the user defines class or user defined datatypes by the help of magic methods.
class Arithmetic:
    def __init__(self,a):
        self.a=a
    def __add__(self,other): # Magic Method
        return self.a+other.a 
    def __sub__(self,other):
        return self.a-other.a    
    def __mul__(self,other):
        return self.a*other.a  
    def __truediv__(self,other):
        return self.a/other.a
    def __lt__(self,other):
        return self.a<other.a
    def __eq__(self,other):
        return self.a==other.a
ob1=Arithmetic(10)
ob2=Arithmetic(20)
print(ob1+ob2)
print(ob1*ob2)
print(ob1-ob2)
print(ob1/ob2)
print(ob1<ob2)
print(ob1==ob2)
