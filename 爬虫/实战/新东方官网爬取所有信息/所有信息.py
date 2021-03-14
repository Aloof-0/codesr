import requests
from queue import Queue
from lxml import etree
from threading import Thread
import time
import re


class new_east(object):

    def __init__(self):
        self.url = r"http://souke.xdf.cn/MiddleSchool-8.html?applystate=0&attr=57&hide=0&page={}"  # 伪url
        self.headers = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 FS"
                        }
        self.proxies = {
        "https": "https://106.14.198.6:8080",
        }
        self.proxy = ""
        self.url_query = Queue()  # 创建url队列
        self.html_query = Queue()  # 创建html队列
        self.data_query_title = Queue()  # 创建数据队列
        self.data_query_url = Queue()  # 创建数据队列
        self.data_query_time = Queue()  # 创建数据队列
        self.data_query_place = Queue()  # 创建数据队列

    def url_list(self):  # 循环创建url
        for i in range(1, 52):
            self.url_query.put(self.url.format(i))

    def html_list(self):
        while True:
            url = self.url_query.get()  # 单一url
            self.url_query.task_done()
            response = requests.get(url=url, headers=self.headers, proxies=self.proxies)
            self.html_query.put(response.content.decode("UTF-8"))  # 加入html_list队列

    def data_list(self):
        while True:
            html = self.html_query.get()  # 先进先出取出数据
            self.html_query.task_done()
            eroot = etree.HTML(html)
            data_title = eroot.xpath(r'''//div[@class="m-classlist-l"]/h3/a/text()''')  # 获取标题文本
            data_url = eroot.xpath(r'''//div[@class="m-classlist-l"]/h3/a/@href ''')  # 获取url
            data_time = eroot.xpath(r'''//div[@class="m-classlist-l"]/p[1]/text()''')  # 获取time
            data_place = eroot.xpath(r'''//div[@class="m-classlist-l"]/p[2]/text() ''')  # 获取地点

            self.data_query_title.put(data_title)
            self.data_query_url.put(data_url)
            self.data_query_time.put(data_time)
            self.data_query_place.put(data_place)

    def get_data(self):
        a = 1
        while True:
            data_title = self.data_query_title.get()  # 标题列
            self.data_query_title.task_done()
            data_url = self.data_query_url.get()  # url列
            self.data_query_url.task_done()
            data_time = self.data_query_time.get()  # 时间列
            self.data_query_time.task_done()
            data_place = self.data_query_place.get()  # 地点列
            self.data_query_place.task_done()
            for i in data_title:
                c = i.strip()
                k = re.search(r"\w", c)
                if not k:
                    continue
                print("标题文本:", c)

            for i in data_url:
                print("网址:", "https:/" + i)   # 输出网址

            for i in data_time:  # type:str
                c = i.strip()
                k = re.search(r"\w", c)
                if not k:
                    continue
                print("时间:", c)  # 输出时间
            for i in data_place:
                c = i.strip()
                k = re.search(r"\w", c)
                if not k:
                    continue

                print("地点:", c)  # 输出地点
            print("第{}页".format(a))
            a += 1

    def main(self):
        thread_list = []
        url_list = Thread(target=self.url_list)
        thread_list.append(url_list)
        html_list = Thread(target=self.html_list)
        thread_list.append(html_list)
        data_list = Thread(target=self.data_list)
        thread_list.append(data_list)
        get_data = Thread(target=self.get_data)
        thread_list.append(get_data)

        for i in thread_list:
            i.setDaemon(True)  # 主线程结束才会结束
            i.start()  # 启动子线程

        time.sleep(20)  # 设置主线程10s结束
        for queue in [self.url_query, self.html_query, self.data_query_title]:
            queue.join()


d = new_east()
d.main()
