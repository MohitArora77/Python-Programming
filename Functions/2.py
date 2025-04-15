# find the nth prime no.
def prime(n):
    count=0
    for i in range(1,n+1):
        if (n%i==0):
            count+=1
    if count==2:
        return True
    else:
        return False
        
def prime_num(n):
    i=2
    count=0
    while count!=n:
        if prime(i)==True: 
            count+=1
        i+=1
    print(i-1)
    
prime_num(3)