# # Extract all the special characters from a given string.
# # Return a list containing all the palindrome numbers from a given range.
# # Return a tuple containing all the prime no. in a given range.


# # 1.
# str_1="kjashdj#$!%k123^F%HDJDK"
# def str_func(str_1):
#     for i in str_1:
#         if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
#             yield i
# print(list(str_func(str_1)))       
# # isalpha()
# # isnumeric()
# # isalnum()  
# # 1.
# str_2="kddfFSDF%$@#$R424"
# def str_f(str_2):
#     for i in str_2:
#         if not (i.isalnum()):
#             yield i
# var= list(str_f(str_2))
# str_out="".join(var) # able to convert list into str
# print(str_out)
# # print("".join(list(str_f(str_2))))

# # 2.
# def pal(n):
#     for i in range(1,n+1):
#         sum=0
#         a=i
#         while i>0:
#             d=i%10
#             sum=sum*10+d
#             i=i//10
#         if sum == a:
#             yield sum
# li=list(pal(200))
# print(li)

# # 2.
# # sv=int(input("enter the num:"))
# # ev=int(input("enter the num:"))
# # def pal_num(sv,ev):
# #     for i in range(sv,ev+1):
# #         if str(i)==str(i)[::-1]:
# #             yield i
# # print(list(pal_num(sv,ev)))
    

# # 3.
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

# # 3.
# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#         else:
#             return True
# sv=int(input("enter the num:"))
# ev=int(input("enter the num:"))
# def prime_num(sv,ev):
#     for i in range(sv,ev+1):
#         if prime(i)==True:
#             yield i
# print(tuple(prime_num(sv,ev)))

# 4. 
# def con_name():
#     a='python'
#     out={}
#     for i in range(len(a)):
#         if i==0 and 'a'<=a[i]<='z':
#             out[a[i]]=chr(ord(a[i])-32)
#             i+=1
#     print(out)
# con_name()

# # 4.
# s="python"
# def gene_dict(s):
#     for i in s:
#         yield i.lower(),i.upper()
# print(dict(gene_dict(s)))

# # 5. 
# s1="python is easy".split()
# def gene_dict1(s1):
#     for i in s1:
#         yield i,i[0]+i[-1]
# print(dict(gene_dict1(s1)))

# # 6.
# s1="python is easy".split()
# def gene_dict1(s1):
#     for i in s1:
#         yield i,len(i)
# print(dict(gene_dict1(s1)))

# #7.
# s1="python is easy".split()
# def gene_dict1(s1):
#     for i in s1:
#         yield i,i[::-1]
# print(dict(gene_dict1(s1)))

# # 8.
# s1="python is easy".split()
# def gene_dict1(s1):
#     for i in s1:
#         yield i,i[-1]+i[1:-1]+i[0]
# print(dict(gene_dict1(s1)))

# 9. WAP to create dictionary where the keys are the numbers and values are the cube of those no. in a given range.

# sv=int(input("enter the starting number:"))
# ev=int(input("enter the ending number:"))
# def gene_1(sv,ev):
#     for i in range(sv,ev+1):
#         yield i,i**3
# print(dict(gene_1(sv,ev)))

# 10.
s="abc"
def gene_2(s):
    for i in s:
        yield i+str(ord(i)),i.upper()
print(dict(gene_2(s)))