# Recursion
# Function calling itself again and again until the termination condition becomes True is known as Recursion
# Run time Stack Mechanism

# 1. n ->natural no. 
# def num(n):
#     if n==1:
#         print(n)
#     else:
#         print(n)
#         num(n-1)
# num(5)

# print n natural no. without using looping -> can be done using recursion 
def num(n,i=1):
   
    if i==n:
        print(i)
    else:
        print(i)
        num(n,i+1)
num(5)