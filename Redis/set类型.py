# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/29 15:26
@Auth ： 高冷Aloof
@File ：set类型.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

"""
⽆序集合
元素为string类型
元素具有唯⼀性，不重复
说明：对于集合没有修改操作
Set类型看作为没有排序的字符集合。Set可包含的最大元素数量是4294967295。
如果多次添加相同元素，Set中将仅保留该元素的一份拷贝。
"""

'''
增
    sadd myset a b c  若key不存在,创建该键及与其关联的set,依次插入a ,b,若key存在,则插入value中,若a 在myset中已经存在,则插入了 d 和 e 两个新成员。  

删
    spop myset  尾部的b被移出,事实上b并不是之前插入的第一个或最后一个成员
    srem myset a d f  若f不存在, 移出 a、d ,并返回2
    
    改
    smove myset myset2 a    将a从 myset 移到 myset2，

查
    sismember myset a    判断 a 是否已经存在，返回值为 1 表示存在。
    
    smembers myset    查看set中的内容
    
    scard myset    获取Set 集合中元素的数量
    
    srandmember myset   随机的返回某一成员
    
    sdiff myset1 myset2 myset3  1和2得到一个结果,拿这个集合和3比较,获得每个独有的值
    
    sdiffstore diffkey myset myset2 myset3  3个集和比较,获取独有的元素,并存入diffkey 关联的Set中
    
    sinter myset myset2 myset3   获得3个集合中都有的元素
    
    sinterstore interkey myset myset2 myset3   把交集存入interkey 关联的Set中
    
    sunion myset myset2 myset3   获取3个集合中的成员的并集
    
    sunionstore unionkey myset myset2 myset3  把并集存入unionkey 关联的Set中
'''