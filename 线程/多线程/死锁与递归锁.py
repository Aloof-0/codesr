# -*- coding: utf-8 -*-
# @Time    : 2019/12/29 22:07
# @Author   : 高冷
# @FileName  : 死锁与递归锁.py
"""
死锁的一个原因是互斥锁。假设银行系统中，用户a试图转账100块给用户b，与此同时用户b试图转账200块给用户a，则可能产生死锁。
2个线程互相等待对方的锁，互相占用着资源不释放
在多线程程序中，死锁问题很大一部分是由于线程同时获取多个锁造成的。举个例子：一个线程获取了第一个锁，然后在获取第二个锁的 时候发生阻塞，
那么这个线程就可能阻塞其他线程的执行，从而导致整个程序假死。
解决方法: 递归锁 LOCK = thread.RLock()
lockA=threading.Lock()
lockB=threading.Lock()<br>#--------------<br>lock=threading.RLock()
"""

"""
递归锁：
　　互斥锁如果嵌套了多个锁之后，会将自己锁死永远都出不来了。
　　这个时候可以使用递归锁，它相当于一个字典，记录了锁的门与锁的对应值，当开门的时候会根据对应来开锁。
"""

# 死锁 和 递归锁
import threading
import time
class threads(threading.Thread):

    def A(self):
        lockA.acquire()
        # lock.acquire()
        print("lockA")
        time.sleep(2)
        lockB.acquire()
        print("lockB")  # B 和 A 2个线程互相等待对方的锁，互相占用着资源不释放

        lockB.release()
        # lock.release()
        lockA.release()

    def B(self):
        lockB.acquire()
        print("lockB")
        time.sleep(3)
        lockA.acquire()
        print("lockA")

        lockA.release()
        lockB.release()
    def run(self):
        self.A()
        self.B()

# lock = threading.RLock()
lockA = threading.Lock()
lockB = threading.Lock()

thread = []
for i in range(5):
    thread.append(threads())
for t in thread:
    t.start()
for t in thread:
    t.join()

