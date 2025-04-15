#If Programs
#WAP to check tye character is uppercase.

a=input("enter the character:")
if 'A'<= a <='Z':
    print("upper")

#'a'<=char<='z' small
#'0'<=char<='9' number

#WAP to check last value of a list is the string and its length more than 3.
l=[1,2,3,'hello']
if  type(l[-1])==str and len(l[-1])>3:
        print("yes")
        
print(isinstance(10.8,int))

#WAP to check the data is the multivalue datatype.
a=input("enter the data:")
print(isinstance('a',(int,str,tuple)))

#2 
data=eval(input("enter the value:"))
if type(data) in [str,list,tuple,set,dict]:
    print("multivalue data")
    
#WAP to check the string in palindrome.
a=input("enter the value")
if a[:]==a[::-1]:
    print("palindrome")
    
    
a=int(input("enter the no.:"))
if a% 2==0:
    print("Even no.",a)
    