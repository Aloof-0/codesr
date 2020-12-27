# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 20:59
# @Author   : 高冷
# @FileName  : 继承.py

# 继承，面向对象中的继承和现实生活中的继承相同，即：子可以继承父的内容。
"""
1.
class 父类:
    PASS

CLASS 子类(父类):
    PASS

2. 重写
    防止执行父类的方法

3.self永远是执行方的调用者(对象)

4.如果非要用父类则 1. super(当前类名, self).你要用的函数 2.po.nnn(self) 父类名.你要用的函数(self)

5.python支持多继承
    a.左侧优先
    b.一条路走到黑
    c.同一个根时,根最后执行
"""
class F:      # 父类;基类
    def f1(self):
        print("part1: f.f1")
    def f2(self):
        print("part1: f.f2")
class S(F):   # S(F)继承了父类 称为 子类,派生类
    def s1(self):
        print("part1: s.s2")
obj = S()
obj.s1()
obj.f1()



# init_也可以继承

class K:
    def __init__(self):
        self.name = "part2: 111"
    def aaa(self):
        print("part:2 aaa")
    def bbb(self):
        print("part:2 bbb")


class O(K):
    def ccc(self):
        super(O, self).aaa()
        print(self.name)

obj1 = O()
obj1.ccc()


# 假如父与子类都有相同方法,则取子类     如果非要用父类则 1. super(当前类名, self).你要用的函数 2.po.nnn(self) 父类名.你要用的函数(self)
class Po:
    def nnn(self):
        print("2")
class OP(Po):
    def nnn(self):
        # 如果非要用父类则 super(当前类名, self).nnn() 你要用的函数  即执行父类中的nnn方法
        super(OP, self).nnn()
        Po.nnn(self) # 与 super一样
        print("part3: 3")

obj2 = OP()
obj2.nnn() # nnn中的self指的是形参,此时代指obj2

