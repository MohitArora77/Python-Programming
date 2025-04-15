def f_name():
    a="python"
    out=" "
    out+=a.capitalize()
    print(out)
f_name()

# alternate:-

def con_name():
    a='python'
    out=" "
    for i in range(len(a)):
        if i==0 and 'a'<=a[i]<='z':
            out+=chr(ord(a[i])-32)
        else:
            out+=a[i]
    print(out)
con_name()
        
a="python"
print(a.capitalize())
       
print("python".capitalize())