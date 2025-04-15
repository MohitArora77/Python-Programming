def instagram(func):
    def inner(*args,**kwargs):
        print("WWW.instagram.com")
        print('logged in')
        func(*args,**kwargs)
        print('logged out')
    return inner

@instagram
def abc_insta():
    print("MSG to Friend")
abc_insta()

print("="*50)

@instagram
def xyz_insta():
    print("MSG to GF")
xyz_insta()

print("="*50)
@instagram
def stu_insta():
    print("Post a Reel")
stu_insta() 

print("="*50)
@instagram
def msg_insta(a):
    print(f'No of msg: {a}')
    print("Checked The MSG")
msg_insta(10)