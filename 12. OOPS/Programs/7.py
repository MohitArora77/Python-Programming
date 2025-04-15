# Method -> object method
class TY:
    cname="PySpiders"
    cloc="Sec-3"
    addr="B-4,near metro-16"
    
    def __init__(self,name,phno,addr,email,YOP,stream,MOCK):
        self.name=name
        self.phno=phno
        self.addr=addr
        self.email=email
        self.YOP=YOP
        self.stream=stream
        self.MOCK=MOCK
    # fucntion for Object Method   
    def disp_obj(self):
        print(self.name,self.phno,self.addr,self.email,self.YOP,self.stream,self.MOCK)
        
    # to add something New 
    def new_phno(self,new):
        self.phno=new
    def new_stream(self,new):
        self.stream=new

XYZ=TY("XYZ",9887876678,"Delhi","XYZ321@gmail.com",2025,"CSE",1)
ABC=TY("ABC",8796586876,"Noida","ABC123@gmail.com",2025,"IT",1)

#Object Method
XYZ.disp_obj()
ABC.disp_obj()
XYZ.new_phno(5977583947)
XYZ.disp_obj()
ABC.new_stream("CSE")
ABC.disp_obj()