class Passenger:
    def __init__(self,name,age,gender,phno):
        self.name=name
        self.age=age
        self.gender=gender
        self.phno=phno
        
    def disp_obj(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("phno:",self.phno)
        
class Boarding(Passenger):
    def __init__(self,name,age,gender,phno,platform_no,boarding_time,date):
        super().__init__(name,age,gender,phno) # object  chaining
        self.platform_no=platform_no
        self.boarding_time=boarding_time
        self.date=date
        
    def disp_obj(self): #method chaining
        super().disp_obj()
        print("Platform no:",self.platform_no)
        print("Boarding_Time:",self.boarding_time)
        print("Date:",self.date)
        
class Conformation(Boarding):
    def __init__(self,name,age,gender,phno,platform_no,boarding_time,date,confirmed_seat,seatno):
        super().__init__(name,age,gender,phno,platform_no,boarding_time,date)
        self.confirmed_seat=confirmed_seat
        self.seatno=seatno
        
    def disp_obj(self):
        super().disp_obj()
        print("Conformed:",self.confirmed_seat)
        print("Seatno:",self.seatno)
        
x=Conformation("Shivam",21,"Male",9876756475,5,"10:00AM","26th/Feb2/025","YES","B32")
x.disp_obj()
        
    
        