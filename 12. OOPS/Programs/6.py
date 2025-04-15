#WAP to create a class mall with min 3 class memebers with 2 object with min 5 object members
class mall:
    mname="Mahagun"
    mloc="Indrapuram"
    msize="10acres"
    
    def __init__(self,shopname,phno,email,accno,addr):
        self.name=shopname
        self.phno=phno
        self.email=email
        self.accno=accno
        self.addr=addr
        
xyz=mall()
abc=mall("xyz",34567867)