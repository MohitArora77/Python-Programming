# take a list to store factorial from 1 to 10.
out=[]
for i in range(1,11):
    fact=1
    for j in range(1,i+1):
            fact*=j
    out+=[fact]
print(out)
    