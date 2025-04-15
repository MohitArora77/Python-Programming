#Wap to extract upper case and even case but its ascii value will be divisble by 3.

def asc():
    a="ASDDFsdajhjdabj"
    out=""
    c=0
    for i in range(0,len(a)):
        if "A"<=a[i]<="Z":
            if i%2==0 and ord(chr(i))%3==0:
                out+=a[i]
                c+=1
    return out,c
print(asc())
                
            