import requests

url = r"https://pic.qiushibaike.com/system/pictures/12411/124115756/medium/OUKZEN7N39EX940V.jpg"

# 单url就能获取

response = requests.get(url=url)
# text(字符串) content(二进制) json()(JSON对象)
html_binaries = response.content
with open("./jiushi.jpg","wb") as f:
    f.write(html_binaries)