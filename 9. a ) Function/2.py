#Function with return and with arguments

# def func(args):
#     out={}
#      True body statement
#     return out
# print(func("values"))

#WAP upper to lower
def func(a):
    a1=" "
    for i in a:
        if "a"<=i<="z":
            a1+=chr(ord(i)-32)
        else:
            a1+=chr(ord(i)+32)
    return a1
print(func("ABCDSSasddeedef"))