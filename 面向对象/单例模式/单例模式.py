# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 16:58
# @Author   : 高冷
# @FileName  : 单例模式.py
# @web       :  https://www.cnblogs.com/wupeiqi/p/5017742.html

"""
每个请求到来，都需要在内存里创建一个实例，再通过该实例执行指定的方法。

那么问题来了...如果并发量大的话，内存里就会存在非常多功能上一模一样的对象。存在这些对象肯定会消耗内存，对于这些功能相同的对象可以在内存中仅创建一个，需要时都去调用，也是极好的！！！

铛铛 铛铛 铛铛铛铛铛，单例模式出马，单例模式用来保证内存中仅存在一个实例！！！

通过面向对象的特性，构造出单例模式：
"""

class dan:

    __obj = None

    @staticmethod
    def dan():
        if dan.__obj:
            return dan.__obj
        else:
            dan.__obj = dan()
            return dan.__obj

    def ok(self):
        print("123")

obj = dan.dan()
obj.ok()
