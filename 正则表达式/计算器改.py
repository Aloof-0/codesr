# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 23:15
# @Author   : 高冷
# @FileName  : 计算器改.py

# 1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))

import re

name = input("")


# 去除英文字母
def number(s):
    ok = True
    if re.findall("[a-zA-Z]", s):
        print("flase")
        ok = False
    else:
        return ok

# 替换
def format(s) :
    s = s.replace(" ", "")
    s = s.replace("+-", "-")
    s = s.replace("-+", "-")
    return s

# 取最小的括号
def xiao(s):
    b = re.search("\([^()]+\)",s)
    print(b.group())





while True:
    if number(name) == True:
        abv = format(name)
        if "(" in abv:
            xiao(abv)
        else:
            print(abv)
    break

