#WAP to extract all the uppercase, lowercase, number, special characters from your email id.
a="SoloPlay77@gmail.com"
char=''
low=''
up=''
num=''
i=0
while i<len(a):
    if 'a'<=a[i]<='z':
        low+=a[i]
        i+=1
    elif 'A'<=a[i]<='Z':
        up+=a[i]
        i+=1
    elif '0'<=a[i]<='9':
        num+=a[i]
        i+=1
    else:
        char+=a[i]
        i+=1
print(low)
print(up)
print(num)
print(char)
 