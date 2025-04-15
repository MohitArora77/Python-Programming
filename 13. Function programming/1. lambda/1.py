# Functional programming (lambda,filter,map,reduce)
# 1. Lambda -->
# -> It is a keyword which iss used to perform the simple mathmatical operation. 
# -> AKA -> Single Line Function.
# -> It Takes n no. of arguments --> single Output
# -> This function has no name that's why it is called anonymous function. 
# -> name of the function(var)= lambda args:expression
#  -> to call the function->print(var())

# # Addition
# l=lambda a,b:a+b 
# print(l(3,4)) # we need to call the function
# print(l) # function Address

# print(lambda b,c:b*c(10,20))  # show the function address

#  WAP to concatenate first name and last name
#  WAP to reverse a no.

# 1. 
# con=lambda a,b:a+b
# print(con("Mohit"," Arora"))

# # 1.
# a1=eval(input("Enter the first_name:"))
# b1=eval(input("Enter the last_name:"))
# con=lambda a1,b1:a1+""+b1
# print(con(a1,b1))

# # 2.
# rev=lambda a:a[::-1]
# print(rev("34887"))

# # 2. 
# num=int(input("enter the num:"))
# rev=lambda num:str(num)[::-1]
# print(rev(num))
 
# 3.
# n=int(input("Enter the Number:"))
# def odd_even(n):
#     if n%2==0:
#         return "Even"
#     else:
#         return "Odd"
# print(odd_even(n))  

# # 3.
# def even_odd1(n):
#     if n%2==0:
#         return True
#     else:
#         return False

# # #3. 
# def even_odd(n):
#     return n%2==0
# print(even_odd(n))    #False

# # # # 3. 
# odd_even1=lambda n:n%2==0
# print(odd_even1(n))

# # syntax for odd even in lambda function->
# # var=lambda args: True statement body(TSB) if cond else False Statement body(FSB)   
# odd_even2=lambda n: "even no." if n%2==0 else "odd no"
# print(odd_even2(n))

#  check the given num is a plaindrome or not by using lamda function

# pal=lambda n:"palindrome" if str(n)[:]==str(n)[::-1] else "Not a Plaindrome"
# print(pal(n))

# # WAP to check is the data is mutable or immutable by using lambda function
# data=eval(input("enter the data:"))
# data1=lambda data: "Mutable" if type(data) in [dict,list,set] else "Immutable data"
# print(data1(data))

# WAP to find the sum of maximum of 5 num and min 2 no by using lambda
sum=lambda a,b,c=0,d=0,e=0:a+b+c+d+e 
print(sum(3,3,5,6,7))