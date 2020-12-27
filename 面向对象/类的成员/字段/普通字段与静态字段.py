# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 10:03
# @Author   : 高冷
# @FileName  : 普通字段与静态字段.py


"""
普通字段:保存对象中执行通过对象访问  __init__

静态字段:保存在类中 执行可以通过对象访问,也可以通过类访问
"""


# 普通字段

class FOOl:

    def __init__(self, name):
        # 普通对象,属于对象
        self.name = name
        print(self.name)

obj1 = FOOl("Pirate")


# 静态字段

class FOOL_2():

    okok = "god"  # 静态字段 属于类,通过类直接调用

    def __init__(self, name):
        # 普通对象,属于对象
        self.name = name
        print(self.name)
print(FOOL_2.okok)
