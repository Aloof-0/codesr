# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/29 14:49
@Auth ： 高冷Aloof
@File ：Hashes类型.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

"""

 我们可以将Redis中的Hashes类型看成具有String Key和String Value的map容器。

 所以该类型非常适合于存储值对象的信息。如Username、Password和Age等。如果Hash中包含很少的字段，那么该类型的数据也将仅占用很少的磁盘空间。

 每一个Hash可以存储4294967295个键值对
 r.hset(name="1", key="1", value="1")
 key: (13:2)(2:2)
"""

'''
Map类型:
    hset myhash field1 "s"  

    django-redis.key=myhash   django-redis.value=( map.key=field1   map.value=s )   

增
    redis_conn.hincrby('carts_%s' % user.id, sku_id, count)  存在则累加 不存在则新增
     
    hset myhash field1 "s"    若字段field1不存在,创建该键及与其关联的Hashes, Hashes中,key为field1 ,并设value为s ，若字段field1存在,则无效
                       
    hsetnx myhash field1 s    若字段field1不存在,创建该键及与其关联的Hashes, Hashes中,key为field1 ,并设value为s， 若字段field1存在,则无效
    
    hmset myhash field1 "hello" field2 "world   一次性设置多个字段

删
    del mykey  删除已有键 
    
    lrem mykey 2 a   从头部开始找,按先后顺序,值为a的元素,删除数量为2个,若存在第3个,则不删除
    
    ltrim mykey 0 2  从头开始,索引为0,1,2的3个元素,其余全部删除

改
    lset mykey 1 e   从头开始, 将索引为1的元素值,设置为新值 e,若索引越界,则返回错误信息
    
    rpoplpush mykey mykey  将 mykey 中的尾部元素移到其头部

查
    HGETALL key           返回 key 指定的哈希集中所有的字段和值
    lrange mykey 0 -1   取链表中的全部元素，其中0表示第一个元素,-1表示最后一个元素。
    
    lrange mykey 0 2    从头开始,取索引为0,1,2的元素
    
    lrange mykey 0 0    从头开始,取第一个元素,从第0个开始,到第0个结束
    
    lpop mykey          获取头部元素,并且弹出头部元素,出栈
    
    lindex mykey 6      从头开始,获取索引为6的元素 若下标越界,则返回nil 
'''
