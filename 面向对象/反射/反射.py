# -*- coding: utf-8 -*-
# @Time    : 2019/12/8 23:31
# @Author   : 高冷
# @FileName  : 反射.py
# @web       : https://www.jb51.net/article/168473.htm , https://www.cnblogs.com/dong-/p/9398465.html
"""
1. getatter() 这个方法是根据字符串去某个模块中寻找方法
2. hasatter() 这个方法是根据字符串去判断某个模块中该方法是否存在
3. setatter() 这个方法是根据字符串去某个模块中设置方法
4. delatter() 这个方法是根据字符串去某个模块中删除方法

反射中适用于类和对象的方法:
                             1. getattr
                             2. setattr
                             3. hasattr
                             4. delattr
反射情景:
          1. 类名反射 : 静态属性  类属性  静态方法
　　　　  2. 对象反射: 对象属性  对象方法
          3. 模块: 模块中的方法
          4. 自己的模块中

反射的参数:
            1. getattr : (命名空间 , ' 变量名 ')
            2. setattr : (命名空间 , ' 变量名 ' , 新值)
　　　　    3. hasattr : (命名空间 , ' 变量名 ')
　　　　    4. delattr : (命名空间 , ' 变量名 ')
"""

class Foo:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def show(self):
        return "%s-%s-%s"%(self.name, self.age, self.sex)
obj = Foo("love", "1my", "None")



# 1. getatter() 这个方法是根据字符串去某个模块中寻找方法

aaa = getattr(obj, 'show')  # 使用getattr函数去寻找字符串的同名方法
print(aaa())

# 2.hasatter()  这个方法是根据字符串去判断某个模块中该方法是否存在

bbb = hasattr(obj, 'show')
print(bbb)

# 3. setatter() 这个方法是根据字符串去某个模块中设置方法

ccc = setattr(obj, "status", "alone")
print(ccc)
print(hasattr(obj, "status"))

# 4. delatter() 这个方法是根据字符串去某个模块中删除方法

delattr(obj, "status")

