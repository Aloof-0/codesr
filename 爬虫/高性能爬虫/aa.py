import time
import requests
from lxml import etree
from queue import Queue
from threading import Thread


class QiuShiSpider(object):
    """糗事百科多线程爬虫"""

    def __init__(self):
        # 构建基础的url地址
        # "http://www.qiushibaike.com/8hr/page/{}/".format("2")
        self.base_url = " http://www.qiushibaike.com/8hr/page/{}/"

        # 构建请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        }

        # 创建url队列容器
        self.url_queue = Queue()

        # 创建html队列容器
        self.html_queue = Queue()

        # 创建数据队列容器
        self.data_queue = Queue()

    # 1.构建url地址
    def get_urls(self):
        """
        :return: 目标url列表
        """
        # 一共13页
        for i in range(1, 14):
            # 拼接翻页的url地址
            url = self.base_url.format(i)
            # 将url地址装入队列
            self.url_queue.put(url)

    # 2.发送请求获取数据
    def get_html(self):

        # 循环的取出url，发送请求，直到任务全部完成
        # 完成标志：Thread().unfinished_task 值为0
        while True:
            # 1.从队列中取出url地址
            url = self.url_queue.get()
            print(url)

            # 2.发送请求获取html页面数据--网络延迟
            response = requests.get(url=url, headers=self.headers)
            html = response.content.decode()

            # 3.将数据存入html队列容器中
            self.html_queue.put(html)

            # 4.通知url队列任务完成
            # 任务数量-1
            self.url_queue.task_done()

    # 3.从响应中提取数据
    def get_content(self):

        while True:
            # 1.从html队列中取出html数据
            html = self.html_queue.get()
            # 2.创建etree对象
            eroot = etree.HTML(html)
            # 3.使用xpath规则提取数据
            title_list = eroot.xpath("//a[@class='recmd-content']/text()")
            # 4.将数据装入数据队列容器
            self.data_queue.put(title_list)
            # 5.通知html队列任务完成
            # 任务数量-1
            self.html_queue.task_done()

    # 4.保存数据
    def save_data(self):
        while True:
            # 1.从数据队列中取出数据
            data = self.data_queue.get()
            # 2.保存数据
            print(data)
            # 3.通知数据队列任务完成
            self.data_queue.task_done()

    # 5.运行多线程爬虫
    def run(self):

        # 线程列表
        thread_list = []

        # 1.创建获取url的任务线程对象
        url_thread = Thread(target=self.get_urls)
        thread_list.append(url_thread)

        # 2.创建获取html的任务线程对象
        html_thread = Thread(target=self.get_html)
        thread_list.append(html_thread)

        # 3.创建获取数据的任务线程对象
        data_thread = Thread(target=self.get_content)
        thread_list.append(data_thread)

        # 4.创建保存数据的任务线程对象
        save_thread = Thread(target=self.save_data)
        thread_list.append(save_thread)

        # 5.分别将线程对象添加到列表中,方便遍历执行任务
        for thread in thread_list:
            # 以守护线程的方式执行
            # 特点：主线程结束，子线程也会结束
            thread.setDaemon(True)
            # 启动子线程
            thread.start()

        # 保证子线程一定能执行
        time.sleep(2)

        # 同时让队列中所有任务执行完毕后才结束程序
        for queue in [self.url_queue, self.html_queue, self.data_queue]:
            # 如果unfinished_task不为0的时，处于队列就等待状态，等待任务执行，
            # 而每个任务函数中里面都有task_done方法[任务数量-1]，任务数量为0时，程序继续执行
            queue.join()


if __name__ == '__main__':
    spider = QiuShiSpider()
    spider.run()