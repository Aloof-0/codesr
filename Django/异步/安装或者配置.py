# 介绍
"""
思考：

    消费者取到消息之后，要消费掉（执行任务），需要我们去实现。

    任务可能出现高并发的情况，需要补充多任务的方式执行。

    耗时任务很多种，每种耗时任务编写的生产者和消费者代码有重复。

    取到的消息什么时候执行，以什么样的方式执行。

结论：

    实际开发中，我们可以借助成熟的工具 Celery 来完成。

    有了 Celery，我们在使用生产者消费者模式时，只需要关注任务本身，极大的简化了程序员的开发流程.

介绍

    celery 是一个简单、灵活且可靠、处理大量消息的分布式系统，可以在一台或者多台机器上运行.

    特点:

    单个 Celery 进程每分钟可处理数以百万计的任务.

    通过消息进行通信，使用消息队列（ 中间人或broker ）在生产者和消费者之间进行协调。
"""

# (1.注意celery 不能传字节类型 如文件
# (2.适合耗时操作和高并发
# 3.  连接redis 调用函数  return(不管有没数据)生成会24小时的数据

# 1.pip安装
pip install Celery # 最好是linux 说网上window 可能有问题但上手应该没有问题

# 2.创建实例并且配置
增加一个python的包 :Celery_new

# 3.创建main.py文件 //启动文件

# 4.写入main.py文件(具体看main.py)

# 5.创建config.py文件  // 配置文件

# 6.写入config.py文件(具体看config.py)

# 7.定义任务 创建sms包(随便名称)

# 8.创建tasks.py(名称必须一致)

# 9.写入tasks.py

# 10.需要使用的文件添加celery 例如view.py
"""
class number(APIView):
        def get(selfself, request):
                ...
                code.delay(mobile)
                
"""

# 11.启动服务
# celery -A celery_button.main worker -l info -P eventlet -c 1000 -E
# 需要安装eventlet
# celery -Acelery_button.main worker -l info -P gevent
# 需要安装gevent