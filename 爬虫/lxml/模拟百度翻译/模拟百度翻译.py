import requests
from lxml import etree
import time


class Translation(object):
    def __init__(self, word):
        url = r"https://fanyi.baidu.com/?aldtype=16047#may/zh/"  # 虚假的url
        self.url = url + word  # 真实的url
        print(self.url)
        self.number_word = len(word.encode('utf-8'))  # 判断utf8的字节数
        self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
                        , "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
        print(self.number_word)
        # self.params = 16047

    def get_html(self):
        response = requests.get(url=self.url, headers=self.headers)  # params=self.params
        html_text = response.content.decode("utf8")
        return html_text

    def main(self):
        html_text = self.get_html()
        text = etree.HTML(html_text)
        time.sleep(3)

        html_list = text.xpath("//p[@class='ordinary-output target-output clearfix']/text()")
        print(html_list)


c = Translation("CC")
c.main()
