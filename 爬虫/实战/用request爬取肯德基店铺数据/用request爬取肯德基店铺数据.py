import requests

url = r"http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"

params = {
    "cname": "",
    "pid": "",
    "keyword": "北京",
    "pageIndex": 8,  # 页数
    "pageSize": 10
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.0"
}
response = requests.post(url=url, headers=headers, params=params)

html_json = response.text
print(html_json)
