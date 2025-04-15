# Dictionary Comprehension:
# zip() : 
# It is an in-built fucntion which is used to combine 2 or more than 2 different iterables into a single iterable with respect to there index position.
# It creates a tuple to store the zip elements.
# It always consider the collection having shortest length.
# Zip() function always return some zip object so we have to typecast it.
#  syntax: var=Zip(collection1,coll2,....colln) ->> typecast the var -->> print(list(var)).
# Zip is used for filter, alignment
# If we want to iterate 2 collection at a time we use zip function.

# 1.
list1=[10,20,30,50,60]
list2=[30,40,50]
s="hello"
var=zip(list1,list2,s)
# print(var) ->  of the variable
print(list(var))

# If we want to iterate 2 collection at a time we use zip function.
# 2.
for i,j in zip(list1,list2):
    print(i,j)
    
# Dict Comprehension:

# var={Key:Value for val1 in collection}
# var={Key:Value for K,V in zip(collection,collection2)}
# var={Key:Value for val1 in collection if condition}
# var={Key:Value1 if condition else val2 for val in collection}

# 1.
# n=int(input("enter the no."))
# var={i:i**2 for i in range(1,n+1)}
# print(var)

# 2.
l1=['a','b','c']
l2=[7,8,9]
var1={k:v for k,v in zip(l1,l2)}
print(var1)

# 3. 
s="Hai HeLlO"
var2={i:ord(i) for i in s if i.isupper() }
print(var2)

# 4. 
list1=['a',8,3.4,[6,7],89]
list2=[10,3.4,'hello',9,[5,6]]
var3={i:j for i,j in zip(list1,list2) if type(i) not in (list,set,tuple)}
print(var3)

#  5. 
input=range(1,7)
print({i:i**2 if i%2==0 else i**3 for i in range(1,7)})