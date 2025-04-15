# create a decorator for the mail 

def q_spider(func):
    def inner(*args,**kwargs):
        print("Hello Candidate")
        print("Good Morning")
        func(*args,**kwargs)   
        print("Thank and Regards")
        print("Qspider,Noida")
    return inner     

@q_spider
def stu_a():
    print("You Are Selected for the Internship Program")
    print("Program Will be going to start from 20/FEB/2025")
    print("Please Bring your Personal ID for Identififcation.")
stu_a()

print("="*50)
@q_spider
def diwali_greet():
    print("Wishing you a and ur family a Happy Diwali ")
diwali_greet()


