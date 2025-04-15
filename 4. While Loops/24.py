# WAP to extract a number which is divisible by 5 with its square less than 50
i=1
while i<51:
    if i%5==0:
        print(i,i**2)
    i+=1