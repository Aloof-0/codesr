# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 15:48
# @Author   : 高冷
# @FileName  : 反射2.py


# 还可以对文件的程序进行处理
import Non

# 在类取值
abc = getattr(Non, "Foo")
aaa = abc()
aaa.koko()

# 在文件上取变量

cde = getattr(Non, "abc")
print(cde)

# 在文件上取函数

more = getattr(Non, "obj")
more()

# 假如查找多个文件

imp = input(">>>")
if hasattr(Non, imp):
    abdf = getattr(Non, imp)
    abdf()
else:
    print("error")
