#  Local Scope
def outer():
    a=10

    print("Inside the enclosed function:",a)
    def inner():
        x=90
        print('Inside of the function:',x)
        x+=90
        print('Modify Inside the function:',x)
    inner()
outer()