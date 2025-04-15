a="abstqz"
out=""
for i in a:
    if i!='z':
     out+=str(chr(ord(i)+1))
    else:
        out+=str(chr(ord(i)-25))
print(out)

# Alternate
a="abstqz"
out=""
for i in a:
    if i=='z':
        out+='a'
    else:
        out+=chr(ord(i)+1)
print(out)