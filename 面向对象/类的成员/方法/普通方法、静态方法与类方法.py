# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 10:15
# @Author   : 高冷
# @FileName  : 普通方法与静态方法.py

"""
普通方法:保存在类中,对象来调用,需要self这类参数

静态方法: 1.类的静态方法，不需要self这类参数，因为类的静态方法，不需要进行实例化，就可以进行调用
         2.可以通过类直接调用
         3.在类中的方法名称前加一个头标记@staticmethod。

类方法:  类的方法,由类直接调用,需要cls(类名)这类参数

#       方法总结:
                1 .普通方法: 保存在类中,由对象来调用    self =>对象
                2.静态方法: 保存在类中,由类来调用
                3.  类方法: 保存在类中,由类调用        cls=>当前类i


#
@staticmethod:静态方法，静态方法是不可以访问实例变量或类变量的,这个类方法实际上跟类没有什么关系，它只是类下面的一个函数，跟类本身没关系，只是名义上归类管。
它与类唯一的关联就是需要通过类名来调用这个方法
如果非要传参数，只有传自己
@classmethod:类方法只能访问类变量，不能访问实例变量
@property :属性方法,属性方法的作用就是通过@property把一个方法变成一个静态属性

"""

# 普通方法

class FOOL:
    def simple(self, name):
        # 需要self这类参数
        print(name)

obj1 = FOOL()
# 保存在类中,对象来调用,
obj1.simple("Priate")


# 特殊方法

class FOOL_2:
    @staticmethod
    def static(name):
        # 不需要self这类参数，
        print(name)

FOOL_2.static("man")
# 可以通过类直接调用


#类方法             @classmethod

FOOL_2.static("man")
# 可以通过类直接调用

class FOOL_3:
    @classmethod
    def special(cls):
        # cls是类名 需要cls类名
        print(cls)

FOOL_3.special()