class hospital: # class name
    hname="Max"
    hloc="Indrapuram" #class members
    hcont=9678947534
    hward=50

rawat=hospital() #object
amit=hospital()

rawat.name="Abhishek Rawat" #object members
rawat.loc="Delhi"
rawat.wardnum=34
rawat.admitteddate="23/2/2024"
rawat.phnum=7698758639
rawat.cond="Stable"
rawat.mail="Abrawat23@gmail.com"

amit.name="Amit"
amit.loc="Raj nagar"
amit.wardnum=37
amit.admitteddate="23/12/2024"
amit.phnum=9879864786
amit.cond="Unstable"
amit.mail="amit123@gmail.com"

print(hospital.hname,hospital.hloc,hospital.hcont,hospital.hward)
print(rawat.name,rawat.loc,rawat.wardnum,rawat.admitteddate,rawat.phnum,rawat.cond,rawat.mail)