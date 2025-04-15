# WAP to check no. is even or odd but it should divisible by 5.
a=int(input("enter the no."))
if a%5==0:
    if a%2==0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")
else:
    print("odd")