# -*- coding: utf-8 -*-
# @Time    : 2019/12/8 12:29
# @Author   : 高冷
# @FileName  : 元类.py

# python 中的一切皆对象
class Foo:
    pass


obj = Foo()

"""
1. OBJ      是一个对象 他是FOO的对象
2. FOO 其实也是一个对象 他是type的对象
3.type('类名', (继承),类的方法)
"""


class FOO:
    def func(self):
        function()


# 一样
def function():
    print("aaa")


Foo = type('Foo', (object,), {'func': function()})  # //type('类名', (继承),类的方法)


#    重点
class Mytype(type):
    def __init__(self, *args, **kwargs):
        print(13)

    def __call__(self, *args, **kwargs):
        print(123)
        self.__init__(Foo)  # 如果想调用Foo子类方法只能这样
        self.aaa(Foo)


class Foo(metaclass=Mytype):
    # 这里的FOO类其实就是Mytype的对象, 它已经执行了Foo = mytype(),
    # 又因为Mytype()会执行MYtype的构造方法
    # 然后Foo()就执行了Mytype的call方法
    def __init__(self):
        print(132)

    def aaa(self):
        Foo.__init__(self)


obj = Foo()

# 第一阶段：解释器从上到下执行代码创建Foo类
# 第二阶段：通过Foo类创建obj对象
