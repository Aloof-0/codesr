# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 12:17
# @Author   : 高冷
# @FileName  : 线程.py

import threading
import time
star = time.time()
def doo(n):
    time.sleep(3)
    print(n)

def bar(n):
    time.sleep(2)
    print(n)

t1 = threading.Thread(target=doo, args=(1,))
t2 = threading.Thread(target=bar, args=(2,))

t1.start()
t2.start()
end = time.time()
print(end - star)
