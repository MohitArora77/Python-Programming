# Method Overiding:
# Changing the implementation of parent class method inside the child class method 
# according to the requirement of child class known as method overiding.

# To perform the method overiding 3 things are necessary:
#  1--> Inheritance should be done.
#  2--> Types of method should be same.
#  3--> Method Signature should be same.
 
#  Method Signature --> Method Name + Arguments

class Parent:
    @staticmethod 
    def marriage():
        print("YOUR ARE GOING TO MARRY WITH XYZ")
class Child(Parent):
    @staticmethod
    def marriage():
        print("YOU ARE GOING TO MARRY WITH ABC")

ob1=Child()
ob1.marriage() # Method Overide

class Teacher:
    @staticmethod # Same type of Method
    def HomeWork(): # Same Method Signature.
        print("You need to complete the Homework")
class Student(Teacher): # Inheritance should be done.
    @staticmethod
    def HomeWork():
        print("You don't need to complete the Homework")

ob1=Student()
ob1.HomeWork() # Method Overide