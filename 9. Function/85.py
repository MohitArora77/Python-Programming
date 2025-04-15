# a=['hello',23,3+5j,"python",[1,2,3],34,'star',(1,3)]
# op= [5,23,3+5j,"python",[1,2,3],34,4,(1,3)]
def f_name(a):
    out=[]
    for i in range(0,len(a)):
        if type(a[i])==str and i%2==0:
            out+=[len(a[i])]
        else:
            out+=[a[i]]
    return out
print(f_name(['hello',23,3+5j,"python",[1,2,3],34,'star',(1,3)]))