#WAP to check the no. is divisible by 3 then print FIZZ, if the no. is divisible by 5 print buzz , if the no. is divisible by both then print fizzbuzz.
a=int( input("enter the no.:"))
if a%3==0 and a%5==0:
    print("FizzBuzz")
elif a%5==0:
    print("buzz")
elif a%3==0:
    print("Fizz")
