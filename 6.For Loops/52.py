#WAP to extract all the integer from the list using for loop
a=[1,2,3,'hello','string']

for i in a:
    if type(i)==int:
        print(i)