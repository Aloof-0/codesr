# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/29 12:05
@Auth ： 高冷Aloof
@File ：string类型.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

"""
字符串类型是 Redis 中最为基础的数据存储类型，它在 Redis 中是二进制安全的，这便意味着该类型可以接受任何格式的数据，
如JPEG图像数据或Json对象描述信息等。在Redis中字符串类型的Value最多可以容纳的数据长度是512M。
"""

'''
增
    set mykey "test"   为键设置新值，并覆盖原有值
    getset mycounter 0   设置值,取值同时进行
    setex mykey 10 "hello"  设置指定 Key 的过期时间为10秒,在存活时间可以获取value
    setnx mykey "hello"   若该键不存在，则为键设置新值
    mset key3 "stephen" key4 "liu"  批量设置键

删
    del mykey  删除已有键


改
    append mykey "hello"  若该键并不存在,返回当前 Value 的长度
                  该键已经存在，返回追加后 Value的长度
    incr mykey   值增加1,若该key不存在,创建key,初始值设为0,增加后结果为1
    decrby  mykey  5   值减少5
    setrange mykey 20 dd   把第21和22个字节,替换为dd, 超过value长度,自动补0

查  
    exists mykey     判断该键是否存在，存在返回 1，否则返回0
    get mykey    获取Key对应的value
    strlen mykey  获取指定 Key 的字符长度
    ttl mykey     查看一下指定 Key 的剩余存活时间(秒数)
    getrange mykey 1 20  获取第2到第20个字节,若20超过value长度,则截取第2个和后面所有的的
    mget key3 key4   批量获取键'' 
'''