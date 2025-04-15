#  Reduce(): It is a In-build function  which is used to reduce our iterable datatype into a single unit.
#  It uses a mathematical folding techique.
#  To use the reduce function we have to import the "functools" modules.
#  Syntax: from functools import reduce
#           var=reduce(f_name,collection)
        #   print(var)  => no need for typecasting.
        
# 1. 
list1=[10,20,30,40]

from functools import reduce
out=reduce(lambda a,b:a+b,list1)
print(out)

# 2.
list2=[22,44,12,4,32]

from functools import reduce
out1=reduce(lambda a,b: a if a>b else b,list2)
print(out1)