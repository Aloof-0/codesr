# -*- coding: utf-8 -*-
# @Time    : 2019/12/8 10:16
# @Author   : 高冷
# @FileName  : 特殊方法2.py

# __iter__  //  对象中的类的__iter__并自动获取返回值,循环上一步中返回的作用

class FOK:
    def __iter__(self):
        return iter([11, 22, 33])
obj12 = FOK()

for i in obj12.__iter__():
    print(i)
"""
1. 如果类有__iter__方法, 那么对象 => 可迭代对象
2. 对象__iter__()的返回值 : 迭代器
3. for循环迭代器 next
4. for循环可迭代对象 对象.__iter__() next

"""
