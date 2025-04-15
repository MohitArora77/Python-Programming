# mall using 
class mall:
    mname="Mahagun"
    mloc="Indrapuram"
    msize="10acres"
    
    def __init__(self,s_name,s_no,s_phno,s_floor):
        self.s_name=s_name
        self.s_no=s_no
        self.s_phno=s_phno
        self.s_floor=s_floor
        
xyz=mall("xyz",56,8976765654,"2nd Floor")
abc=mall("abc",36,8345765654,"1st Floor")

print(xyz.s_name,xyz.s_no,xyz.s_phno,xyz.s_floor)
print(abc.s_name,abc.s_no,abc.s_phno,abc.s_floor)
print(mall.mname)