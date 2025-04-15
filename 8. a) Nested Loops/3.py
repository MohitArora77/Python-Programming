a=[10,"hello",3+5j,321]
out=[]
for i in a:
    sum=0
    if type(i)==int:
        for j in str(i):
            sum+=int(j)
        out+=[sum]
print(out)
            
            