# Time method -> sleep

# import time
# print("HI")
# time.sleep(7)
# print("Hello")
# time.sleep(7)
# print("Bye")

# time method -> time
# import time
# start=time.time()
# print("Starting time is:",start)
# for i in range(0,20):
#     print(i)
# end=time.time()
# print("Ending time is:",end)
# print("Total Time Taken is:",end-start)

#  Create  adecorator to calculate the total time taken to execute any program
# import time
# start=time.time()
# print("Strating Time is :",start)
# for i in range(0,30):
#     if i%2==0:
#         print("even")
#     else:
#         print("odd")
# end=time.time()
# print("Ending Time is:",end)
# print("Total time taken is:",end-start)

#  Create  a decorator to calculate the total time taken to execute any program
def time_calculator(func):
    def inner(*args,**kwargs):
        import time
        start=time.time()
        print("Sarting time is :",start)
        func(*args,**kwargs)
        end=time.time()
        print("Ending Time is:",end)
        print("Total Time Taken is:",end-start)
    return inner

@time_calculator
def odd_even():
    for i in range(0,20):
        if i%2==0:
            print("even")
        else:
            print("odd")
odd_even()