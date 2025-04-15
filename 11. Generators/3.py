# Generator: a functon able to create squence of values with the help of yield keyword
# A function contains atleast 1 yield keyword -> generator
# Generator is memory friendly bcz we can call thses generator when we need them intead of calling them againa and again
# a generator function returns generator object that's why we have to typecast it.
# Yield -> a Keyword which can be used to  return the n number of of values without chainging the flow of exccution.
# can be called a sper user requirements

# Ex: 1
# def fun():
#     print("Hello")
#     yield 10 ,20  # return value
#     print("Bye")
    
# x=fun()
# print(x) # Address where data is stored (Generator Object)

# TypeCast->
# print(list(x)) # [(10, 20)] 
# print(dict(x)) # {10: 20}
# print(set(x)) # {(10, 20)}
# print(tuple(x)) # ((10, 20),)
# print(str(x)) # Generator object

# Ex-2 ->
# list1=[False,8+3j,"hello",99,"python",8.9,"bye"]
# def fun(list1):
#     out=[]
#     for i in list1:
#         if type(i)==str:
#             out+=[i]
#     yield out
# x=fun([False,8+3j,"hello",99,"python",8.9,"bye"])
# print(list(x))

# Ex-3 ->
# list2=[False,8+3j,"hello",99,"python",8.9,"bye"]
# def fun1(list2):
#     for i in list2:
#         if type(i)==str:
#             yield i
            
# x=fun1(list2) 
# print(list(x)) # ['hello', 'python', 'bye']

# Ex-4 -> Extract all the special characters from a given string.
# def str_sp(str):
#     for i in str:
#         if not(i.isalnum()):
#             yield i
            
# x=str_sp("Hello#$sgd!@#ASDASDad213")
# print(list(x))            

# Ex-5 -> Return a list containing all the palindrome numbers from a given range.
# def pal_num(list1):
#     for i in list1:
#         if str(i)==str(i)[::-1]:
#             yield i

# x=pal_num(["hello",452,131,262,786,909])
# print(list(x))

# def pal_ran(s,e):
#     for i in range(s,e+1):
#         if str(i)==str(i)[::-1]:
#             yield i
# x=pal_ran(2,20)
# print(list(x)) # [2, 3, 4, 5, 6, 7, 8, 9, 11]
        

# Ex-6 -> Return a tuple containing all the prime no. in a given range.
# def prime_num(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#         else:
#             return True
# def prime_ran(s,e):
#     for i in range(s,e):
#         if prime_num(i)==True: 
#             yield i
    
# x=prime_ran(2,40)
# print(tuple(x))

# def prime(n):
#     for i in range(2,n):
#         c=1
#         for j in range(2,i):
#             if i %j==0:
#                 c+=1
#         if c==1:
#             yield i
# p=list(prime(30))
# print(p)

# def prime_num(n):
#     for i in range(2,n):
#      c=1
#      for j in range(2,i):
#            if i%j==0:
#                c+=1
#      if c==1:
#         yield i
            
# x=prime_num(30)
# print(tuple(x))

# Generators in Dictionary Examples :

# Ex-1 ->

# a="Python"
# out={'p': 'P'}
# def con_name():
#     a="python"
#     for i in a:
#             yield i.lower(),i.upper()
            
# x=con_name()
# print(dict(x))

# Ex-2 ->
# {'python': 'pn', 'is': 'is', 'easy': 'ey'}
# def func():
#     str="python is easy".split()
#     for i in str:
#         yield i,i[0:2]

# x=func()
# print(dict(x))

# Ex-3 -> {'python': 6, 'is': 2, 'easy': 4}
# ex-4 -> {'python': 'nohtyp', 'is': 'si', 'easy': 'ysae'}
# ex-5 -> {'python': 'nythop', 'is': 'si', 'easy': 'yase'}
# WAP to create dictionary where the keys are the numbers and values are the cube of those no. in a given range.
# ex-6 -> {'a97': 'A', 'b98': 'B', 'c99': 'C'}

# 3.
# def func():
#     s="Python is easy".split()
#     for i in s:
#         yield i,len(i)
# x=func()
# print(dict(x)) # {'Python': 6, 'is': 2, 'easy': 4}

# 4.
# def func(): 
#     s="Python is easy".split()
#     for i in s:
#         yield i,i[::-1]
# x=func()
# print(dict(x))    # {'Python': 'nohtyP', 'is': 'si', 'easy': 'ysae'}

# 5.
# def func():
#     s="Python is Easy".split()
#     for i in s:
#         yield i,i[-1]+i[1:-1]+i[0]
# x=func()
# print(dict(x)) # {'Python': 'nythoP', 'is': 'si', 'Easy': 'yasE'}

# 6. 
# def func(n):
#     for i in range(1,n+1):
#         yield i,i**3
# x=func(5)
# print(dict(x)) # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# 7.
# def func():
#     s="abc"
#     for i in s:
#         yield str(i)+str(ord(i)),i.upper()
# x=func()
# print(dict(x)) # {'a97': 'A', 'b98': 'B', 'c99': 'C'}[']