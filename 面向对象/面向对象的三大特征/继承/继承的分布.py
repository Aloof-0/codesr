# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 11:46
# @Author   : 高冷
# @FileName  : 继承的分布.py


class Star:
    def __init__(self):
        print("star")

class Moon(Star):
    def __init__(self):
        print("moon")
        Star.__init__(self)

    def wu(self):
        print("wu")
        self.rabbit()
    def rabbit(self):
        print("Moon.rabbit")


class Sun:
        def rabbit(self):
            print("sun.rabbit")

class The_earth(Sun, Moon):
        pass

obj = The_earth()
obj.wu()

