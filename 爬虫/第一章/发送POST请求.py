# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 13:58
# @Author  : Frosty 
# @Email   : 935722505@qq.com
# @File    : 发送POST请求.py
# @Time : 2020/7/20 13:58
# @Software: PyCharm



# 表单形式
import requests
headers  = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36", "host":"www.santostang.com"}
link = "http://www.santostang.com/"
r = requests.post(link ,headers = headers)
print(r.text)
