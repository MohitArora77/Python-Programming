#WAP to check if ano. is perfect no. or not
a=int(input("enter the no."))
i=1
fact=0
while i<a:
    if a%i==0:
        fact+=i
    i+=1
if fact==a:
    print("Perfect no.")
else:
    print("not aPerfect no.")
    
    