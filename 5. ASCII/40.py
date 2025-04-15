a=['abc',10,'python',3+5j,'English',3.5]
i=0
a1={}
while i<len(a):
    if type(a[i])== str:
        a1[a[i]]=len(a[i])
    i+=1
print(a1)
        