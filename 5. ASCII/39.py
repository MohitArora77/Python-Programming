#WAP to check the string is palindrome.
'''a="naman"
i=0
a1=" "
rev=0
a2=len(a)-1
while i<len(a):
    if a[i]==a:
        rev+=a[a2-i]
        i+=1
        
    elif rev==a:
        print("Palindrome")
print(rev)'''
    
a="naman"
a1=" "
i=len(a)-1
while i>=0:
    a1+=a[i]
    i-=1
if a==a1:
    print("palindrome")
else:
    print("not a palindrome")