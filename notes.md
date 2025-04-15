# For loops:-  Same set of instruction again and again unless the condition become false but for loop totally depends on the collection.
-> Fixed collection
-> Faster than while loop
-> sytax:-
for i in collection:-
collection-> 
i)  Range
ii) String
iii)List
iv) Tuple
v)  Set
vi) Dictionary
> In for loop we don't have to initialize, update the collection it automatically get updated.

# range function:-
> range is the in-built function which is use to set the flow of collection by lower,upper limit.

syntax:-
range(Starting point,Ending point,steps)
-> Whenever we deals with no. we use range function.

# while solving for loop if we are dealing with index type questions u will use range functions.

# Continue:-
> Continue is a keyword which is used to skip the iteration without breaking the loop.
> In this process we don't put any condition on continue.
> It will work for -> For loop, While loop

#set dictionary not in while loop

# Pass:-
> Pass is a keyword which make a empty block as a valid block.

Program--> Function--> module--> Packages--> library
# Function(method) :-
> A Function is a block of code to perform a specific task or user required task.
> In the block of code we write set of instruction which is callable when calling the function. 
> We use functions to reduce the code size and increse the efficiency of the operation.
> We have 2 types of functions:-
i)  In-build Function
ii) User defined function 

# In-build Function:-
> These are the Predefined functions which are having some specific task to do which are assign by the developer.

# 6 types:-

i) String-> upper(),lower(),ord(),spilt(),reverse(),chr() 
ii) List-> append(),pop(),int(),sort()
iii) Tuple->Index(),count()
iv) Set ->add(),remove()
v) Dict-> var.keys,var.values,var.item
vi) Unitary-> input(),len(),id(),type(),print(),eval()

 * Unitary-> Unitary in-build functions are the functions which are common for every datatype.
ex:- Input(),len(),id(),type(),print(),eval()

# User-defined fucntions:-
> These are the functions which are made as per user requirement.
> To create user defined function we have to use a keyword " def ".

> We have 4 types of user-defined functions:-
i)  without variable without return
ii) with variable without return
iii) without variable with return
iv) with variable with return

# Syntax:-
def f_name(variable/arguments):

True Body Statement
return value

f_name( ) or print(f_name()) }-> calling function

def-> def is a keyword which is used to create a function.
function_name-> These are the name given to ablock of code.
arguments-> These are parameters passed with the function name.
return-> return is a keyword which control the operation by providing the values.
calling Fucntion-> It is the function name which is already created using def.
2 ways:
i) f_name( )
ii)print(f_name( ))

# Without Argument/variable without return
def f_name():
True body statement
f_name()
____________________________________________________________
|main()          | method()                                  |
|_______________ |___________________________________________|
upper_case()    | Block of code stored on that particular id.
(have some id)  | a="python"
                | out=" " 
                 for i in a:
                    if 'A'<=i<='Z':
                       out+=i
                    print(out)


>  Capitalize : It is an in-build fucntion which is used to covert the first alphabet of a string to uppercase.



# Join function -> Which is use to connect to data.
> join is a in-build function which is used to connect /merge data.
> syntax->
 gluestr.join(var)

eg-> 

# title function -> 
> title is a in-build function which is used to make the first letter upppercase in the string where you have space .
syntax is -> var.title(variable name)

eg->
title()
-> how are you all
-> How Are You All
 > return-> it is a keyword which control the operation 

# 3.  without variable with return
> syntax:-
def f_name():
   TBS 
   return value
print(f_name) # it is mandatory

> In return type of function it is mandatory to call print while calling the function .

# Anagam:- 
 > Letter's length and the characters are all same
 > ex:- listen - silent

# Sorted:- These are the no. whose sum of individual cube is equal to the no.
# armstrong no. : these are the no. which are sum by the no. of digit, pair no. of digit's power where individual values will be sum which is equal to the same no. 


# OOPS:-

# Memebrs of class and object :
> Members are nothing but the properties of class and objects 
> we have 2 types of members:
 1-> Static member/ class member (fixed for everyone)
 2-> Object member (independent)

# Methods in OOPS:
1) Object Method
 syntax:
 class c_name:
 {
   properties/class
 }
 def __int__(self,arguments)


 def m_name(self,argument(new)):
       print()

  object.c_name()

  Access :- obj.m_name()
  Modify :- obj.m_name( values)

2) class method: 
> Class Member-> Modification and access we use class method
> to deal with class members we use -. cls in the presence of -> @classmethod

Access:- obj=c_name()

# Decorators: It should increase the efficiency of the function without changing its original functionality
1) In-build
2) 

3) Static Method: 
@staticmethod 
def msg():
 print("hello")
 
company.msg() # class
abc.msg() # Object

# Inheritance:

> Deriving the properties from one class to another class

class -> Parent class/Super class/Base class
 |
 | Derived Properties
 |
class -> Child class/Sub class/Derived class

syntax:
class PC:
   SB
class CC:
   SB

# 5 types of inheritance:
1) Single level inheritance
2) Multi level inheritance
3) Multiple inheritance
4) Heirarichal inheritance
5) Hybrid inheritance

# method resolution order(MRO) -> class C(A,B):

> @staticmethod:
class Add:
   @staticmethod
   def add(a,b):
     return a+b
class Mul:
   @staticmethod
   def mul(a,b):
      return a*b
class Sub:

# Heirarchical Inheritance
> one parent class -> multiple child class

             Parent
      _________|__________
     |         |          |
   Child1    Child2.......Childn

# Hybrid Inheritance:
> combination of 2 or more than 2  different types of inheritance.


             Parent ( Heirarchical)
       _________|__________
      |         |          |
   Child1    Child2.......Childn
     |__________|__________|
                |
               ParentC2 (Multiple)

ASCII->

A-Z-> 65-90
a-z-> 97-122

ord("char")
chr(ascii value)

# isalnum()-> number,alphabet

# Polymorphism:
 > It is a phenomenon of performing 2 or more than 2 opertaion by the method or the operators
 > Some method or operators----> two or more than 2 different operations

# we can explain polymorphism in 3 ways:
 > 1. method overloading
 > 2. operator overloading
 > 3. method overiding

# 1. method Overloading:
 > It is the process of using same methods in 2 or more than 2 diff types of operations.
 > Python does not support method overloading

