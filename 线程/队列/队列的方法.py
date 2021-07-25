# 创建队列 FIFO模式 先进先出
from queue import Queue
"""
    1. 创建队列的时候可以设置春芳的最大数量
    2. put的时候超过最大数量也会阻塞住,等下其他线程get走数据
"""
q = Queue(maxsize=100)


# 1. 存数据  -- put
q.put("hello world")
q.put("save world")

# 2. 取数据  -- get
"""
    1. 队列不如列表灵活,队列只有get和put,存从最左边存,取从最右边取,先进先出. 
    2. 是线程安全决定的
    3. 队列里有2个值,如果3个get城西不会结束阻塞住等待其他线程put数据
"""
print(q.get())
print(q.get())

# 3. 阻塞队列&&完成队列
"""
    1. join阻塞进程,直到所有任务完成,需要配合task_done方法
    2. task_done方法表示任务完成,每一条get语句后需要加一条
"""
q.put("free")
q.task_done()  # 表示任务完成
