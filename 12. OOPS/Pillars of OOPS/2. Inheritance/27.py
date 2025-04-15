# heirarchical inheritance
class Pc:
    a=20
    b="hi"
class Cc(Pc):
    pass
class Cc2(Pc):
    pass
print(Cc.a,Cc.b)
print(Cc2.a,Cc2.b)