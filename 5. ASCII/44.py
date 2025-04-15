a="(())((())"
i=0
out=0
a2=0
while i<len(a):
    if a[i]==')':
        out+=1
    else:
        a2+=1
    i+=1
b=a2-out    
print(b)


#Alternate
a="(())((())"
print(abs(a.count('(')-a.count(')')))
### abs ####-> convert any negative data to positive data.
#abs(a2-out)

