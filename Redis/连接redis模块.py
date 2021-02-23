from redis import StrictRedis
# 1. 创建redis客户端对象
# decode_responses=True 将返回的bytes转换成字符串
redis_cli = StrictRedis(decode_responses=True)
# 2.储存数据-redis以二进制的方式存储数据
redis_cli.set("kobe", "12", ex=36000)
# 3.取数据-redis默认获取的数据的bytes类型
print(redis_cli.get("kobe"))

# 4.创建管道对象  默认会开启事务
pipeline = redis_cli.pipeline()

# 5.使用管道对象-增删改查 [所以命令放入同一事务，不会打断]
a = pipeline.set("name", "love")
b = pipeline.get("name")
# 6.提交事务
c = pipeline.execute()

print(a)
print(b)
print(c)
