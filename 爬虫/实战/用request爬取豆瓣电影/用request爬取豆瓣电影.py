import requests
url = r"https://movie.douban.com/j/chart/top_list"
params = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 0,  # 开始的条数
    "limit": 10  # 结束的条数
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
    "Accept": "*/*"
}
response = requests.get(url=url, params=params, headers=headers)

html_json = response.json()

print(html_json)