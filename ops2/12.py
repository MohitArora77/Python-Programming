# Method overiding :
# Changing the implementation of parent class method inside the child class method according to the requirement of the child class is known 
# as Method overiding.
# To perform method overiding method signature, type of method should be same or equal.
# Inheritance is required
class Parent:
    def cricket(self):
        print("My Fav Player is Yuvraj Singh")

class Child(Parent):
    def cricket(self):
        print("My Fav Player is Virat Kohli")
    # pass
        
obj1=Child()
obj1.cricket()
    