"""
基本语法
    ·watch  redis实现的乐观锁
机制
    事务开启前,这种对数据的监听,EXEC时,如果发现数据发生过修改,事务会自动取消(DISCARD)
    事务EXEC后,无论成败,监听会被移除
"""
from redis import StrictRedis, WatchError
# 1.创建客户端对象
redis_cli = StrictRedis(decode_responses=True)
# 2.创建管道对象
print(redis_cli.get("reserve_count"))
# redis_cli.set("reserve_count", 10)
pipe = redis_cli.pipeline()

while True:
    try:
        # 3.监听数据,如果开启监听,则不会开启默认的事务,后续的pipe操作会立即执行
        pipe.watch("reserve_count")
        count = pipe.get("reserve_count")

        if int(count) > 0:  # 有库存.库存减一
            # 手动开启事务
            pipe.multi()
            # 库存减一
            pipe.decr("reserve_count")

            # 提交事务
            pipe.execute()
            print("下单成功")
        else:  # 无库存
            print("商品已售完")
            # 将监听移除
            pipe.reset()
        break

    except WatchError:  # 捕获到该异常, 说明监听的数据被其他客户端修改, 此时应该重试/取消操作
        print('数据被修改, 重试')
        continue

