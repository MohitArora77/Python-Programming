#OOPS
# class name
class zoo: 
    # class members
    a="Monkey"    
    b="Elephant"
    c="Crocodile"
    
# Object name
abc=zoo()
xyz=zoo()

# Print the object 
print(zoo.a,zoo.b,zoo.c)
print(abc.a,abc.b,abc.c)
zoo.b="lion"
print(zoo.a,zoo.b,zoo.c)

zoo.d="tiger"

print(zoo.a,zoo.b,zoo.c,zoo.d)

print(zoo.a,zoo.b,zoo.c)
zoo.a="panda"

print(zoo.a,zoo.b,zoo.c)
print(abc.a,abc.b,abc.c)