# # Enclosed/non-local scope:
# a=100
# print(a)
def outer():
    a=10
    print(a)
    a+=20 # can able to modify enclosed variable in the outer function.
    print("Inside of enclosed function:", a)
    def inner():
        nonlocal a
        a-=20
        # a-=20 -> showw error can't modify the enclosed function in inner funtion.
        print("inside of inner function:",a)
    inner()
outer()
