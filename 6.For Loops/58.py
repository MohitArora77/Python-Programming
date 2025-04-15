a="Python is very easy".split()
out={ }
for i in range(0,len(a)):
    if i%2==0:
        out[a[i]]=a[i][::-1]+str(len(a[i]))
        i+=1
    else:
        out[a[i]]=len(a[i])*2
print(out)
