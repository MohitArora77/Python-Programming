# Comprehension : It's a phenomenon of creating a new mutable collection by writing the code in the concise way or
# by using a sinlge line of statement.
#  can able to create -> list,set,dict
#  3 types of comprehension:1)list 2)set 3)dict

# 1) List Comprehension: It is a process of creating a list by using a single line statement.
# Syntax : i) var = [val for val in collection] -> General syntax (no condition)
# ii) var = [val1 for val1 in collection if condition] -> when 1 statement body(1 condition)
# iii) var =[val1 if condition else val2 fro val in collection] -> when 2 statement body ( 2 condtion)
# iv) var=[(var1,var2) for val1 in collection for val2 in collection] -> advance (nested for loop)

# var=[ x for x in range(1,11)]
# print(var)

# var1=[x for x in range(1,21) ]
# print(var1)

# var2=[ i for i in  range(1,21) if i%2==1]
# print(var2)

# var3=[i for i in range(1,21) if i%2==0]
# print(var3)

#  create a list containing n natutal numbers
# n=int(input("enter the number:"))
# nat=[i for i in range(1,n+1)]
# print(nat)

# create a list containing a natural even numbers
n1=int(input("enter the number:"))
even_nat=[i for i in range(1,n1+1) if i%2==0]
print(even_nat) 
