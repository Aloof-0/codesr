# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 21:37
# @Author   : 高冷
# @FileName  : json的dumps.py

"""
JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写。

函数         描述
json.dumps	将 Python 对象编码成 JSON 字符串
json.loads	将已编码的 JSON 字符串解码为 Python 对象

"""

# JSON转化
import json

# data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
#
# json = json.dumps(data)
# print(json)

# json 跨文本转化

dis = {'wenjie': 'huangjing', 'borang': 'baiying','borang1': 'baiying'}
aaa = json.dumps(dis)

f = open('json_text', 'w')
f.write(aaa)
f.close()

"""
import json
#dct="{'1':111}"#json 不认单引号
#dct=str({"1":111})#报错,因为生成的数据还是单引号:{'one': 1}

dct='{"1":"111"}'
print(json.loads(dct))

#conclusion:
#        无论数据是怎样创建的，只要满足json格式，就可以json.loads出来,不一定非要dumps的数据才能loads
"""
