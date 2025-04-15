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
      print(self.name,self.phno,self.add,self.PAN,self.email,end=" ")
      
class Offline_bank(Online_bank):
    def __init__(self,name,phno,add,PAN,email,accno,aadhar):
        super().__init__(name,phno,add,PAN,email) #consctructor chaining -> able to chain the data from one class object to another class object
        self.accno=accno
        self.aadhar=aadhar
    def disp_obj(self): # method chaining
        super().disp_obj() 
        print(self.aadhar,self.accno)
        
abc=Offline_bank("abc",9878767654,"Delhi",987876765654,"abc@gmail.com",56786754654378,987656746543)
abc.disp_obj()