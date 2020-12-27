# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 11:34
# @Author   : 高冷
# @FileName  : 公有和私有字段.py

"""
成员修饰符
            1.公有成员

            2.私有成员 前面加__就是私有
                                        1.私有字段
                                        2.私有方法

! 私有的外部无法直接访问, 只能内部间接访问
! 无法把私有的继承 ,自能继承公有的

"""

# 私有字段 (普通字段)

class Foo():
    def __init__(self, name, age):
        self.name = name
        # self.age = age 公有字段
        self.__age = age   # 私有字段,外部无法直接访问

    def show(self):
        print("私有字段 (普通字段)", self.__age)   # 只能用方法调用 间接访问

obj = Foo("alex", 18)
# print(obj.__age) 出错  //不能直接访问
obj.show()


# 私有字段 (静态字段)

class Koo:
    __v = 36                # 私有字段,外部无法直接访问

    def show(self):
        print("私有字段 (静态字段)", Koo.__v)

obj = Koo()
obj.show()

# 私有方法(普通方法)

class OOL:
    def __f1(self):         # 私有字段,外部无法直接访问
        print("私有方法(普通方法)", 123)

    def f2(self):
        self.__f1()

obj = OOL()
obj.f2()

# 私有方法(静态方法)

class Foop:
    @staticmethod
    def __f1():             # 私有字段,外部无法直接访问
        print("私有方法(静态方法)", 123)
    @staticmethod
    def show():
        Foop.__f1()
Foop.show()
