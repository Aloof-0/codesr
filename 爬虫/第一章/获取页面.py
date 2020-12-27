# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 13:02
# @Author  : Frosty 
# @Email   : 935722505@qq.com
# @File    : 获取页面.py
# @Time : 2020/7/19 13:02
# @Software: PyCharm

import requests

a = "http://ntlias-stu.boxuegu.com/#/login" #定义link为目标网易地址
r = requests.get(a)
r.raise_for_status()
r.encoding = r.apparent_encoding
print(r.text)
print("文本编码：",r.encoding)