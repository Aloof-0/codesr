# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 16:49
# @Author   : 高冷
# @FileName  : 特殊方法.py

"""
        1.  __call__    //对象可以直接执行  obj()
        2. __int__     //自动执行对象 ___int__ 方法并将返回值赋给int对象
        3. __str       //自动执行对象 ___str__ 方法并将返回值赋给str对象'
        4. __add__   // __add__接受两个参数都是对象,两个对象相加才能进行调用这个函数
        5.__getitem__   // 自动执行li对象的类中的__gentitem__方法 对象[X] "X"当作参数传递给item   __setitem__

        __init__    类()自动执行
        __call__    对象() 类()() 自动执行
        __int__     int(对象)
        __str__     str(对象)
        __add__     对象 +  对象 = add方法的返回值
        __getitem__ 对象[]

一般这样用
class Foo:
    def __init__(self):
        self.name = 'alex'
        self.age  =  18
    def __str__(self):
        return self.name
    def __int__(self):
        return self.age
obj = Foo()
print(str(obj))
print(int(obj))
"""

# __call__    //对象可以直接执行  obj()
class FOO:
    def __call__(self, *args, **kwargs):
        print("1. __call__    //对象可以直接执行")
        print("obj()")
obj = FOO()
obj()


# __int__    //自动执行对象 ___init__ 方法并将返回值赋给int对象
class FOOL:
    def __int__(self):
        print("2. __int__    //自动执行对象 ___int__ 方法并将返回值赋给int对象")
        return 123
obj1 = FOOL()
print(int(obj1))

# __str__
class FOA:
    def __str__(self):
        print("3. __str__   //自动执行对象 ___init__ 方法并将返回值赋给int对象")
        return "str"
obj2 = FOA()
print(str(obj2))

# __add__   // __add__接受两个参数都是对象,两个对象相加才能进行调用这个函数
class FOOI:
    def __add__(self, other):
        return 10
obj10  = FOOI()
obj11 = FOOI()
print("4. __add__   //接受两个参数都是对象,两个对象相加才能进行调用这个函数 ")
print(obj10 + obj11)# 得到的是返回值 10

# __del__   // 析构方法 与构造方法相反 对象被销毁时自动执行

                        # pass

# __getitem__   // 自动执行li对象的类中的__gentitem__方法 对象[X] "X"当作参数传递给item

class FOOX:
    def __getitem__(self, item):
        return item + 10
li = FOOX()
r = li[8]
print("5.__getitem__   // 自动执行li对象的类中的__gentitem__方法 对象[X] X当作参数传递给item")
print(r)

