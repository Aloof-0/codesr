import requests
from lxml import etree
import time
import re
class qiushi(object):
    def __init__(self):
        self.url = r"https://www.qiushibaike.com/imgrank/page/4/"  # 第一页
        self.headers = {"Accept": "*/*",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
                        }
        self.params = {
            "user_time": "2021 - 03 - 06 10: 37:01",
            "version": "2017-09-04 14:36",
            "url": self.url,
            "protocol": "https"
        }

    def get_html(self):
        response = requests.get(url=self.url, params=self.params, headers=self.headers)
        html = response.content.decode("utf-8")
        return html

    def main(self):
        html = self.get_html()
        HTML = etree.HTML(html)
        html_list = HTML.xpath("//img/@src")

        for i in html_list:
            time.sleep(0.5)
            html_url = "http:" + i
            resp = requests.get(url=html_url)
            img_name = re.sub(r"\D", "", i)
            img = img_name + ".jpg"
            jpg = "./qiushi/{}".format(img)
            html_binaries = resp.content
            with open(jpg, "wb") as f:
                f.write(html_binaries)
            print(img, "下载成功")


a = qiushi()
a.main()
