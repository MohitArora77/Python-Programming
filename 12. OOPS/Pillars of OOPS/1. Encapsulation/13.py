class clg:
    cname="KEC"
    caddr="Sahibabad"
    __cboard="state" #private
    
    def __init__(self,name,rollno,branch,YOP):
        self.name=name
        self.rollno=rollno
        self.branch=branch
        self.__YOP=YOP # Private
        
    def disp_obj(self):
        print('name',self.name)
        print('rollno',self.rollno)
        print('branch',self.branch)
        print('YOP',self.__YOP) #Private
    
    @classmethod
    def disp_cls(cls):
        print('cname',cls.cname)
        print('caddr',cls.caddr)
        print('cboard',cls.__cboard) #private
        
    def __disp_name_rollno(self):
        print('name',self.name)
        print('rollno',self.rollno)
    
obj=clg("abc",132,'CS',2025)

obj.disp_obj()
clg.disp_cls()
print(clg._clg__cboard) # able to access the private class member 
print(obj._clg__YOP) # able to access the private object member
obj._clg__disp_name_rollno()
clg._clg__cboard="private"
print(clg._clg__cboard)