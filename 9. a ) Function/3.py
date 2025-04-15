#Take one list contain 3,4 no. find greatest no.
def func(a,b,c,d):
    if a>b and a>c and a>d:
        return "greatest a"
    if b>c and b>d:
        return "greatest b"
    if c>d:      
        return "greatest c"
    else:
        return "greatest d"
print(func(5,3,2,3))
        