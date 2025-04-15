# Class Method:
class company:
    cname="Google"
    cloc="Uganda"
    cceo="XYZ"
    
    def __init__(self,name,age,phno,email,gender,salary,desg):
        self.name=name
        self.age=age
        self.phno=phno
        self.email=email
        self.gender=gender
        self.salary=salary
        self.desg=desg
        
    def disp_obj(self): # use to display the object members
        print(self.name,self.age,self.phno,self.email,self.gender,self.salary,self.desg)
        
    def new_salary(self,new): # Use to make changes in details of object members       
        self.salary=new 
    
    @classmethod #Decorators(must use): the function which increase the function efficiency without changing the orginal functions.
    def disp_cls(cls): # Use to access the detils in the class members/
        print(cls.cname,cls.cloc,cls.cceo)
    @classmethod # Decorators (must use)
    def new_cceo(cls,new): # Use to change, modify the details in class members
        cls.cceo=new
        
    @staticmethod
    def msg():
        print("Good Morning")
        

xyz=company("xyz",22,7685763466,"xyz234@gmail.com","M",50000,"Project Manager")
abc=company("abc",25,8675857587,"abc123@gmail.com","F",100000,"HR")

company.disp_cls() #Class Details
xyz.disp_obj() #Object Members Details
abc.disp_obj() #Object Members Details
abc.new_salary(60000) # To change object member details 
abc.disp_obj() # object member detail change
company.new_cceo("abc") # To change the details of the class members
company.disp_cls() # Changed deatils of class members will be displayed. 
company.msg()
abc.msg()