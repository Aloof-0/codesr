# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 9:28
# @Author   : 高冷
# @FileName  : 同步锁.py

# 条件变量同步(Condition)

"""
wait()：条件不满足时调用，线程会释放锁并进入等待阻塞；
notify()：条件创造后调用，通知等待池激活一个线程；
notifyAll()：条件创造后调用，通知等待池激活所有线程。
"""

import threading

class aaa(threading.Thread):

    def run(self):
        print("123")

abc = aaa()
abc.start()
