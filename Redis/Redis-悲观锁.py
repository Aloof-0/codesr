"""
SETNX命令
    键不存在才会设置成功
    多个客户端抢夺, 只有一个可以设置成功(获取锁, 获取操作数据的权限)
SETNX lock1  1   # 键不存在,才会设置成功
$ 1
SETNX lock1  1   # 键存在, 无法设置, 返回0
$ 0
"""
from redis import StrictRedis

# 1.创建redis客户端对象
redis_cli = StrictRedis(decode_responses=True)

# 2.创建锁的key
order_lock = 'lock:goods'

# 3.开启循环
while True:
    # 4.抢夺redis悲观锁  //抢到资源返回True, 未抢到处于等待状态
    lock = redis_cli.setnx(order_lock, 11)

    if lock:
        # 给悲观锁设置过期时间，防止移除锁儿导致死锁
        redis_cli.expire(order_lock, 5)
        # 5.查询库存
        count = redis_cli.get(order_lock)
        if int(count) > 0:
            # 6.减库存，下单成功
            redis_cli.decr(order_lock)
            print("下单成功")
        else:
            # 7.库存不足,商品已经售完
            print("商品已售完")

    # 8.移除悲观锁
    redis_cli.delete(order_lock)
    break
