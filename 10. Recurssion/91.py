def eve_sq(a,out=[],i=0):
    if i>=len(a):
        return out
    if type(a[i]) is int and a[i]%2==0:
        out+=[a[i]**2]
    else:
        out+=[a[i]]
    return eve_sq(a,out,i+1)
print(eve_sq([2,3.5,7,8,3+5j]))