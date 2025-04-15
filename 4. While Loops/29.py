# split :- It is function which convert string into a list.
#rev the whole string 
a='python is very easy'.split()
out=" "
i=len(a)-1
while i>2:
    out+=a[i][::-1]+" "
    i-=1
print(out)

    

