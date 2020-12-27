# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 22:15
# @Author   : 高冷
# @FileName  : json的loads.py

import json

# json.loads	将已编码的 JSON 字符串解码为 Python 对象

# jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
#
# text = json.loads(jsonData)
# print(text)


# json.loads  跨文本解码


f = open('json_text', 'r')
aaa = f.read()
bbb = json.loads(aaa)
print(bbb)
f.close()