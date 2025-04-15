u='abc'
pw='123'
usn=input("enter the name:")
psw=input("enter the password:")
if usn==u:
    if psw==pw:
        print("Login Success")
    else:
        print("Username is okay but password is incorrect")
else:
    print("declined, Try Again!!")
