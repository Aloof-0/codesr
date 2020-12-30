# Python交互 {#python交互}

* 安装包如下

  > pip install redis-py-cluster

* redis-py-cluster源码地址[https://github.com/Grokzen/redis-py-cluster](https://github.com/Grokzen/redis-py-cluster)

* 创建⽂件redis\_cluster.py，示例码如下

```python
from rediscluster import *
if __name__ == '__main__':
  try:
    # 构建所有的节点，Redis会使⽤CRC16算法，将键和值写到某个节点上
    startup_nodes = [
        {'host': '192.168.26.128', 'port': '7000'},
        {'host': '192.168.26.130', 'port': '7003'},
        {'host': '192.168.26.128', 'port': '7001'},
    ]
    # 构建StrictRedisCluster对象
    src=StrictRedisCluster(startup_nodes=startup_nodes,decode_responses=True)
    # 设置键为name、值为itheima的数据
    result=src.set('name','itheima')
    print(result)
    # 获取键为name
    name = src.get('name')
    print(name)
  except Exception as e:
    print(e)
```



