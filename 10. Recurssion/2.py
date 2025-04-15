#WAP to find the sum of of a no. using recursion
# def num(n,sum=0):
#     if n==0:
#         print(sum)
#     else:
#         temp=n%10
#         sum=sum+temp
#         n=n//10
#         num(n,sum)
        
# num(453)

#Alternate1
def num1(n):
    if n==0:
        return 0
    else:
        return n%10+num1(n//10)
print(num1(453))

#Alternate2
def num2(n):
    if n==0:
        return 0

    return n%10+num2(n//10)
print(num2(453))