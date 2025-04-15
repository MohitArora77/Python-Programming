#armstrong no. :- these are no.
n=153
arm=0
while n>0:
    temp=n%10
    arm=temp*temp*temp+arm
    n=n//10
if arm==n:
    print("ARMSTRONG")
else:
    print( "NOT AMSTRONG")