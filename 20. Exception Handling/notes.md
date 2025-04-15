# EXCEPTION HANDLING :

# 3 Types of Exception :

1) Specific Exception Handling
2) Generic Exception Handling
3) Default Exception Handling

> TRY
> Except
> Finally

# Specific Exception Handling
> We know the exception

# Generic Excpetion Handling:

> When we don't know which type of exception will rise in that case we will use General Exception Handling.
> In this case we cannot provide specific solution to the solution.
> There is class which known as Exception (This class contains all the Exceptions).
> In Generic Expection Handling we will use one class i.e." Exception " -> which contains all the types of  exceptions. Except -> KeyboardInterrupt 

> Syntax :
try :

  Problem statement

except Exception  (contains all the error):

  Solution statement

  > Disadvantage -> it cannot hamdle keyboardInterrrupt

 * Note :Ctrl+C will break the program in between if the program is in infinte loop.

 
# Default Exception Handling :
> In this we can hanlde all the Exceptions including keyboard interrupt.

try:
problem statement

except:
solution statement

# CUSTOMIZED EXCEPTION :
> Python Support the user to throw exception according to its requirements.
> SYNTAX:
raise ErrorName,'msg'  
         |---> Standard ErrorName


# USER-DEFINED EXCEPTION :
> These are the exception which can be defined by the user.
> by " raise " Keyword.

> EX: 
class Ageerror(exception):
pass