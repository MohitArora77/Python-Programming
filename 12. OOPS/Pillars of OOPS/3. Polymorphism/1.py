#method overloading

class Overload:
    @staticmethod 
    def add(a,b):
        return a+b
    prev=add # Monkey Patching -> we are storing the address of previous method in new variable. 
             # For that method to work and that;s called "Monkey Patching"
    @staticmethod
    def add(a,b):
        return a-b
    prev1=add #Monkey Patching
    @staticmethod
    def add(a,b):
        return a*b
obj1=Overload()
print(obj1.add(2,3))
print(obj1.add(56,34))
print(obj1.prev(4,6))
print(obj1.prev1(7,6))
# Here the latest method is executed , previous method are getting overwrite by latest method.
# Previous method become a waste method.
# To restore the previous method we have a concept called "Monkey Patching".
# Monkey Patching --->we are storing the address of previous method in new variable. For that method to work we need concept called "Monkey Patching"
