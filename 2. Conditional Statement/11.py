#WAP to check the character is uppercase or lowercase or a no. or a special character.
a=input("enter the character:")
if 'a'<=a<='z':
    print("lowercase")
elif 'A'<=a<='Z':
    print("Uppercase")
elif '0'<=a<='9':
    print("a no.")
else:
    print("special character")
    