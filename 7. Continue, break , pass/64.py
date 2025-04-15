#WAP to extract all the upper case from the given string but using continue.
a="HelElWoR"
out=" "
for i in a:
    if 'A'<=i<='Z':
        print(i,end=" ")
    else:
        continue

a="HelElWoR"
out=" "
for i in a:
    if not ('A'<=i<='Z'):
        continue
    out+=i
print(out)