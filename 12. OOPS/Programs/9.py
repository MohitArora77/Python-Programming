# class employee 
class emp:
    cname="XYZ"
    caddr="Delhi"
    cnum=7869567488
    
    def __init__(self,name,phno,addr,salary,adharno):
        self.name=name
        self.phno=phno
        self.addr=addr
        self.salary=salary
        self.adharno=adharno
    
    def disp_obj(self):
        print(self.name,self.phno,self.addr,self.salary,self.adharno)
    
    def new_salary(self,new):
        self.salary=new
    @classmethod 
    def disp_cls(cls):
        print(cls.cname,cls.caddr,cls.cnum)
    @classmethod
    def new_cnum(cls,new):
        cls.cnum=new
        
        
abc=emp("abc",8679576898,"Delhi",50000,876565435432)
xyz=emp("xyz",8675867554,"Indrapuram",40000,765465345463) 

# abc.disp_obj()
# xyz.disp_obj()
# abc.new_salary(70000)
# abc.disp_obj()
# xyz.new_salary(80000)
# xyz.disp_obj()
# print(emp.cname,emp.caddr,emp.cnum)

emp.disp_cls()
