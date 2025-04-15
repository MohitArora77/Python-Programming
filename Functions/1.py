# def add(a,b):
#     print(a+b)
# # add(10) #type error
# add(20,30)
# # type() -> type error
# # len()  -> type error

# Arguments without return
#create a function which is ued to chechk the no is odd or even
# def odd_even(num):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# odd_even(35)
# odd_even(34)

# arguments with using return function

# def sam():
#     print("hii")
#     print("hello")
#     return 10
# # sam()    
# v=sam()
# # print(v)
# print(sam())

# def odd_even(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
# print(odd_even(35))
# print(odd_even(34))

# 1.
# def prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             print("not prime")
#             exit()
# c=prime(2)
# print("prime")        

# 2.
# def prime(num):
#     for i in range(2,num):
#         if i%num==0:
#             print("Not a Prime no.")
#             break
#     else:  
#         print("Prime no.")       
# prime(2)

# 3. 
# def prime_no(n):
#     count=0
#     for i  in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         print("prime")
#     else:
#         print("not prime")
# prime_no(6)

# prime for series of no.

def series(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
for i in range(1,101):
    if series(i) == True:
        print(i,end=" ")
