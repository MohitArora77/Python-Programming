# Abstraction :
# Hiding the internal implementation by providing the functionality to the user is known as "Abstraction".
# While working with real time project or designing the software , apps the Architects will make use of "Abstraction".

# To perform Abstraction 3 things are necessary:
#  1--> Abstract Method
#  2--> Abstract Class
#  3--> Concrete Class

#  1--> Abstract Method -> It is a method which is declared but not implemented.
#  before the abstract method we use decorator "@abstractmethod" -> present in "abc" module.

# from abc import abstractmethod
# class A:
#     @abstractmethod
#     def method1():
#         pass
    
#  2--> Abstract Class Method 
# -> If a class contains atleast one abstract method. Then it will be known as abstract method.
# -> Should be the child class of "ABC" (Abstract Base Class).
# -> ABC is Present in "abc" module.
# -> Object creation is not possible in abstract class. 

# from abc import abstractmethod,ABC
# class A(ABC):
#     @abstractmethod
#     def method1():
#         pass
# ob1=A()

#  Q-> which class cannot be instantiated?
#  A-> Abstract Class

#  Concrete Class:
# -> It is a class which doesn't contain any abstract method.
# -> object creation is possible.
# -> No abstraction method is there.
# -> used for real time projects or designing the S/W,apps the Architects.

from abc import abstractmethod,ABC
class ATM(ABC):
    @abstractmethod
    def check_bal(self):
        pass
    @abstractmethod
    def deposite(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def customer_info(self):
        pass
class NewAtm(ATM): #overide
    def __init__(self,name,addr,bal):
        self.name=name
        self.addr=addr
        self.bal=bal
    def customer_info(self):
        print(f'Name: {self.name},Address:{self.addr},Balance:{self.bal}')   
    def check_bal(self):
        print(f"Your Balance is: {self.bal}")
    def deposite(self):
        bal=int(input("enter the deposite Amount:"))
        self.bal+=bal
        print(f"Deposite Amount:{bal}, Current Balance:{self.bal}")
    def withdraw(self):
        bal=int(input("enter the withdraw amount:"))
        if bal<=self.bal:
            self.bal-=bal
            print(f"Withraw Amount: {bal}, Current Amount:{self.bal}")
        else:
            print("Insufficient Balance")
            print(f"Current Balance is: {self.bal}")
            

ob1=NewAtm("Mr.x","Delhi",100000)
print(" Enter-1  To see the customer info \n Enter-2 to check your balance \n Enter-3 To Deposite \n Enter-4 To Withdraw \n Enter-5 TO Exit")
# ob1.customer_info()    
# ob1.check_bal()    
# ob1.deposite()
# ob1.withdraw()

while True:   
  choice=int(input("Enter your choice:"))
  if choice==1:
        ob1.customer_info()
        print("="*50)
  elif choice==2:
        ob1.check_bal()
        print("="*50)
  elif choice==3:
        ob1.deposite()
        print("="*50)
  elif choice==4:
        ob1.withdraw()
        print("="*50)
  elif choice==5:
      print("Thank U")      
      break
  else:
      print("Invalid Choice")