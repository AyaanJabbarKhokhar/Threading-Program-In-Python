import threading
import time

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)


t1 = threading.Thread(target=func, args=[3])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()