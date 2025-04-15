# Multithreading

# 1) thread() class

'''import threading
from time import sleep

# Extended thread class
def display(msg):
    for i in range(5):
        # print("Python")
        print(msg)
        sleep(1)

def other(msg):
    for i in range(5):
        # print("Java")
        print(msg) # can take 1 argument as msg as well 
        sleep(1)

# Create Multiple thread        
t1=threading.Thread(target=display,args=('Python',))
t2=threading.Thread(target=other,args=('Java',))
t1.start() # To start the thread
t2.start()
# c=threading.current_thread() # Main thread
# print(c)
# Arguments will be send in tuple format --> (target=display,args=('Python'))
# But argument will be the insert datatype not tuple , to make it tuple we use ',' beside the insert data in the argument.
for i in range(5):
    print("Hello")''' # This will be prsent in main thread

import threading
from time import sleep

class MyThread(threading.Thread): # to create thread class
    def run(self):
        for i in range(1,6):
            print(i,end=" ")
            sleep(1)
            
class Alpha(threading.Thread):
    def run(self):
        for i in 'ABCDE':
            print(i,end=" ")
            

# object for MyThread class -> 
e1=MyThread()
e2=Alpha()
# to start the thread
e1.start()
# Join allow thread to complete before running other threads 
e1.join() # e1 ---> e2 will be joined --> remaing thread (in betwe)
e2.start()
e2.join()

# enumerate to check the threads
print(f'All the Active threads',threading.enumerate())
for i in range(6):
    print("Bye")
    sleep(1)

# Main thread will always be active (Default Thread)
print(f'All the Active threads',threading.enumerate())