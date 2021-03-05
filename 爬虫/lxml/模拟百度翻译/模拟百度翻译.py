import requests
from lxml import etree
import time

class Translation(object):
    def __init__(self, word):
        url = r"https://fanyi.baidu.com/?aldtype=16047#may/zh/"  # 虚假的url
        self.url = url + word  # 真实的url
        self.number_word = len(word.encode('utf-8'))  # 判断utf8的字节数
        self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        print(self.number_word)

    def get_html(self):
        response = requests.get(url=self.url, headers=self.headers)
        html_text = response.content.decode("utf8")
        print(html_text)
        return html_text

    def main(self):
        html_text = self.get_html()
        text = etree.HTML(html_text)
        print(text)
        time.sleep(3)
        html_list = text.xpath("//p[@class='ordinary-output target-output clearfix']/text()")
        print(html_list)

c = Translation("爱你")
c.main()