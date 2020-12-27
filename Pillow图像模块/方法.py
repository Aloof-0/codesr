# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/27 23:31
@Auth ： 高冷Aloof
@File ：方法.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from PIL import Image
im = Image.open("1.png")
im.show()


# format属性定义了图像的格式，如果图像不是从文件打开的，那么该属性值为None；size属性是一个tuple，
# 表示图像的宽和高（单位为像素）；mode属性为表示图像的模式，常用的模式为：L为灰度图，RGB为真彩色，CMYK为pre-press图像。如果文件不能打开，则抛出IOError异常。
print(im.format, im.size, im.mode)

# save保存
im.save("c:\\")

# convert
# convert() 是图像实例对象的一个方法，接受一个 mode 参数，用以指定一种色彩模式，mode 的取值可以是如下几种：
"""
· 1 (1-bit pixels, black and white, stored with one pixel per byte) 
· L (8-bit pixels, black and white) 
· P (8-bit pixels, mapped to any other mode using a colour palette) 
· RGB (3x8-bit pixels, true colour) 
· RGBA (4x8-bit pixels, true colour with transparency mask) 
· CMYK (4x8-bit pixels, colour separation) 
· YCbCr (3x8-bit pixels, colour video format) 
· I (32-bit signed integer pixels) 
· F (32-bit floating point pixels)
"""
im = Image.open('1.png').convert('L')

# Filter
from PIL import Image, ImageFilter
im = Image.open('1.png')
# 高斯模糊
im.filter(ImageFilter.GaussianBlur)
# 普通模糊
im.filter(ImageFilter.BLUR)
# 边缘增强
im.filter(ImageFilter.EDGE_ENHANCE)
# 找到边缘
im.filter(ImageFilter.FIND_EDGES)
# 浮雕
im.filter(ImageFilter.EMBOSS)
# 轮廓
im.filter(ImageFilter.CONTOUR)
# 锐化
im.filter(ImageFilter.SHARPEN)
# 平滑
im.filter(ImageFilter.SMOOTH)
# 细节
im.filter(ImageFilter.DETAIL)