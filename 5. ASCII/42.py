#WAP to take a list but the list should be add in set.
a=[1,2,34,3,2,1,'hello',4,5,2,1,3]
i=0
out=[ ]
while i<len(a):
    if a[i] not in out:
        out+=[a[i]]
    i+=1
print(out)
        
        
    