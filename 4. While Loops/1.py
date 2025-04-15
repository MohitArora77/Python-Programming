# WAp to print Hello 10 times
# i=1
# while i<=10:
#     print("Hello",end=" ") # Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello 
#     i+=1

# WAP to print 1st 10 natural numbers.
# i=1
# while i<=10:
#     print(i,end=" ")  # 1 2 3 4 5 6 7 8 9 10
#     i+=1
    
# WAP to print all the evn numbers less than 100.
# i=1
# while i<=100:
#     if i%2==0:
#         print(i,end=" ") #2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100
#     i+=1
    
# WAP to extract a number which is divided by 5 , with its square  and less than 50
# i=1
# while i<50:
#     if i%5==0:
#         print(i,i**2,end=" ") # 5 25 10 100 15 225 20 400 25 625 30 900 35 1225 40 1600 45 2025 
#     i+=1

# Wap to extract all the odd no. from m to n

# m=int(input("enter the number :"))
# n=int(input("enter the number :"))
# while (m<=n):
#     if m%2!=0:
#         print(m,end=" ") # 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39
#     m+=1
    
# WAP to find the sum of natural no.
# i=1
# sum=0
# while i<=10:
#     sum+=i
#     print(sum,end=" ") #1 3 6 10 15 21 28 36 45 55 
#     i+=1
# print(f"The Sum of 1st 10 natural number : {sum}") # 55

# WAP to find the product of the 1st 10 natural number.
# i=1
# prod=1
# while i<=10:
#     prod*=i
#     i+=1
# print(f"The Product of the 1st 10 natural number : {prod}")

# WAP to find the reverse of the number
# n=789
# rev=0
# while n>0:
#     temp=n%10
#     rev=rev*10+temp
#     n=n//10
# print(rev)

# WAP to print the reverse of the string
# s="Python is easy".split()
# out=" "
# i=len(s)-1
# while i>2:
#     out+=s[i][::-1]+" "
#     i-=1
# print(out)
    
# WAP to print the table of the number.
# n=int(input("enter the number:"))
# i=1
# while i<=10:
#     print(f"{n} X {i} = {n*i}")
#     i+=1

# WAP to find the sum of the digit in the number
# n=int(input("enter the number : "))
# sum=0

# while n>0:
#     temp=n%10
#     sum+=temp
#     n=n//10
# print(sum)

# WAP to print all the string present in the list whose len is greater than 3
s=["hello",34,4+8j,"bye","am","good",321,34.45]
i=0
out=[]
while i<len(s):
    if type(s[i])==str and len(s[i])>3:
        out+=[s[i]]
    i+=1
print(out) # ['hello', 'good']