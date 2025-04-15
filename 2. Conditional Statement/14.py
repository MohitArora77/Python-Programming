#WAP to create a railway system
age=int(input("enter the age:"))
fair=int(input("enter the fair:"))
if age>=60:
    print("Senior Citizen:",fair*0.5)
elif age<=60 and age>=18:
    print("Adult:",fair)
elif age<5:
    print("Child:",fair*0)
