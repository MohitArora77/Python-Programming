a="abacdabacddba"
a1=" "
a2=0
b1=0
c1=0
d1=0
i=0
while i<len(a):
    if a[i]=='a':
        a2+=1
    elif a[i]=='b':
        b1+=1
    elif a[i]=='c':
        c1+=1
    elif a[i]=='d':
        d1+=1
    i+=1
print('a',a2,'b',b1,'c',c1,'d',d1)
    

a="abacdabacddba"
i=0
out=' '
while i<len(a):
    if a[i] not in out:
        out+=a[i]+str(a.count(a[i]))
    i=i+1
print(out) 
