#WAP
def wap():
    a="python is programming language".split()
    out={}
    for i in a:
        if i[0] not in out:
          out[i[0]]=[i]
        else:
          out[i[0]]+=[i]
    return out
print(wap()) # when we have return we use print to call the function.