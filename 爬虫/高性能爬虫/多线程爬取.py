import threading
import time


def a(num):
    for i in range(0, 10):

        print(num)
        time.sleep(10)


def b(a):
    for i in range(0,10):
        print("NO")
        time.sleep(0.1)


if __name__ == "__main__":
    t2 = threading.Thread(target=a, args=("t2",))
    b = threading.Thread(target=b, args=("t1",))
    b.start()
    t2.start()
