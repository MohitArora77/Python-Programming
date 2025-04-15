#WAP to print all the factorial from range 1 to 10
a=[10,'hai',3+5j,321]
out=[]
for i in a:
    sum=0
    if type(a)==int:
        for j in str(i):
            sum+=int(j)
        out+=[sum]
print(out)
            
    
    