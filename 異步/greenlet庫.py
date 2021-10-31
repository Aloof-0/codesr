from greenlet import greenlet


def fun1():
    print(1)  # 第 1
    gr2.switch()
    print(2)  # 第三
    gr2.switch()


def fun2():
    print(3)  # 第二
    gr1.switch()
    print(4)  # 第四


gr1 = greenlet(fun1)
gr2 = greenlet(fun2)

gr1.switch()  # 第一步： 去執行func1
