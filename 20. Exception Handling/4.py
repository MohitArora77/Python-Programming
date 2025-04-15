# Customized Error Error :

# for i in range(1,6):
#     print(i)
#     raise ValueError ('This is userdefines error')

# Customized Exception :
def func_even():
    a=int(input("enter the number:"))
    if a%2==0:
            print("EVEN")
    else:
            raise ValueError("IT IS AN ODD NUMBER NOT EVEN")  # CUSTOMIZED EXCEPTION USING ""RAISE"" KEYWORD
    return a
x=func_even()
print(x)