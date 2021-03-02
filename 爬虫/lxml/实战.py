import requests
from lxml import etree
# 获取html文本
headers = {
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
}
url = "https://tieba.baidu.com/f?kw=%E5%90%90%E6%A7%BD"
response = requests.get(url=url)

text = response.content.decode("utf8")
print(text)
# print(text)
html = etree.HTML(text)
aaa = html.xpath("//div[@class='threadlist_abs threadlist_abs_onlyline ']/text()")
print(aaa)

for i in aaa:
  item = {}
  item["front"] = i
  print(item)
