# OOPS: 
> Object Oreinted Programming -->

# Advantages:
> Modularity
> Code reusability
> Flexibility
> Maintainability
> Collaboration

# Class : 
> Class is the blueprint which contains properties and functionalities of an object.
< -or- >
> It is a medium where data can be stored and can be accessed.

# Object : 
> Object is the instance(object) of class.
> It is the real time entity having some attribute.
> Object belongs to class.
> A class can contains 'n' no. of object.

# How to create a class and object :
class Class_name:
      
      Properties/statements and functionalities/Behaviour

Obj(object refrence)=Class_name(args)  # args are optional
> Class name should be in upper case.

# There are 2 types of Classes:
> In-build class -> All the datatypes are in-build class
> User Defined Class 

# How to access the data:
> class_name.property -> class name -> class Properties
> obj_name.property -> object name -> objecy properties

# How to Modify the properties:
> 1) By using class
 Syntax-> Class_name.property=property
--> If we are using the class to  modify it will affects or modifies the properties for all the objects.

> 2) By using Object
 Syntax-> Object_name.property=property
--> If we are using the object it will modify the property of specified object.

# Types of properties/states/members
> There are 2 types of Properties
 1) Class/generic/static properties ->
 > Class properties/Class members-> These are the members of the class which are same or equal for all the objects.
 >> Example: If we consider this bank as the class , the object are customer , and class properties-> bank_name,addr,bank_manager,IFSC code.
 
 2) Object/specific/dynamic properties ->
 > Object Properties/Object members-> These are the members of the class  which are different for all the object.
 >> Example: customer_name,custonmer_addr,phno,bank_balance,account no,aadhar card no.


# Methods/Fucntion in OOPS 
> Function inside a class is known as method.
> a(object for str class)= 'hii'(str class)

# Method-> Constructor/init method/ initialization  
> It is an in-built method which is used to initialize the members of the object. (To create object properties.,  to create instance's (object) attributes(properties)).
> We don't need to call this method outside of the class , at the time object creation it get invoked(called) automatically.
> It is mendatory to pass 'self' as the 1st argument. (self carries the address of the object).
> We can use other variable instead of 'self' , but for industrial standard we have to use 'self'.
> Syntax to create the constructor: 
    > def __init__(self,arg1,arg2,...argn):
    >       self.prop1=prop1
    >       self.prop2=prop2
    >       self.prop3=prop3
    >       self.prop4=prop4 ...
    >    ...self.propn=propn
> 'self' stores object address that's why its not showing self in error.

# Format String / F-string ->
> It is used to multiple variable substitution.
> print(f'str{var1}str{var2}str......{varn}')

# Types of Methods:
> Methods are used to provide functionalities to the object.
> There are 3 types of methods:
1) Object Method
2) Class Method
3) static Method

# 1) Object Method :
> Object Methods are used to Access and modify the object properties.
> IT takes mendatory argument -> 'self'
> TO call the object method -> 

  obj1.method_name(args)

> Syntax to create object method:
  class class_name:
      def method_name(self):
          Statement Body 

# 2) Class Method :
> It is used to Access and Modify the class Properties.
> @classmethod