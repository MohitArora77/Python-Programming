# 2.Map Function:

# --> It is an In-build function which is used to traverse through the collection to perform same task on each and every values of the collection. 
# --> range or length of the input must be equal with the length of the output.
# --> Syntax: var=map(func_name,IA)
# 2 Arguments-> i) Function name ii) iterable datatype / collection datatype / multivalue datatype / single value datatype.
# variable(var) will returns one map object, so to get the required output we have to typecast it.

# list1=[10,20,30,40]
# def square(n):
#     return n**2

# var_1=map(square,list1)
# print(list(var_1))  

# 
# list1=[10,20,30,40]
# square=lambda n:n**2

# var_1=map(square,list1)
# print(list(var_1))  

# #
# print(list(map(lambda n:n**2,eval(input("enter the list of range:")))))

# 1
s="Pyhton is easy".split()
def len_word(s):
    return len(s)
list1=list(map(len_word,s))
list1=list(map(len,s))
print(list1)
# o/p-> [6,2,4]


# 2. s="abc"
print(list(map(lambda s1:ord(s1),eval(input("enter the str:")))))

s="abc"
res=map(ord,s)
print(list(res))

# 3. WAP to get the list of factorial of the n natural number in a given range.
n=int(input("enter the no:"))
def fact_num(n):
    if n==0 or n==1:
        return 1
    return n*fact_num(n-1)

res1=map(fact_num,range(1,n+1))
print(list(res1))

# 4.    
s="python is easy".split()

s1=list(map(lambda s:s[::-1],s)) # map(fuctionname,collection)
print(" ".join(s1)) # join is used to convert any datatype into string here we have given space to separate it