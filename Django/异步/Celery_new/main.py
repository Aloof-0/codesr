
# 从您刚刚下载的包导入Celery类
from celery import Celery
# 利用导入的创建Celery对象
celery_app = Celery("casually") # 名字随便

# 配置
celery_app.config_from_object("celery_new.config")

# 自动捕获任务
celery_app.autodiscover_tasks(['Celery_new.sms'])