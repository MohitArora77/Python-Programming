#WAP to extract all the palindrome integers from a given list
a=[121,999,787]
out=[]
for i in a:
    if not str(i)==str(i)[::-1] or not type(i)==int:
        continue
    out+=[i]
print(out)
    