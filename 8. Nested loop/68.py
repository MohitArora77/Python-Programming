a="Hai How are you".split()
out=[]
for i in a:
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    out+=[c]
print(out)