class Online_reg:
       hname="Max"
       hloc="Delhi"
       
       def __init__(self,name,phno,age,addr,diagnosed):
           self.name=name
           self.phno=phno
           self.age=age
           self.addr=addr
           self.diagnosed=diagnosed
           
       def disp_obj(self):
           print(self.name,self.phno,self.age,self.addr,self.diagnosed,end=" ")
           
class Offline_reg(Online_reg):
    def __init__(self,name,phno,age,addr,diagnosed,aadhar,payment):
        super().__init__(name,phno,age,addr,diagnosed)
        self.aadhar=aadhar
        self.payment=payment
        
    def  disp_obj(self):
        super().disp_obj()
        print(self.aadhar,self.payment)
        
abc=Offline_reg("ABC",9878767656,55,"Delhi","Cancer",9878767654654,1000000)
abc.disp_obj()
        
        
               
       
       
       