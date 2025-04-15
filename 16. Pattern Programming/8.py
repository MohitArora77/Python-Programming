# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print(j,end=" ")
#         else:
#             print(j,end=" ")
#     print()
    
# n=5
# num=int(input("enter the num:"))
# for i in range(1,n+1):
#     k=num
#     for j in range(1,n+1):
#         if i>=j:
#             print(k,end=" ")
#             k+=1
#         else:
#             print(end=" ")
#     print()

# n=5
# a=eval(input("enter the num:"))
# for i in range(1,n+1):
#     k=a
#     for j in range(1,n+1):
#         if i+j>=n+1:
#             print(k,end=" ")
#         else:
#             print("  ",end=" ")
#         k+=1
        
#     print()
    
    
# n=5
# a=eval(input("enter the num:"))
# for i in range(1,n+1):
#     k=a
#     for j in range(1,n+1):
#         if i+j>=n+1:
#             print(chr(k),end=" ")
#         else:
#             print(" ",end=" ")
#         k+=1
        
#     print()

n=5
a=eval(input("enter the num:"))
for i in range(1,n+1):
    k=a
    for j in range(1,n+1):
        if i+j<=n+1:
            print(i,end=" ")
        else:
            print(" ",end=" ")
        k+=1
        
    print()