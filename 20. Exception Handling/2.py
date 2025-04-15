#  Generic Excpetion Handling:
# When we don't know which type of exception will rise in that case we will use General Exception Handling.
# In this case we cannot provide specific solution to the solution.

# try:
#     a=int(input("enter the Number:"))
#     b=int(input("enter the Number:"))
#     print(a/b)
# except Exception: # Class called exception
#     print("There are some errors in the code")
  
# KeyboardInterrrupt

# try:
#     i=1
#     while True: 
#         print(i)
#         i+=1
# except Exception:
#     print("There are some error :")
# finally:
#     print("Further statements of the programme")

# ctrl+c will break the program in between -> keyboardInterrupt

# Example-1 ->
# try:
#     a=int(input("enter the number :"))
#     l=[1,2,3,4,5]
#     print(l[a])
# except Exception:

#         print("Invalid Syntax")

# finally:
#         print(f"HERE IS YOUR VALUE : {l[a]} ")
#         print(f"HERE IS YOUR LIST : {l} ")
      
#EXAMPLE-2 -> (with keyBoardInterrupt (ctrl+c))
try:
    n=int(input("enter the number:"))
    while True:
        print(n)
except Exception:
    print("Invalid Syntax")
finally:
    print("KEY_BOARD_INTERRUPT")
    