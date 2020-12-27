# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:03
# @Author   : 高冷
# @FileName  : 面向对象的特殊方法.py

# 1.super() 函数            super(当前类名, self).你要用的函数()    与po.nnn(self) 父类名.你要用的函数(self)一样
"""
super() 函数是用于调用父类(超类)的一个方法。

super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。

MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
如果非要用父类则 super(当前类名, self).nnn() 你要用的函数  即执行父类中的nnn方法
"""
class A(object):   # Python2.x 记得继承 object
    def add(self, x):
         y = x+1
         print(y)
class B(A):
    def add(self, x):
        super(B, self).add(x)
b = B()
b.add(2)  # 3


# __dict__  // 将对象封装的所有内容通过字典形式返回
class FOOJ:
    A = 0
    def __init__(self):
        self.name = "王八"
        self.age = 1000000
        print("5. __dict__  // 将对象封装的所有内容通过字典形式返回")
FOOJ()
print(FOOJ.__dict__)

