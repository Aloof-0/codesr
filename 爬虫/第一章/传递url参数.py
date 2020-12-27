# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 13:35
# @Author  : Frosty 
# @Email   : 935722505@qq.com
# @File    : 传递url参数.py
# @Time : 2020/7/20 13:35
# @Software: PyCharm



import requests

kley_dict = {"key1":"value1", "key2":"value2"}
headers = {'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',  'Host': 'www.bilibili.com'}
link = "http://www.bilibili.com"
r = requests.get(link, headers=headers)
print(r.text)
print(r.url)

PA = open("text","r+", encoding="utf8")
PA.write(r.text)
PA.close()

