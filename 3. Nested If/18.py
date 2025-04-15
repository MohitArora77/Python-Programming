# WAP to find the greatest in 5 no.
a,b,c,d,e=eval(input("enter the no."))
if a>b:
    if a>c:
        if a>d:
            if a>e:
                print("a is greatest")
            else:
                print("e is greatest")
        else:
            if d>e:
                print("d is greatest")
            else:
                print("e is greatest")
    else:
        if c>d:
            if c>e:
                print("c is greatest")
            else:
                print("e is greatest")
        else:
            if d>e:
                print("d is greatest")
            else:
                print("e is greatest")
else:
    if b>c:
        if b>d:
            if b>e:
                print("b is greatest")
            else:
                print("e is greatest")
        else:
            if d>e:
                print("d is greatest")
            else:
                print("e is greatest")
    else:
        if c>d:
            if c>e:
                print("c is greatest")
            else:
                print("e is greatest")
        else:
            if d>e:
                print("d is greatest")
            else:
                print("e is greatest") 