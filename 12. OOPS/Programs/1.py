class zoo:
    a="ape"
    b="bander"
    c="crocodile"

simran=zoo()
harsh=zoo()

print(zoo.a,zoo.b,zoo.c)
print(simran.a,simran.b,simran.c)
print(harsh.a,harsh.b,harsh.c)

zoo.a="anaconda"
print(zoo.a,zoo.b,zoo.c)
print(simran.a,simran.b,simran.c)
print(harsh.a,harsh.b,harsh.c)
simran.b="bhalu"
print(zoo.a,zoo.b,zoo.c)
print(simran.a,simran.b,simran.c)
print(harsh.a,harsh.b,harsh.c)

