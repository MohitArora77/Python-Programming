#WAP to extract the all the string present inside the list whose length is more than 3.
l=['hello', 'world', 'this', 'is' ,'New',324]
out=[]
i=0
while i<len(l):
    if type(l[i]) == str and len(l[i])>3:
        out+=[l[i]]
    i+=1
print(out)
    