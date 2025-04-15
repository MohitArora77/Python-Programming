# a="abadcdadca"
# out=" "
# for i in range(len(a)):
#     out+=a[i]+chr(ord(a[i])-48)
# print(out)
        
# alternate
a="abaacdcabcd"
out=""
for i in a:
    out+=i+str(ord(i)-96)
print(out)