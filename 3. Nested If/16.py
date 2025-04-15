#WAP to check the character is vowel or consonant but with nested form.
a=input("enter the character:")
if 'a'<=a<='z':
    if a in ('a','e','i','o','u'):
        print("Vowels")
    else:
        print("Consonant")
      
else:
    print("Not in alphabet")
    
          