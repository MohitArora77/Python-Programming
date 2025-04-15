  # GENERATOR:
''' 
--> Genertor is a function which is used to generate sequence of values by the help of "Yield" keyword.
--> If a function contains atleast one "Yield" keyword inside of it , then it will be known as generator.
--> "Yield" is a keyword which is used to return n no. of values without breaking the flow of execution.
--> Generator function always return a generator object. so to get the required output we have to typecast it.
--. can be used on extract data based questions.
'''
# def gene():
#     print("hii")
#     yield 10,"SQL",True
#     print("hello")
#     yield 20,"python"
#     print("Bye")
#     yield 30,40 # will be in tuple format
# var=gene()
# print(list(var)) # need to typecast
# print(tuple(var)) # need to typecast
# # print(str(var)) # need to typecast for the collection

#  WAP to extract all the string value from the list
# list1=[False,8+3j,"hello",99,"python",8.9,"bye"]
# def string1(list1):
#     out=[]
#     for i in list1:
#         if type(i)==str:
#             out+=[i]
#     yield out
# var=string1(list1)
# print(list(var))

# list1=[False,8+3j,"hello",99,"python",8.9,"bye"]
# def str_list(list1):
#     for i in list1:
#         if type(i)==str:
#             yield i
# print(list(str_list(list1)))

# Extract all the special characters from a given string.
# Return a list containing all the palindrome numbers from a given range.
# Return a tuple containing all the prime no. in a given range.

def gene():
    yield 10,True
    print("hii")
    yield 20,"python"
    print("hello")
    yield 30,40
    yield (1,2),(200,500) #no mutable datatype
    print("Bye")
print(dict(gene()))