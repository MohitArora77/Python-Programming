# using function extract all the integers in the list using recursion.
def ex_int(a,out=[],i=0):
    if i>=len(a):
        return out
    if type(a[i])==int:
          out+=[a[i]]
    return ex_int(a,out,i+1)
print(ex_int([12,"hello",23,4+5j,[1,2,3],'good']))