"""
redis的事务和管道可以分离, 可以 不使用事务的情况下单独使用管道
管道可以实现 一次发送多条命令给redis服务器, 提高传输效率
"""
from redis import StrictRedis

redis_cli = StrictRedis(decode_responses=True)
# 创建管道对象  设置transaction参数为False, 则会创建非事务型管道(只开管道, 不开事务)
pipe = redis_cli.pipeline(transaction=False)
# pipe的后续操作会被管道中
a = pipe.set("loveU", 1234)
b = pipe.set("COCO", 12345)
# 执行管道  会让管道将命令打包发给redis服务器
c = pipe.execute()

print(a)
print(b)
print(c)
