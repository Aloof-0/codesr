# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 10:54
# @Author   : 高冷
# @FileName  : 属性方法.py
# @web       :  www.cnblogs.com/zhong2018/p/9016366.html
# @web2      :  www.cnblogs.com/zhangfengcian/p/10199935.html




#
#
"""
  @property :属性方法,属性方法的作用就是通过@property把一个方法变成一个静态属性
  1. 经典类中的属性只有一种访问方式，其对应被 @property 修饰的方法
  2. 新式类中的属性有三种访问方式，并分别对应了三个被@property、@方法名.setter、@方法名.deleter修饰的方法
  3. 由于新式类中具有三种访问方式，我们可以根据它们几个属性的访问特点，分别将三个方法定义为对同一个属性：获取、修改、删除
  其实就是一一对应
"""

class Goods:
    """python3中默认继承object类
        以python2、3执行此程序的结果不同，因为只有在python3中才有@xxx.setter  @xxx.deleter
    """
    @property
    def price(self):
        print('@property')

    @price.setter
    def price(self, value):
        print('@price.setter',value)

    @price.deleter
    def price(self):
        print('@price.deleter')

# ############### 调用 ###############
obj = Goods()
obj.price          # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
obj.price = 123    # 自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数
del obj.price      # 自动执行 @price.deleter 修饰的 price 方法

"""
定义时，在普通方法的基础上添加 @property 装饰器；
定义时，属性仅有一个self参数
调用时，无需括号
           方法：foo_obj.func()
           属性：foo_obj.prop
"""