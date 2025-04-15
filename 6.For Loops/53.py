#WAP to take a string extract all the uppercase and all the lowercase, if the len of uppercase are more than length of lowercase print string as it is.Otherwise print concat of upper and lower case.

a="AbcDeFg"
l=""
u=""
for i in a:
    if "a"<=i<="z":
        l+=i
    elif "A"<=i<="Z":
        u+=i
if len(u)>len(l):
        print(a)
else:
        print(u+l)
    
        