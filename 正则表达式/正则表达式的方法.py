# -*- coding: utf-8 -*-
# @Time    : 2019/11/2 21:40
# @Author   : 高冷
# @FileName  : 正则表达式的符号.py

# re库常用的功能函数
"""
   函数                            说明
re.match()                   从字符串的起始位置匹配,匹配成功,返回一个匹配的对象,否则返回None
re.search()                  扫描整个字符串并返回第一个成功的匹配             (搜索)
re.findall()                 在字符串中找到正则表达式所匹配的所有子串,并返回一个列表,如果没有找到匹配的,则返回空列表
re.split()                   将一个字符串按照正则表达式进行分割,返回列表类型
re.finditer()                在字符串中找到正则表达式所匹配的所有字串,并把他们作为一个迭代器返回
re.sub()                     把字符串中所有匹配正则表达式的地方替换成新的字符串
"""
import re

# 1.   re.match()
'''
从字符串的起始位置匹配,匹配成功,返回一个匹配的对象，否则返回None

语法：re.match(pattern, string, flags=0)
 pattern：匹配的正则表达式
 string:要匹配的字符串
 flags:标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等;flags=0表示不进行特殊指定

'''

# 2.  re.search()
'''
扫描整个字符串并返回第一个成功的匹配对象，否则返回None

语法：re.search(pattern, string, flags=0)
示例：

>>> re.search(r'\d{2}','Ab123')
<_sre.SRE_Match object; span=(2, 4), match='12'>
>>> re.search(r'\d{2}','Abcde')
>>> print(re.search(r'\d{2}','Abcde'))
None
re.match与re.search的区别：
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配（注意：仅仅是第一个）
'''
first = re.search('ak', 'ak47')
print("1.", first)

# 3.  re.findall()
"""
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表

注意： match 和 search 是匹配一次,而findall 匹配所有

>>> re.findall(r'\d{2}','21c34d56e78')
['21', '34', '56', '78']
"""

# 4.4.  re.finditer()
"""
 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回.

 示例：

 复制代码
 >>> match = re.finditer(r'\d{2}','21c34d56e78')
 >>> for t in match:
    print(t.group())


 21
 34
 56
 78
 >>>
"""


# 5.  re.split()
"""
 根据正则表达式中的分隔符把字符分割为一个列表并返回成功匹配的列表.

 示例：

 >>> match = re.split(r'\.|-','hello-world.data')   # 使用 . 或 - 作为字符串的分隔符
 >>> print(match)
 ['hello', 'world', 'data']
 
 字符串也有split方法，如下，作个对比：
 
    字符串的split方法
    >>> 'a b   c'.split(' ')  # b和c之间有3个空格
    ['a', 'b', '', '', 'c']

    如果用空格不好理解的话，可以换位x
    >>> 'axbxxxc'.split('x')
    ['a', 'b', '', '', 'c']
    >>>
 """

# 6. re.sub()7
"""
用于替换字符串中的匹配项
    语法： re.sub(pattern, repl, string, count=0)
    pattern : 正则中的模式字符串。
    repl : 替换的字符串，也可为一个函数。
    string : 要被查找替换的原始字符串。
    count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
示例：
>>> match = re.sub(r'a', 'b','aaccaa')   # 把字符串中的a都替换为b
>>> print(match)
bbccbb
>>> 
"""