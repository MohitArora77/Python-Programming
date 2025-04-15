#  Scope of Variables
# Global Scope
a=10
print('At main space:',a)
def main():
    global a
    a+=30
    print('Inside the function:',a)
    
main()

class Out:
    global a
    a+=50
    print("Outside of the funtion:",a)
    
    @staticmethod
    def val():
        global a # we can use global keyword to modify the value of global at any level -> function , class.
        a+=90
        print('Inside the class:',a)
Out.val()    

#  modify
a+=90
print("After Modification:",a)