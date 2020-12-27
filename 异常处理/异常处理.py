# -*- coding: utf-8 -*-
# @Time    : 2019/12/8 18:10
# @Author   : 高冷
# @FileName  : 异常处理.py
# @web       : https://www.cnblogs.com/wupeiqi/p/5017742.html

"""
1. 概念：错误是无法通过其他代码进行处理问题，如语法错误和逻辑错误，语法错误是单词或格式等写错，只能根据系统提示去修改相应的代码，
逻辑错误是代码实现功能的逻辑有问题，系统不会报错，也是只能找到相应的代码进行修改；异常是程序执行过程中，出现的未知问题，这里语法和逻辑都是正确的，
可以通过其他代码进行处理修复，如可以通过if判定语句来避免对年龄进行赋值时输入了字符而出现异常的情况，如使用捕捉异常可以避免除零异常等


2. 基本构造
    try:
        pass  代码块;逻辑
    except Exception as e:                                      //  Exception可以处理任何一种异常情况
        pass  # 上述代码块如果出错, 自动执行当前块内容
              # e是Exception的对象,对象封装了错误信息

3. python中的异常种类非常多，每个异常专门用于处理某一项异常！！！

4.
                (1). try: 对于特殊处理或提醒的异常需要先定义，最后定义Exception来确保程序正常运行。
                (2). else:在没有检测出异常情况时, 执行else语句.
                (3). finally：无论是否出现异常情况,都会执行finally语句
                (4). raise: 主动触发异常
                (5). assert: 断言 用于判断一个表达式，在表达式条件为 false 的时候触发异常。
5.  一但有错误 try不再执行
"""

# 1. try: 对于特殊处理或提醒的异常需要先定义，最后定义Exception来确保程序正常运行。     //  可以单独定义异常处理  主要用于日志文件
s1 = 'hello'
try:
    int(s1)
except KeyError as e:
    print('键错误')
except IndexError as e:
    print('索引错误')
except Exception as e:
    print('# 1. 错误')

# 2. else:在没有检测出异常情况时, 执行else语句.

s1 = 1223
try:
    int(s1)
except KeyError as e:
    print('键错误')
except IndexError as e:
    print('索引错误')
except Exception as e:
    print('错误')
else:
    print("# 2. You're right")

# 3. finally：无论是否出现异常情况,都会执行finally语句
s1 = 1223
try:
    int(s1)
except KeyError as e:
    print('键错误')
except IndexError as e:
    print('索引错误')
except Exception as e:
    print('错误')
else:
    pass
finally:
    print("# 3. finally the end")

# 4. raise: 主动触发异常 ,错误对象必须有一个名字，且它们应是Error或Exception类的子类。

try:
    raise Exception("# 4. raise error")
except KeyError as e:
    print('键错误')
except IndexError as e:
    print('索引错误')
except Exception as e:
    print(e)

# 5. assert: 断言 用于判断一个表达式，在表达式条件为 false 的时候触发异常。   语法格式如下：assert expression

print("# 5. assert")
assert 1 == 1   # 假如为真 则可以继续执行程序
print("# 5. fine")

assert 1 == 2   # 假如为假 直接报错
print("ok")
