#  Filter function:
#  Filter funtion is an in-build function which is used to traverse to through the values of the collection and to extract the specified values.
#  The length of the output collection maybe equal or less than the length of the input collection.
#  Syntax:- var=fliter(f_name,collection/itreable datatype)
              #print(list(var))
#  Takes Argument:
#  1. Function name
#  2. Collection/Iterable datatype

#  Here the function should return always Ture or False as output
#  When it returns True : then only the values are considered.
#  when False: then no extraction

# list1=[10,"hii",4.5,"Bye",False]
# def type_func(list1):
#    if type(list1)==str:
#        return True
#    else:
#        return False

# # out=filter(type_func,list1)
# # print(list(out))       
# print(list(filter(lambda list1:type(list1)==str,list1))) # using lambda function

# 1.
list1=[121,343,11,78678,323,3245]
def pal(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
out=filter(pal,list1)
print(list(out))

# 2

def pal_num(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
out=filter(pal,range(1,100))
print(list(out))

# 3 
list2=[99,False,2.334,6+4j,4.91,"hii",5.45,2.445,5665]
print(list(filter(lambda list2:type(list2)==float and len(str(list2).split(".")[-1])==3,list2)))

#  filter,Map,reduce are the funtion because they take function as an argument.