# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 9:16
# @Author   : 高冷
# @FileName  : LOCK锁.py
# @web       ：https://www.cnblogs.com/Nicholas0707/p/11440491.html

import time
import threading
# 同步锁    线程修改同一个共享数据时，会发生数据覆盖或丢失的问题。则需要加锁
"""
线程1抢到GIL锁，拿到执行权限，开始执行，然后加了一把Lock，还没有执行完毕，即线程1还未释放Lock，有可能线程2抢到GIL锁，开始执行，
执行过程中发现Lock还没有被线程1释放，于是线程2进入阻塞，被夺走执行权限，有可能线程1拿到GIL，然后正常执行到释放Lock。。。这就导致了串行运行的效果
既然是串行，那我们执行

　　t1.start()
　　t1.join
　　t2.start()
　　t2.join()

　　这也是串行执行啊，为何还要加Lock呢，需知join是等待t1所有的代码执行完，相当于锁住了t1的所有代码，而Lock只是锁住一部分操作共享数据的代码。
"""
# 不加锁与加锁后  // 加锁前 num怎么都不会为0 加锁后为0
# 这里让设置全局变量num = 100 让他循环-100次每次减1,即num为0则正确
num = 100
def threads():
    global num
    lock.acquire()
    temp = num
    time.sleep(0.0001)
    num = temp - 1
    lock.release()
thread = []
lock = threading.Lock()
for i in range(100):
    t1 = threading.Thread(target=threads)
    t1.start()
    thread.append(t1)
for i in thread:
    i.join()
print("num:", num)

