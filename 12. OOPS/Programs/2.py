# WAP to take a class bank with minimum 3 static members and 2 objects with atleast 5 object members.

class bank:
    bname="SBI"
    bloc="sec-15" #static member 
    BIFSC="SBIN000006547" 
    
rhythm=bank()
mohit=bank()

rhythm.name="rythm" #object member
rhythm.accno=345678765432
rhythm.phno=7879748808
rhythm.addr="Ashok Nagar"
rhythm.pan="DGWED565D78"


mohit.name="Mohit"
mohit.accno=456732454321
mohit.phno=7827188612
mohit.addr="Vijay Nagar"
mohit.pan="QRDDF453ERW"

print(bank.bname,bank.bloc,bank.BIFSC)
print(rhythm.name,rhythm.accno,rhythm.addr,rhythm.pan)
print(mohit.name,mohit.accno,mohit.addr,mohit.pan)