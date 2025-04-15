# ASCII: These are the standards followed universally.
a='hai hello'
i=0
a1=' '
while i<len(a):
    if 'a'<=a[i]<='z':
        
        a1+=chr(ord(a[i])-32)
    else:
        a1+=a[i]
    i+=1
print(a1)