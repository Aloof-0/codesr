# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 9:49
# @Author   : 高冷
# @FileName  : 正则表达式方法2.py

import re

# 1.findall()   所有结果都返回到一个列表里

kkk = re.findall("koko", "kokookookoko")
print("1.", kkk)

# 2.search()    返回匹配的第一个对象,对象可以调用group()

sbpeng = re.search("fuck dog", "kkkjhfdskjfhksfuck dog")
print("2.", sbpeng.group())

# 3.match()     只在字符串开始匹配,也只返回一个对象,对象可以调用group()     //效果与^一样
lovecheng = re.match('pppp', 'pppp98456464')
print('3.', lovecheng.group())

# 4.split()     以分组为分割符的时候，分组内容也会被保存下来                //对于一个找不到匹配的字符串而言，split 不会对其作出分割

iamFear = re.split("1", "i1am1Fear")
print("4.", iamFear)

# 5.sub()      用于替换字符串中的匹配项。('规则','内容','替换的内容')

pldsn = re.sub('KOKO', 'LLLLKOKOLLLL', 'OKOK')
print('5.', pldsn)

# 6.compile()   用于定义一个规则
ppp = re.compile('ak47')
print('6.', ppp.findall('m4a1ak47'))


