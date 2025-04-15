# WAP to take a class Hospital with minimum 3 static members and 2 objects with atleast 5 object members.
class hospital:
    h_name="Fortis"
    h_addr="Haryana"
    h_employees=9600
    
xyz=hospital()
abc=hospital()

xyz.name="xyz"
xyz.phno=9878767656
xyz.idno=8767
xyz.wardno=78
xyz.addr="Delhi"

abc.name="abc"
abc.phno=9876545656
abc.idno=6754
abc.wardno=67
abc.addr="Lucknow"

print(xyz.name,xyz.phno,xyz.idno,xyz.wardno,xyz.addr)
print(abc.name,abc.phno,abc.idno,abc.wardno,abc.addr)