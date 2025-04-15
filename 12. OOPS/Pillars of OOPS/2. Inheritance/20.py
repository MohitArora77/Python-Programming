# WAP to create a resume using multi level inheritance

class HighSchool:
    Hname="DAV Public School"
    Hloc="Sahibabad"
    
    def __init__(self,name,phno,addr,h_per,h_rollno,h_YOP,h_name):
        self.name=name
        self.phno=phno
        self.addr=addr
        self.h_per=h_per
        self.h_rollno=h_rollno
        self.h_YOP=h_YOP
        self.h_name=h_name
    def disp_obj(self):
        print(self.name,self.phno,self.addr,self.h_per,self.h_rollno,self.h_YOP,self.h_name,end=" ")
    
class Intermediate(HighSchool):
    def __init__(self,name,phno,addr,h_per,h_YOP,h_name,h_rollno,i_per,i_rollno,i_YOP,i_name):
        super().__init__(name,phno,addr,h_per,h_YOP,h_name,h_rollno)
        self.i_per=i_per
        self.i_rollno=i_rollno
        self.i_YOP=i_YOP
        self.i_name=i_name
    def disp_obj(self):
        super().disp_obj()
        print(self.i_per,self.i_rollno,self.i_YOP,self.i_name)

class Graduation(Intermediate):
    def __init__(self,name,phno,addr,h_per,h_YOP,h_name,h_rollno,i_per,i_YOP,i_name,i_rollno,g_per,g_YOP,g_rollno,g_name):
        super().__init__(name,phno,addr,h_per,h_YOP,h_name,h_rollno,i_per,i_YOP,i_name,i_rollno)
        self.g_per=g_per
        self.g_YOP=g_YOP
        self.g_rollno=g_rollno
        self.g_name=g_name
        
    def disp_obj(self):
        super().disp_obj()
        print(self.g_per,self.g_YOP,self.g_rollno,self.g_name)
        
obj=Graduation("Mohit Arora",7827188612,"Ghaziabad",79.8,2019,"DAV",987676565,86.5,2021,"DAV",98767654,75.4,2025,2101610100135,"KEC")
obj.disp_obj()