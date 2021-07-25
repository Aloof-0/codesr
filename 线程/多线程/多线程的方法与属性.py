# -*- coding: utf-8 -*-
# @Time    : 2020/2/5, 11:10 
# @Author   : 高冷
# @FileName  : PyCharm

"""
1. 构造方法
    process         : [group,[,target[,name]]]
    group           : 线程组,目前还没实现,库引用必须是None
    target          : 要执行的方法
    name            ：进程名
    args/kwargs     ：要传入方法的参数
2. 实例方法
    is-alive()      : 返回进程是否在运行
    join([timeout]) ：阻塞当前上下环境进程程,直到调用此方法的进程结束或timeout
    start()         : 进程就绪等待cpu调度
    run()           : start()调用润方法,如果实例进程未制定传入target,这start默认执行run方法
    terminate       : 不管任务是否完成，立刻停止工作进程
"""






