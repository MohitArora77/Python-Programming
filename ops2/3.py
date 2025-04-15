#  To modify class and object 
class School:
    s_name="DAV"
    addr="Sahibabad"
    s_principal="Mr.ABC"

obj1=School()
obj2=School()

# Modify using the class
School.addr="Ghaziabad" 
print(School.addr,obj1.addr,obj2.addr)
print("="*50)

# Modify using the object
obj1.s_name="DPS"
print(obj1.s_name,obj2.s_name,School.s_name)
print("="*50)
obj2.s_principal="MR.XYZ"
print(obj2.s_principal,obj1.s_principal,School.s_principal)