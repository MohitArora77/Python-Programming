# Exception Handling

# Specific Exception HAndling :
# When we know the exception

# Example-1 ->
# try:
#     a=int(input("enter the Number:"))
#     b=int(input("enter the Number:"))
#     print(a/b)
# except ValueError:
#     print("The value of a and b should be integer")
# except ZeroDivisionError:
#     print("The value of b can not be zero")

#Example-2 ->
try:
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    # c=input("enter the data :")
    print(f"Sum of the number : {a+b}")
    # print(f"conactenate : {a+b+c}")
# except ValueError:
#     print("Invalid Value")
# except TypeError:
#     print("Invalid Type")
except Exception:
    print("Invalid Syntax")
