def bin_num(a,b,i=0,c1=0,c2=0):
    if  i >=len(a) and i>=len(b):
        return c1-c2
    if a[i]=='1':
        c1+=1
    if b[i]=='1':
        c2+=1
    
    return bin_num(a,b,c1,c2,i+1)
print(bin_num('0101100000110001','1110010001001100'))



# print(abs(a.count('1')-b.count('1')))
