# n natural number
# n natural odd numbers.
#  n natural even numbers
#  create a list square of even number and cube of the odd numbers

# 1
# n=int(input("enter the num:"))
# var =[x for x in range(1,n+1)]
# print(var)

# 2 
# n1=int(input("enter the number:"))
# var1 =[x1 for x1 in range(0,n1+1) if x1%2==1]
# print(var1)

# 3.
# n2=int(input("enter the number:"))
# var2 =[x2 for x2 in range(0,n2+1) if x2%2==0]
# print(var2)

# 4. 
# n3=int(input("enter the num:"))
# var3=[x3**2 if x3%2==0 else x3**3 for x3 in range(0,n3+1) ]
# print(var3)

# 5.
# n4=int(input("enter the num:"))
# var4=[x4 for x4 in range(1,n4+1) if str(x4)==str(x4)[::-1] ]
# print(var4)

# #  6.
# s='hai'
# var5 =[(i,j)  for i in s for j in range(len(s))]
# print(var5)

#  7. 
list1=["apple",'pear','orange','pineapple']
print([i for i in list1 if len(i)>4])