# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/27 23:04
@Auth ： 高冷Aloof
@File ：hello.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

a = []

for i in range(0, 101):
      a.append(i)

print(a)
k = 0
b = 3
for i in a:

    if a[k:b] == []:
        break
    print(a[k:b])
    k+=3
    b+=3
