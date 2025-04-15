# using constructor or __int__

class bank:
    b_name="ICICI"
    b_addr="Noida"
    b_IFSC=9878767656545
    
    def __init__(self,name,phno,addr,IFSC,gender):
        self.name=name
        self.phno=phno
        self.addr=addr
        self.IFSC=IFSC
        self.gender=gender
        
xyz=bank("xyz",8767656545,"Delhi",9878767656545,"M")
print(xyz.name,xyz.phno,xyz.addr,xyz.IFSC,xyz.gender)
    
