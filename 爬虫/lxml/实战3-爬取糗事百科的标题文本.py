import requests
from lxml import etree

class baike(object):
    def __init__(self, num):
        self.url_list = []
        self.url = "http://www.qiushibaike.com/8hr/page/{}/".format(num)

    def request_html(self):
        response = requests.get(self.url)
        resp = response.content.decode("utf-8")
        return resp

    def main(self):
        resp = self.request_html()
        html = etree.HTML(resp)
        html_list = html.xpath("//a[@class='recmd-content']/text()")
        for i in html_list: print(i)


a = baike(2)  # 获取页数
a.main()
