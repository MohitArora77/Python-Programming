# 1) set Comprehension: It is a process of creating a set by using a single line statement.
# Syntax : i) var = {val for val in collection} -> General syntax (no condition)
# ii) var = {val1 for val1 in collection if condition} -> when 1 statement body(1 condition)
# iii) var ={val1 if condition else val2 fro val in collection} -> when 2 statement body ( 2 condtion)
# iv) var={(var1,var2) for val1 in collection for val2 in collection} -> advance (nested for loop)

#  store the prime number in a given range

# def func(a):
#     for i in range(2,a):
#         if a%i==0:
#             return False
#         else:
#             return True
# prime_set={num for num in range(1,int(input("enter the number:"))+1)if func(num)}
# print(prime_set)
    
#  WAP to extract all the immutable data from the given list and store in a set
list1=[10,'python',4+5j,[99,88,77],(1,2,3),{"hii","hello"}]
var={i for i in list1 if type(i) not in (dict,set,list)}
print (var)