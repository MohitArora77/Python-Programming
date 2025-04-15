# add 2 numbers using classmethod , static method ,object method .

class num:
    def addition(self,a,b): # object method
        print(a+b)
    

    @classmethod
    def disp_sum(cls,a,b): # class method
        print(a+b)

    @staticmethod 
    def add(a,b): # static method
        print(a+b)
    
obj=num()
obj.addition(3,4)
obj.disp_sum(7,9)
obj.add(6,7)
