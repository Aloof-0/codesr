# -*- coding: utf-8 -*-
# @Time    : 2019/11/23 0:13
# @Author   : 高冷
# @FileName  : shelve模块.py

# shelve模块比pickle模块简单，只有一个open函数，返回类似字典的对象，可读可写;
# key必须为字符串，而值可以是python所支持的数据类型
import shelve

f = shelve.open(r'shelve.txt')

f['stu1_info']={'name':'alex','age':'18'}
f['stu2_info']={'name':'alvin','age':'20'}
f['school_info']={'website':'oldboyedu.com','city':'beijing'}

print(f.get('stu_info')['age'])