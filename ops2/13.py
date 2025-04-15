# Encapsulation :
# Wrapping the data and functionality into a single unit is known as encapsulation.
#  <--OR-->
# It is the process of providing the security to the members of the class by using Access Specifier.

# Access Specifier : it specifies whether the user can access the data outside of the class or not.
#  There are 3 types of access specifier.
#  1) Public 2) Protected 3) Private

# 1) Public Access Specifier : 
# --> These are the members of the class which can be accessable outside of the class.
# --> Generally what we declare inside the class by default they are known as Public Access Specifier.

# SYNTAX :
# class parent:
#     # class properties/class members
#     var1="val1"
#     var2="val2"
#     var3="val3"
    
#     @classmethod
#     def m_name(cls):
#         # statement Body
#     def m_name(self):
#         # statement Body
    
#     @staticmethod
#     def m_name():
#         # statement body


# 2) Protected Access Specifier:  
# --> These are the members of the class which should be protected by protected access specified.
# --> For which they won't be able to access outside of the class.
# --> To create Protected Access Specifier we have to use single '_' before the members of the class.

# Note -> #  In Python Protected Access Specifier doesn't provide any security to the members of the class.

# SYNTAX :
# class parent:
#     # class properties/class members
#     _var1="val1"
#     _var2="val2"
#     _var3="val3"
    
#     @classmethod
#     def _m_name(cls):
#         # statement Body
#     def _m_name(self):
#         # statement Body
    
#     @staticmethod
#     def _m_name():
#         # statement body

# Example
# class Parent:
#     _a=10
#     _b=20
#     def _cricket(self):
#         print("Fav Player is Kapil Dev")
        
# ob1=Parent()
# print(ob1._a)
# print(ob1._b)
# print(ob1._cricket())

# 3) Private Access Specifier :
# --> These are the member of the class which cannot be access outside of the class.
# --> To Make the class members as the private access specifier we have to use '__' before the property name/method name.
# --> In some situation if the user access the class member and the method outside of the class then we have the following steps can be followed:

# i) obj/class._classname__property/method

# We can use 2 method: 1) get method and 2) set method to access and modify the Private Access Specifier.


# SYNTAX :
# class parent:
#     # class properties/class members
#     _var1="val1"
#     _var2="val2"
#     __var3="val3"
    
#     @classmethod
#     def __m_name(cls):
#         # statement Body
#     def __m_name(self):
#         # statement Body
    
#     @staticmethod
#     def __m_name():
#         # statement body

# Example
class Parent:
    __a=10
    __b=20
    def __cricket(self):
        print("Fav Player is Kapil Dev")
        
    def get(self): #Access
        return self.__a
    def set(self): #Modify
         self.__a=int(input("Enter the Number:"))
        
ob1=Parent()
print(ob1._Parent__a)
ob1._Parent__a=40
print(ob1._Parent__a)
print(ob1.set())
print(ob1.get())



print(ob1._Parent__b)
print(ob1._Parent__cricket())