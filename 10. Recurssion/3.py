#Product of digit of a number
#sum of n natural number
#product of n natural no
#list1=[10,20,30,40] op-> 100
# list2=[1,2,3,4] o/p-> 24

# 1. Product of digit of a number
# def num2(n):
#     if n==1:
#         return 1

#     return n%10*num2(n//10)
# print(num2(453))

# # def num(n,prod=1):
# #     if n==0:
# #         print(0)
# #     else:
# #         temp=n%10
# #         prod=prod*temp
# #         n=n//10
# #         num(n,prod)
        
# # num(453)

# # 2. Sum of n natural number
# def num(n,i=1):
   
#     if i==n:
#         print(i)
#     else:
#       print(i)
#       num(n,i+1)
#     if n==0:
#          return 0
#     else:
#          return n%10+num(n//10)
# print(num(453))

#4.
# list1=eval(input("enter a list:"))
# def add_list(list1,length):
#   if length==0:
#     return 0
#   else:
#     return list1[length-1]+add_list(list1,length-1)

# print(add_list(list1,len(list1)))

#5.
# list2=[1,2,3,4]
# def prod_list(list2,length1):
#   if length1==0:
#     return 1
#   else:
#     return list2[length1-1]*prod_list(list2,length1-1)
  
# print(prod_list(list2,len(list2)))


# #6. odd or even using recursion
# n=int(input("enter the number:"))
# def odd_even(n,i=2):
#   if n%i==0:
#     return "even"
#   else:
#     return "odd"
# print(odd_even(n))

#7. wap to execute n odd no.
# def odd_no(n,i=1):
#   if (n==i):
#     pass
#   elif (i%2!=0):
#     print(i)
#     odd_no(n,i+1)
#   else:
#     odd_no(n,i+1)
  
    
# odd_no(40)

# WAP to print n natural odd numbers
# n=10
# def odd_num(n):
#   if n>0:
#     odd_num(n-1)
#     if n%2!=0:
#       print(n)
#     else:
#       print(n)
# odd_num(n)

# sum of n natural no.
def num(n):
  if n==0:
    return 0
  else:
    return n + num(n-1)
print(num(5))

# product of n natural number.
def num1(n1):
  if n1==0:
    return 1
  else:
    return n1 * num1(n1-1)
print(num1(3))