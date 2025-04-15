# def no_dup():
#  a=[10,"Hai",25,"Hai",3+5j,10,"Hello",10]
#  out=[]
#  for i in range( 0,len(a)):
#      if a[i] not in out:
#          if type(a[i]) in [str,int] and a.count(a[i])>1:
#              out+=[a[i]]
#  return out
# print(no_dup())
    
# Alternate
def dupli():
    a=[10,'hai',3,'hai',3+5j,'hello',3,10]
    out=[]
    for i in a:
        if i not in out:
            if a.count(i)>1:
                out+=[i]
    return out
print(dupli())