#WAP to extract all the uppercase from the given string.
a="hELLo"
out=" "
for i in a:
    if 'A'<=i<='Z':
        out+=i
print(out)
