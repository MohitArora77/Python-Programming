#  Method -> using constructor/__init__/intitialize

# class Sam:
#     def __init__(Self):
#         print("Hello")
        
# obj1=Sam()

class School:
# Class Properties / Class members
    s_name="DAV"
    addr="Sahibabad"
    s_principal="Mr.ABC"

# Object Properties/ Object members
    def __init__(self,sname,rollno,phno,addr):
        self.sname=sname  # LHS-> Address and RHS-> Variable name where address will be stored
        self.rollno=rollno
        self.phno=phno
        self.addr=addr
    
    # def __init__(self):
    #     self.sname=eval(input("Enter the Data:"))
    #     self.rollno=eval(input("Enter the Data:"))
    #     self.phno=eval(input("Enter the Data:"))
    #     self.addr=eval(input("Enter the Data:"))

# Object method to access and modify object properties
    def std_info(self):
        print(f'Student name {self.s_name},student rollno {self.rollno}') 

#  to access the object method:

obj1=School("ABC",45,8767656545,"Delhi")
obj2=School("XYZ",67,7899678856,"Indrapuram")
obj1.std_info()

print("Student1 Details:")
print(obj1.s_name,obj1.rollno,obj1.phno,obj1.addr)
print("Student2 Details:")
print(obj2.s_name,obj2.rollno,obj2.phno,obj2.addr)

print(School.s_name,School.addr,School.s_principal)

# std1=School()
# print(std1.s_name,std1.phno,std1.rollno,std1.addr)

