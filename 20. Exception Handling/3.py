#  Default Exception Handling :
# try:
#     i=1
#     while True: 
#         print(i)
#         i+=1
# except :
#     print("There are some error :")

# print("Further statements of the programme")

# Example-1 ->
try:
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    while True: 
       print(a+b)
       break
except:
    print("Invalid syntax")
finally:
    print("DEFAULT_EXCEPTION_HANDLING")
    