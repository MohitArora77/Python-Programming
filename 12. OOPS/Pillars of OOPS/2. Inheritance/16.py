class Online_bank:
    name="Kotak"
    helplineno=9876857767
    IFSC="KOTAK8738957489"  
    def __init__(self,name,phno,add,PAN,email):
        self.name=name
        self.phno=phno
        self.add=add
        self.PAN=PAN
        self.email=email
        
    def disp_obj(self):
        print('Name',self.name)
        print('Phno',self.phno)
        print('Address',self.add)
        print('PAN',self.PAN)
        print('email',self.email)
    
class Offline_bank(Online_bank):
    def __init__(self,name,accno,phno,PAN,aadhar,email,add):
        super().__init__(name,phno,PAN,email,add) #consctructor chaining
        self.accno=accno
        self.aadhar=aadhar
    def disp_obj(self):
        super().disp_obj()
        print(self.aadhar,self.accno)
    
abc=Offline_bank("abc",987876765654,9878767656,98787676565454,987876765654987,"abc@gmail.com","Delhi")
abc.disp_obj()