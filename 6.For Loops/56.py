a=[10,"hello",3+5j,[1,2],3.8]
out=[ ]
for i in a:
    if type(i) in [int,complex,float,bool]:
        out+=[1]
    else:
        out+=[len(i)] # to store str in list
print(out)
        
        
        
        