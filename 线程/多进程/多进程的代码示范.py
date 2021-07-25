# -*- coding: utf-8 -*-
# @Time    : 2020/2/15, 12:08 
# @Author   : 高冷
# @FileName: 多进程的代码示范.py

# 1.创建一个普通的线程
import threading
def A(c):
    print("123"+c)
f = threading.Thread(target=A,args=("c",))
f.start()

# 2.LOCK锁                   lock.acquire(),lock.release()
import time
num = 100
def TIMES():
    global num
    lock.acquire()
    temp = num
    time.sleep(0.001)
    num =temp - 1
    lock.release()

lock = threading.Lock()

for i in range(100):
    t1 = threading.Thread(target=TIMES)
    t1.start()
    t1.join()
print("num:", num)

# 守护线程      //主线程结束不会等守护进程结束        setDaemon(True)

def a():
    print("123")
g = threading.Thread(target=a)
g.setDaemon(True)
g.start()

