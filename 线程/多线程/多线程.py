# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 18:25
# @Author   : 高冷
# @FileName  : 线程.py
# @web       ：https://www.cnblogs.com/yuanchenqi/articles/5733873.html

import time
import threading
"""
线程的概念： 1. 是操作系统能够进行运算调度的最小单位。本质上就是一串指令的集合。
             2. 线程是操作系统够进行运算调度的最小单位。它被包含在进程之中，是进程中的实际运作单位。一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务


进程的概念： 1. 以一个整体的形式暴露给操作系统管理，里面包含各种资源的调用。 对各种资源管理的集合就可以称为进程。


进程和线程的区别：
            1、线程共享内存空间，进程有独立的内存空间。
            2、线程启动速度快，进程启动速度慢。注意：二者的运行速度是无法比较的。
            3、线程是执行的指令集，进程是资源的集合
            4、两个子进程之间数据不共享，完全独立。同一个进程下的线程共享同一份数据。
            5、创建新的线程很简单，创建新的进程需要对他的父进程进行一次克隆。
            6、一个线程可以操作（控制）同一进程里的其他线程，但是进程只能操作子进程
            7、同一个进程的线程可以直接交流，两个进程想要通信，必须通过一个中间代理来实现。
            8、对于线程的修改，可能会影响到其他线程的行为。但是对于父进程的修改不会影响到子进程。
"""

# 多线程对象创建               //多线程对象 = theading.Thead(target = 参数名, args = (形参, ) )

def foo_1(n):
    print(n)
t1 = threading.Thread(target = foo_1, args = (1, ))     # //这就是创建了一个多线程对象
#        或
print("AA", "BB", "CC", "DD")
T1 = threading.Thread(target=print, args=("FF", "DD", "EE", "GG"))
T1.start()

# 多线程对象的使用            //多线程对象的.start()

def foo_2(n):
    print(n)
t2 = threading.Thread(target=foo_2, args=(2, ))
t2.start()

# join()方法  主要作用就是同步，它可以使得线程之间的并行执行变为串行执行。即T2等T1执行完才执行
# setDeamon() 守护线程  只要主线程走完 就自动结束,不管守护线程是否执行完

def foo_3(n):
    time.sleep(3)
    print(n, "wait for 3S")
def foo_31(n):
    time.sleep(4)
    print(n, "wait for 4S")

Thread = []
t1 = threading.Thread(target=foo_3, args=("T1",))
Thread.append(t1)
t2 = threading.Thread(target=foo_31, args=("T2",))
Thread.append(t2)

for i in Thread:
    # t2.setDaemon(True)        // T2设置为守护线程
    i.start()
    i.join()                    # 不加join()是多线程 加了就变成串行 本来是T1和T2同时执行即4S 但是现在是一共7S

# thread 模块提供的其他方法：
#   threading.currentThread(): 返回当前的线程变量。
#   threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
#   threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
#   除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
#   run(): 用以表示线程活动的方法。
#   start():启动线程活动。
#   join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
#   isAlive(): 返回线程是否活动的。
#   getName(): 返回线程名。

#  同步锁   这也是串行执行啊，为何还要加Lock呢，需知join是等待t1所有的代码执行完，相当于锁住了t1的所有代码，而Lock只是锁住一部分操作共享数据的代码。
def addNum():
    global num                  # 在每个线程中都获取这个全局变量
    # num-=1
    lock.acquire()
    temp = num
    print('--get num:', num)
    #time.sleep(0.1)            # 线程修改同一个共享数据时，会发生数据覆盖或丢失的问题。
    num = temp-1                # 对此公共变量进行-1操作
    lock.release()

num = 100                       # 设定一个共享变量
thread_list = []
lock=threading.Lock()

for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list:          # 等待所有线程执行完毕
    t.join()

print('final num:', num)



