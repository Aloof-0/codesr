# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 11:20
# @Author   : 高冷
# @FileName  : 封装.py

# 一、封装
"""
封装，顾名思义就是将内容封装到某个地方，以后再去调用被封装在某处的内容。

所以，在使用面向对象的封装特性时，需要：
1. 将内容封装到某处
2. 从某处调用被封装的内容
"""

# 1. 第一步：将内容封装到某处


class Foo:

    def __init__(self, name, age):                                # 称为构造方法,根据类创建对象时执行 即 XXX = foo()时执行
        self.name = name
        self.age = age

# 根据类创建对象
# 自动执行FOO类的__init__方法
                                                                  # 将WXC和18分别封装到obj1和obj2的name和age属性中
obj1 = Foo("WXC", "18")

# 根据类创建对象
# 自动执行FOO类的__init__方法
                                                                  # 将WXC和18分别封装到obj1和obj2的name和age属性中
obj2 = Foo("wbx", "20")

"""
lf 是一个形式参数，当执行 obj1 = Foo('wupeiqi', 18 ) 时，self 等于 obj1

                              当执行 obj2 = Foo('alex', 78 ) 时，self 等于 obj2

所以，内容其实被封装到了对象 obj1 和 obj2 中，每个对象中都有 name 和 age 属性，在内存里类似于下图来保存。
"""


# 第二步：从某处调用被封装的内容

"""
调用被封装的内容时，有两种情况：

        通过对象直接调用
        通过self间接调用
1、通过对象直接调用被封装的内容

上图展示了对象 obj1 和 obj2 在内存中保存的方式，根据保存格式可以如此调用被封装的内容：对象.属性名
"""

# 1、通过对象直接调用被封装的内容 上图展示了对象 obj1 和 obj2 在内存中保存的方式，根据保存格式可以如此调用被封装的内容：对象.属性名
class Fool:

    def __init__(self, name, age):
        self.name = name
        self.age = age


obj10 = Fool('wupeiqi', 18)
print(obj1.name)  # 直接调用obj1对象的name属性)
print(obj10.age)  # 直接调用obj1对象的age属性)

obj20 = Fool('alex', 73)
print(obj20.name)  # 直接调用obj2对象的name属性
print(obj20.age)   # 直接调用obj2对象的age属性












"""
小明，10岁，男，上山去砍柴
小明，10岁，男，开车去东北
小明，10岁，男，最爱大保健
老李，90岁，男，上山去砍柴
老李，90岁，男，开车去东北
老李，90岁，男，最爱大保健
"""

class koko:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sex = "男"

    def hihi(self, KOKO):
        print(self.name+","+self.age+","+self.sex, KOKO)


LLL = koko("小明", "10岁")
LLL.hihi("上山去砍柴")
LLL.hihi("开车去东北")
LLL.hihi("开车去东北")

ooo = koko("老李", "90岁")
ooo.hihi("上山去砍柴")
ooo.hihi("开车去东北")
ooo.hihi("开车去东北")


