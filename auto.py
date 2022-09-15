#import plotly.express as px
import threading
import time

def thread_function1(a):
    print("Thread starting", a)
    while (True):
        e1.wait()
        print("event received", a)
        e1.clear()

def thread_function2(a):
    print("Thread starting", a)
    time.sleep(2)
    e1.set()
    print("Thread finishing", a)

e1 = threading.Event()
thread1 = threading.Thread(target=thread_function1, args=(1,))
thread2 = threading.Thread(target=thread_function2, args=(2,))

thread1.start()
thread2.start()