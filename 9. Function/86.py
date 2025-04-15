# Anagram
def anag():
    a="listen"
    a1="silent"
    if len(a)==len(a1) and sorted(a)==sorted(a1) :
        return "anagram"
    else:
        return "not anagram"
    
print(anag())

# without sorted.
def anag( ):
    a="silent"
    b="listen"
    c=0
    for i in a:
        for j in b:
            if i==j:
                c+=1
                if c==len(a):
                    print("anagram")
                else:
                    print("not a anagram")
            else:
                print("not in anagram")
    anag()
    
            
