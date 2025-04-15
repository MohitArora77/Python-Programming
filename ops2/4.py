class School:
    # Class Properties
    s_name="DAV"
    addr="Sahibabad"
    s_principal="Mr.ABC"

std1=School()
std2=School()

#  Object Properties
std1.sname="ABC"
std1.rollno=34
std1.addr="UP"

std2.sname="XYZ"
std2.rollno=35
std2.addr="Punjab"

print(std1.sname,std1.rollno,std1.addr)
print("="*50)
print(std2.sname,std2.rollno,std2.addr)
print("="*50)
print(School.s_name)
