import threading
from queue import Queue
import requests
from lxml import etree
import time


class qiushi(object):
    def __init__(self):
        self.url = "https://www.qiushibaike.com/8hr/page/{}/"  # 获取url

        self.url_queue = Queue()   # 创建url队列
        self.html_queue = Queue()  # 创建html队列容器
        self.data_queue = Queue()  # 创建数据队列容器

    def url1(self):
        for i in range(2, 11):
            self.url_queue.put(self.url.format(i))  # 将url加入队列

    def html(self):
        while True:
            url = self.url_queue.get()  # 取一url队列
            self.url_queue.task_done()  # 结束一url队列
            response = requests.get(url=url)
            html_text = response.content.decode("utf-8")
            self.html_queue.put(html_text)
            # print(html_text)
            print("url", self.url_queue.unfinished_tasks)

    def data(self):
        while True:
            data = self.html_queue.get()  # 取一html队列容器
            self.html_queue.task_done()  # 结束一url队列
            html_text = etree.HTML(data)
            data_list = html_text.xpath(r"//a[@class='recmd-content']/text()")
            self.data_queue.put(data_list)
            print("html", self.html_queue.unfinished_tasks)

    def data_save(self):
        while True:
            print(self.data_queue.get())
            print("data", self.data_queue.unfinished_tasks)
            self.data_queue.task_done()

    def main(self):
        # 线程列表
        thread_list = []

        # 1.创建获取url的任务线程对象
        url_thread = threading.Thread(target=self.url1)
        thread_list.append(url_thread)

        # 2.创建获取html的任务线程对象
        html_thread = threading.Thread(target=self.html)
        thread_list.append(html_thread)

        # 3.创建获取数据的任务线程对象
        data_thread = threading.Thread(target=self.data)
        thread_list.append(data_thread)

        datasave_thread = threading.Thread(target=self.data_save)
        thread_list.append(datasave_thread)

        for thread in thread_list:
            thread.setDaemon(True)
            # 启动子线程
            thread.start()

        time.sleep(5)
        for queue in [self.url_queue, self.html_queue, self.data_queue]:
            queue.join()


spider = qiushi()
spider.main()
