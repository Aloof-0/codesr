# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 12:14
# @Author  : Frosty 
# @Email   : 935722505@qq.com
# @File    : 超时.py
# @Time : 2020/7/21 12:14
# @Software: PyCharm

import requests
link = "http://www.santostang.com/"
re =requests.get(link ,timeout = 0.001)

# 异常值为超过0.001还没链接成功就出错