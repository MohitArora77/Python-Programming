class company:
    cname="TCS"
    cloc="Noida"
    __csec="IT Sector"
    
    def __init__(self,name,addr,phno,id,income):
        self.name=name
        self.addr=addr
        self.phno=phno
        self.__id=id
        self.income=income
        
    def disp_obj(self):
        print('name',self.name)
        print('addr',self.addr)
        print('phno',self.phno)
        print('id',self.__id)
        print('income',self.income)
        
    @classmethod
    def disp_cls(cls):
        print('cname',cls.cname)
        print('cloc',cls.cloc)
        print('csec',cls.__csec)
        
    def __disp_name_id(self):
        print('name',self.name)
        print('id',self.__id)
        
obj=company("abc","Noida",8675967586,1987,10000000)

obj.disp_obj() #object member
company.disp_cls() #class member
print(company._company__csec) # IT sector
print(obj._company__id) #1987

obj._company__disp_name_id() #both name and id
company._company__csec="Private"
print(company._company__csec) # able to change value of the that class member

        