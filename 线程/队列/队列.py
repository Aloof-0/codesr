# 导包
from queue import Queue

# 创建队列对象
q = Queue(maxsize=100)  # maxsize=100 创建最大的队列数  先进先出

list_1 = {"love": "kk"}
list_2 = ["jk", "no"]

q.put(list_1)  # 把数据放入到队列中,就进行等发知道队列不满把数据添加到队列中
q.put(list_2)
q.put_nowait(list_1)  # 把数据放入到队列中,如果队列数据已满,就不进行等待,引发异常

print(q.get())  # 把数据从队列中取出,如果队列为空,就进行等待直到队列不为空,返回数据
print(q.get_nowait())  # 把数据从队列中取出,如果对垒为空,就不进行等待,引发异常

print(q.qsize())  # 获取队列中的元素个数
print(q.task_done())  # 让未完成的任务数unfinished_tasks属性 -1
print(q.unfinished_tasks)  # 获取未完成的任务数 用task_done会-1

q.join()  # 让当前进程进行等待状态,直到队列的 unfinished_tasks 属性为0时继续进行

"""
注意:
    1. 当调用put或put_nowait方法是q.qsize会+1,并且q.unfinished_tasks也会+1
    2. 当调用get或get_nowait方法时q.qsize 会-1 ,但是unfinished_tasks不会变化
    3. 当调用task_done方法时unfinished_tasks会-1
"""
