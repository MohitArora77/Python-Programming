# Initialising property using functions
# without using __init__

class bank:
    b_name="ICICI"
    b_addr="Noida"
    b_IFSC=9878767656545
    
    def func(obj,name,phno,addr,IFSC,gender):
        obj.name=name
        obj.phno=phno
        obj.addr=addr
        obj.IFSC=IFSC
        obj.gender=gender
    
xyz=bank()
abc=bank()

xyz.func("xyz",8767656545,"Delhi",987876765654,"M")
abc.func("abc",9878767655,"Indrapuram",98878787867,"F")

print(xyz.name,xyz.phno,xyz.addr,xyz.IFSC,xyz.gender)
print(abc.name,abc.phno,abc.addr,abc.IFSC,abc.gender)