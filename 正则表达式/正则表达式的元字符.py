# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 21:40
# @Author   : 高冷
# @FileName  : 正则表达式的元字符.py

import re

# 1.    .匹配任意字符,除了换行符(/n)

yidian = re.findall('.', 'iakjsdykuashklldksa24564364152')
print("1.", yidian)

# 2.    ?匹配一个任意字符,范围[0,1]                                  // i?a 意思是i是0或1次都可以匹配 ,即a一定要有,i是0或1都可以匹配

wenhao = re.findall('i?a', 'iakjsdykuashklldksiiia5745645212')
print("2.", wenhao)

# 3.    ^匹配字符串的开头                                            //^输入字行首,且输出行首即^iak则['iak'] ;^iakjsd则[iakjsd];但^dakjgdk则出错

jiantou = re.findall('^iak', 'iakjsdykuashklldksiiia5745645212')
print("3.", jiantou)

# 4.    $匹配字符串的结尾

daole = re.findall('45212$', 'iakjsdykuashklldksiiia5745645212')
print("4.", daole)

# 5.    *匹配前面的子表达式任意次;即重复匹配[0,正无穷]                //例如，zo*能匹配“z”，也能匹配“zo”以及“zoo”。*等价于o{0,}

xingxing = re.findall('ak*', 'iakjsdykuashklldksiiia5745645212')
print("5.", xingxing)

# 6.    +匹配前面的子表达式任意次;即重复匹配[1,正无穷]               //例如，“zo+”能匹配“zo”以及“zoo”，但不能匹配“z”。+等价于{1,}。

jiahao = re.findall('ak+', 'iakjsdykuashklldksiiiakk5745645212')
print("6.", jiahao)

# 7.    {n}匹配n是一个非负整数。匹配确定的n次
"""
{n}                        n是一个非负整数。匹配确定的n次。例如，“o{2}”不能匹配“Bob”中的“o”，但是能匹配“food”中的
{n,}                       n是一个非负整数。至少匹配n次。例如，“o{2,}”不能匹配“Bob”中的“o”，但能匹配“foooood”中的所有o。“o{1,}”等价于“o+”。“o{0,}”则等价于“o*”。
{n,m}                      m和n均为非负整数，其中n<=m。最少匹配n次且最多匹配m次。例如，“o{1,3}”将匹配“fooooood”中的前三个o为一组，后三个o为一组。“o{0,1}”等价于“o?”。请注意在逗号和两个数之间不能有空格。
"""

dakuohao = re.findall('a{2,3}k', 'aaaaaaaaakaaaak')
print("7.", dakuohao)

# 8.    [xyz]字符集合。匹配所包含的任意一个字符              例如， '[abc]' 可以匹配 "plain" 中的 'a'。即匹配a,b,c都可以,但是只是匹配其中一个元素(分开)
#       [^xyz]负值字符集合。匹配未包含的任意字符。           例如，“[^abc]”可以匹配“plain”中的“plin”。

kuangkuang = re.findall('[abc]', 'pianb')
print("8.", kuangkuang )

kuangkuang = re.findall('[^abc]', 'pianb')
print("8.", kuangkuang )

# 9.    [a-z]字符范围，匹配指定范围内的任意字符。            例如，“[a-z]”可以匹配“a”到“z”范围内的任意小写字母字符。[0-9]则全部数字

kuangli = re.findall('[a-z]','kjahkdsk')
print("9.", kuangli)


