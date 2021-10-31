# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 12:13
# @Author   : 高冷
# @FileName  : 正则计算器.py


# ！/usr/bin/env/ python3
# -*- coding: utf-8 -*-

"""用户输入计算表达式，显示计算结果"""

__author__ = 'Jack'

import re

bracket = re.compile(r'\([^()]+\)')  # 寻找最内层括号规则
mul = re.compile(r'(\d+\.?\d*\*-\d+\.?\d*)|(\d+\.?\d*\*\d+\.?\d*)')  # 寻找乘法运算规则
div = re.compile(r'(\d+\.?\d*/-\d+\.?\d*)|(\d+\.?\d*/\d+\.?\d*)')  # 寻找除法运算规则
add = re.compile(r'(-?\d+\.?\d*\+-\d+\.?\d*)|(-?\d+\.?\d*\+\d+\.?\d*)')  # 寻找加法运算规则
sub = re.compile(r'(-?\d+\.?\d*--\d+\.?\d*)|(-?\d+\.?\d*-\d+\.?\d*)')  # 寻找减法运算规则
c_f = re.compile(r'\(?\+?-?\d+\)?')  # 检查括号内是否运算完毕规则
strip = re.compile(r'[^(].*[^)]')  # 脱括号规则


def Mul(s):
    """计算表达式中的乘法运算"""
    exp = re.split(r'\*', mul.search(s).group())
    return s.replace(mul.search(s).group(), str(float(exp[0]) * float(exp[1])))


def Div(s):
    """计算表达式中的除法运算"""
    exp = re.split(r'/', div.search(s).group())
    return s.replace(div.search(s).group(), str(float(exp[0]) / float(exp[1])))


def Add(s):
    """计算表达式中的加法运算"""
    exp = re.split(r'\+', add.search(s).group())
    return s.replace(add.search(s).group(), str(float(exp[0]) + float(exp[1])))


def Sub(s):
    """计算表达式中的减法运算"""
    exp = sub.search(s).group()
    if exp.startswith('-'):  # 如果表达式形如：-2.2-1.2；需变换为：-（2.2+1.2）
        exp = exp.replace('-', '+')  # 将-号替换为+号；+2.2+1.2
        res = Add(exp).replace('+', '-')  # 调用Add运算，将返回值+3.4变为-3.4
    else:
        exp = re.split(r'-', exp)
        res = str(float(exp[0]) - float(exp[1]))
    return s.replace(sub.search(s).group(), res)


def calc():
    while True:
        s = input(
            'Please input the expression(q for quit):')  # 例：'1+2- (3*  4-3/2+ (   3-2*(3+  5 -3*  -0.2-3.3*2.2 -8.5/ 2.4 )+10) +10)'
        if s == 'q':
            break
        else:
            s = ''.join([x for x in re.split('\s+', s)])  # 将表达式按空格分割并重组
            if not s.startswith('('):  # 若用户输入的表达式首尾无括号，则统一格式化为：(表达式)
                s = str('(%s)' % s)
            while bracket.search(s):  # 若表达式s存在括号
                s = s.replace('--', '+')  # 检查表达式，并将--运算替换为+运算
                s_search = bracket.search(s).group()  # 将最内层括号及其内容赋给变量s_search
                if div.search(s_search):  # 若除法运算存在(必须放在乘法之前）
                    s = s.replace(s_search, Div(s_search))  # 执行除法运算并将结果替换原表达式
                elif mul.search(s_search):  # 若乘法运算存在
                    s = s.replace(s_search, Mul(s_search))  # 执行乘法运算并将结果替换原表达式
                elif sub.search(s_search):  # 若减法运算存在（必须放在加法之前）
                    s = s.replace(s_search, Sub(s_search))  # 执行减法运算并将结果替换原表达式
                elif add.search(s_search):  # 若加法运算存在
                    s = s.replace(s_search, Add(s_search))  # 执行加法运算并将结果替换原表达式
                elif c_f.search(s_search):  # 若括号内无任何运算（类似（-2.32）除外）
                    s = s.replace(s_search, strip.search(s_search).group())  # 将括号脱掉，例：（-2.32）---> -2.32

            print('The answer is: %.2f' % (float(s)))


if __name__ == '__main__':
    calc()
