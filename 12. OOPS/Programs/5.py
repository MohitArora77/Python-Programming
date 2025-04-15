#using constructor
class bank:
    bname="HDFC"
    bloc="Indrapuram"
    bIFSC="HDFC3000426YR"
    
    def __init__(selfi,name,phno,email,accno):
        selfi.name=name
        selfi.phno=phno
        selfi.email=email
        selfi.accno=accno
xyz=bank('xyz',8768765456,'xyz32@gmail.com',34812234411)
print(bank.bname)
print(xyz.name)