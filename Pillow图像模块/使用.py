# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/27 23:28
@Auth ： 高冷Aloof
@File ：使用.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""



from PIL import Image

file_path = 'C:/Users/admin/Pictures/scence/1.jpg'   # 获取文件地址 网络图片也是可以

img = Image.open(file_path)
imgSize = img.size  # 大小/尺寸
w = img.width  # 图片的宽
h = img.height  # 图片的高
f = img.format  # 图像格式
print(imgSize)
print(w, h, f)
"""
打印：
(534, 300)
534 300 JPEG
"""
