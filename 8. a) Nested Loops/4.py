a="HaI EvErYONe".split()
out={}
for i in a:
    c=0
    for j in i:
        if "A"<=j<="Z":
            c+=1
    out[i]=c
print(out) 