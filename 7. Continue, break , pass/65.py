#Extract integer from the set.
a={1,2,3,4,5,'hello'}
out=set()
for i in a:
    if not type(i)==int:
        continue
    out.add(i)
print(out)
        
