from time import sleep
from threading import *


class Hello(Thread):  # 1st Thread
    def run(self):  # overrides the inbuilt method of thread class
        for i in range(5):
            print("hello")
            sleep(1)  # Delays the execution time


class Hi(Thread):  # 2nd Thread
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)  # Delays the execution time to avoid collision


# Creating object of the classes
t1 = Hello()
t2 = Hi()

t1.start()  # start will invoke run method in hello class
sleep(0.2)  # To avoid collision when using multi threading since both the class executes simultaneously
t2.start()  # start will invoke run method in hi class

t1.join()
t2.join()

print("bye")  # this bye is executed by main thread


