# function and find the greatest no. among 3 no.
def gre():
    a,b,c=eval(input("enter the no.:"))
    if a>b and a>c:
            return a
    elif b>c:
            return b
    else:
            return c
print(gre())