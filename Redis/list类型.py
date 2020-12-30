# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/29 15:23
@Auth ： 高冷Aloof
@File ：list类型.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
"""
    列表的元素类型为string
    按照插⼊顺序排序
    List类型是按照插入顺序排序的字符串链表。和数据结构中的普通链表一样，我们可以在其头部(left)和尾部(right)添加新的元素。
    在插入时，如果该键并不存在，Redis将为该键创建一个新的链表。与此相反，如果链表中所有的元素均被移除，那么该键也将会被从数据库中删除。
    List中可以包含的最大元素数量是4294967295。
"""

'''
List类型:(链表:最后一个插入的元素,位置索引为o)

增 
    redis_conn.sadd('selected_%s'%user.id, sku_id)  Sadd 命令将一个或多个成员元素加入到集合中，已经存在于集合的成员元素将被忽略。
    
    lpush mykey a b  若key不存在,创建该键及与其关联的List,依次插入a ,b， 若List类型的key存在,则插入value中
    
    lpushx mykey2 e  若key不存在,此命令无效， 若key存在,则插入value中
    
    linsert mykey before a a1  在 a 的前面插入新元素 a1
    
    linsert mykey after e e2    在e 的后面插入新元素 e2
    
    rpush mykey a b 在链表尾部先插入b,在插入a
    
    rpushx mykey e  若key存在,在尾部插入e, 若key不存在,则无效
     
    rpoplpush mykey mykey2   将mykey的尾部元素弹出,再插入到mykey2 的头部(原子性的操作)

删
    redis_conn.srem('selected_%s' % user.id, sku_id)   列表对象 key 中移除一个或多个 member 元素，不存在的 member 元素会被忽略。当 key 不是集合类型，返回一个错误。
     
    del mykey  删除已有键 
    
    lrem mykey 2 a   从头部开始找,按先后顺序,值为a的元素,删除数量为2个,若存在第3个,则不删除
    
    ltrim mykey 0 2  从头开始,索引为0,1,2的3个元素,其余全部删除

改
    lset mykey 1 e   从头开始, 将索引为1的元素值,设置为新值 e,若索引越界,则返回错误信息
    
    rpoplpush mykey mykey  将 mykey 中的尾部元素移到其头部

查
    SMEMBERS key         Redis Smembers 命令返回集合中的所有的成员。 不存在的集合 key 被视为空集合。
    lrange mykey 0 -1   取链表中的全部元素，其中0表示第一个元素,-1表示最后一个元素。
    
    lrange mykey 0 2    从头开始,取索引为0,1,2的元素
    
    lrange mykey 0 0    从头开始,取第一个元素,从第0个开始,到第0个结束
    
    lpop mykey          获取头部元素,并且弹出头部元素,出栈
    
    lindex mykey 6      从头开始,获取索引为6的元素 若下标越界,则返回nil 
'''