#Wap to find greatest no. among 3 no. 
a= int(input("enter the no."))
b= int(input("enter the no."))
c= int(input("enter the no."))
if a>b and a>c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
elif c>a and c>b:
    print("c is greatest")
    
    
    
# Alter Method:-
a,b,c,d=eval(input("enter the no."))
if a>b and a>c and a>d:
    print("a is greatest")
elif b>c and b>d:
    print("b is greatest")
elif c>d:
    print("c is greatest")
else:
    print("d is greatest")