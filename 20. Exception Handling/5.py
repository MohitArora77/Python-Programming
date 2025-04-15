# USER-DEFAULT EXCEPTION :
# class AgeError(Exception):
#     pass

# age=int(input("Enter the age :"))
# if age>=50:
#     print("To early for marry")
#     raise AgeError("This is userdefined error")
# elif age>=18:
#     print("You can marry at any moment")
# else:
#     print("Sorry !! it's too late for u marry")
#     raise AgeError("This is userdefined error")

# User-defined Exception: out 3 no. either a or b must be greatest number

class GreatestError(Exception):
    pass
try:
    a,b,c=eval(input("Enter the Numbers:"))
    if (a>b) and (a>c):
        print("A is Greatest")
    elif (b>a) and (b>c) :
         print("A is Greatest")
    else:
        print("C is Greatest")
        raise GreatestError("The Number C must not be the Greatest")

finally:
    print("YOU HAVE THE GREATEST NUMBER")