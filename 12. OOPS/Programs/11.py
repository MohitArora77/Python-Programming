# Static Method:
# WAP create a bank with minimum 3 class members , 2 objects , 5 object members and with 2 object method withdraw and deposite.
class bank:
    bname="ICICI"
    baddr="Indrapuram"
    bIFSC=876765654467
    
    def __init__(self,name,addr,phno,gender,accno,balance):
        self.name=name 
        self.addr=addr 
        self.phno=phno
        self.gender=gender 
        self.accno=accno
        self.balance=balance
    
    @classmethod
    def disp_cls(cls):
        print(cls.bname,cls.baddr,cls.bIFSC)
        
    def new_cls(cls,new):
        cls.bname=new
        
    def disp_obj(self):
        print(self.name,self.addr,self.phno,self.gender,self.accno,self.balance)
        
    def deposite(self,amt):
        self.balance=self.add(self.balance,amt)
        
    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient Balance")
        else:
            self.balance=self.sub(self.balance,amt)
    
    @staticmethod
    def add(a,b):
        return a+b
        
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def msg1():
        print("Deposite")
        
    @staticmethod
    def msg2():
        print("Withdrawal")
        
        
xyz=bank("xyz","Delhi",9786576465,"M",986758674784,10000000000)
abc=bank("abc","Delhi",9675846574,"F",859768467894,100000000000)

# bank details
bank.disp_cls()
# object details
xyz.disp_obj()
abc.disp_obj()
# Withdraw display
xyz.withdraw(10000000)
xyz.disp_obj()
xyz.msg2()
abc.withdraw(128738912)
abc.disp_obj()
abc.msg2()
# Deposite display
xyz.deposite(10000000)
xyz.disp_obj()
xyz.msg1()
abc.deposite(1000000000)
abc.disp_obj()
abc.msg1()