#Else Program89
a=int(input("enter the no.:"))
if a% 2==0:
    print("Even no.",a)
else:
    print("Odd no.",a)
    
    
a=input("enter the string:")
if a== "a" or a== "e" or a== "i" or a== "o" or a== "u":
    print("Vowel")
else:
    print("Consonent")
    
a=input("enter  the string:")
if a in "AEIOUaeiou":
    print("Vowels")
else:
    print("Consonent")
    
#WAP to check the data is the multivalue datatype and its len is more than 5.
b=eval(input("enter the data:"))
if type(b) in [str,list,tuple,set,dict] and len(b)>5:
    print("Multivalue data")
else:
    print("not a multivalue data")
    
# WAP to print cube of a number if the no. is even otherwise print square of it.
a=int(input("enter the no."))
if a%2==0:
    a**3
    print("cube of a no.:",a)
else:
    a**2
    print("square of a no.",a)