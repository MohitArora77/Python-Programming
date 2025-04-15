#WAP to print cancat of 2 string if len of first str is greater than the 2nd string if not print the product of 1st str with len of 2nd string.
a=input("enter the str:")
b=input("enter the str:")
if len(a)>len(b):
    print(a+b)
else:
    print(a*len(b))