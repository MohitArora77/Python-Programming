# write a program to covert aall the alphabet from lowercase to uppercase from the given string

def f_name(a):
    out=''
    for i in a:
        if "a"<=i<="z":
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out
print(f_name("asdkuanhandnmiQWDWDWd"))