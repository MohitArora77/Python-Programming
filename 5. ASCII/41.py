a=[171,23,'hello',9999,319,'apple']
a1=[]
i=0
while i<len(a):
    if type(a[i])==int and str(a[i])==str(a[i])[::-1]:
        a1+=[a[i]]
    i+=1
print(a1)
    
    
        