# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/29 15:28
@Auth ： 高冷Aloof
@File ：zset类型.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

"""
sorted set，有序集合
元素为string类型
元素具有唯⼀性，不重复
每个元素都会关联⼀个double类型的score，表示权重，通过权重将元素从⼩到⼤排序
说明：没有修改操作
"""
'''
增
    zadd myzset 2 "two" 3 "three"   添加两个分数分别是 2 和 3 的两个成员

删
    zrem myzset one two  删除多个成员变量,返回删除的数量

改
    zincrby myzset 2 one  将成员 one 的分数增加 2，并返回该成员更新后的分数

查 
    zrange myzset 0 -1 WITHSCORES  返回所有成员和分数,不加WITHSCORES,只返回成员
    
    zrank myzset one   获取成员one在Sorted-Set中的位置索引值。0表示第一个位置
    
    zcard myzset    获取 myzset 键中成员的数量
    
    zcount myzset 1 2   获取分数满足表达式 1 <= score <= 2 的成员的数量
    
    zscore myzset three  获取成员 three 的分数
    
    zrangebyscore myzset (1 2   获取分数满足表达式 1 < score <= 2 的成员
'''