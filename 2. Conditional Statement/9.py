#Elif 
#Wap to check the no. is single digit , 2 digit , 3 digit or 4 digit no.
a=int(input("enter the digit:"))
if 0<=a<=9:
    print("single digit")
elif 10<=a<=99:
    print("double digit")
elif 100<=a<=999:
    print("triple digit")
elif 1000<=a<=9999:
    print("4 digit")