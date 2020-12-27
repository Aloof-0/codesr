# -*- coding: utf-8 -*-
# @Time    : 8:55 
# @Author   : 高冷
# @FileName  : PyCharm


"""
队列是一种数据结构
"""

import queue
import threading
from random import randint
from time import sleep


class Production(threading.Thread):
    def run(self):
        while True:
            r=randint(0,100)
            q.put(r)
            print("生产出来%s号包子"%r)
            sleep(1)
class Proces(threading.Thread):
    def run(self):
        while True:
            re=q.get()
            print("吃掉%s号包子"%re)
if __name__=="__main__":
    q=queue.Queue(10)
    threads=[Production(),Production(),Production(),Proces()]
    for t in threads:
        t.start()
