#wap to extract all the vowels from a given string 
def vow():
    a="abcdreiesyhas"
    out=""
    c=0 
    for i in a:
        if i in "aeiouAEIOU":
            out+=i
            c+=1
    return out,c
print(vow())
 