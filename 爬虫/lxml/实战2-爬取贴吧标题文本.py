import requests
from lxml import etree
import time
import re

class tieba(object):
    def __init__(self, kw):
        self.url_list = []
        self.proxies = {
            "http": "http://223.215.6.104:9999",
        }
        self.all_html = []
        for i in range(0, 550, 50):
            self.url_list.append("https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}".format(kw, i))
        print(self.url_list)

    def html_art(self):
        for i in self.url_list:
            time.sleep(6)
            response = requests.get(i,proxies=self.proxies)
            str_html = response.content.decode("utf8")

            self.all_html.append(str_html)
        return self.all_html

    def main(self):
        number = 0

        no_html = self.html_art()
        for i in no_html:
            print("\033[31m 第{}页 \033[0m".format(number+1))
            html = etree.HTML(i)
            re_path = "//div[@class='threadlist_abs threadlist_abs_onlyline ']/text()"
            html_list = html.xpath(re_path) if len(re_path) > 0 else None
            num = 0
            for i in html_list:
                c = i.strip()
                d = re.search("\w", c)
                if not d:
                    continue
                print("第", num, "页", c)
                num += 1
            number += 1


a = tieba("刘飞儿的小黑屋")
a.main()
