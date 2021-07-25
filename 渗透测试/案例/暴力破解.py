import itertools

tsPassWord = "13@dcN"  # 设置的测试密码
MaxLenPassword = 10  # 最大密码长度
wordList = "0123abcd@!MN"  # 密码字符集合

for lenPassword in range(1, MaxLenPassword + 1):
    passWd = itertools.product(wordList, repeat=lenPassword)  # 调用迭代函数 自匹配
    for i in passWd:
        str = ''.join(i)
        if str == tsPassWord:
            print("密码设置为", str)
            break
