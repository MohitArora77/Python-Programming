# WAP to take a class bank with minimum 3 static members and 2 objects with atleast 5 object members.
class bank:
    b_name="HDFC"
    b_addr="Noida"
    b_manager="XYZ"
    b_IFSC=9887667799878
    
# object 
emp1=bank()
emp2=bank()

# object member : obj_1
emp1.name="xyz"
emp1.phno=9876876765
emp1.addr="Sahibabad"
emp1.idno=8767
emp1.gender="M"

# object member : obj_2
emp2.name="abc"
emp2.phno=98543765465
emp2.addr="Noida"
emp2.idno=7656
emp2.gender="F"

# print
print(bank.b_name,bank.b_addr,bank.b_IFSC,bank.b_manager)
print(emp1.name,emp1.phno,emp1.addr,emp1.idno,emp1.gender)
print(emp2.name,emp2.phno,emp2.addr,emp2.idno,emp2.gender)
emp1.name="stv"
emp1.idno=7654
print(emp1.name,emp1.phno,emp1.addr,emp1.idno,emp1.gender)