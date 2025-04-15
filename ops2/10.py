# Polymorphism : It is the process of making the same method or operator to work on 2 operation or more than 2 different type of operations.\

# We can extract this by using 3 methods:
# 1) Method Overloading 2) Operator overloading and 3) method overiding  

# 1) Method Overloading :
# > This process of using the same method in 2 or more tham 2 different types of operations.

class Overloading:
    @staticmethod
    def add(a,b):
        return a+b
    prev=add
    @staticmethod
    def add(a,b):
        return a*b
    prev1=add
    @staticmethod
    def add(a,b):
        return a/b
obj1=Overloading()
print(obj1.add(5,20))
print(obj1.prev(5,20))
print(obj1.prev1(5,20))
# In Python the latest method will overides the previous method and it is not possible to perform method overloading in python  
# Method to fix overiding we use monkey patching by adding some varibale in each methods.
# However if we want to use the previous method or waste methods than we have to store the address of the waste method or 
# previous method inside of the new variable.because new variable will act as method. This process known as Monkey Patching.