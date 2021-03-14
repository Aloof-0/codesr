# 导入抓取首页的包
import requests
import time
from 抓取首页 import *
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"
}
url = r"http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
for i in html_json["list"]:  # 循环输出id
    params = {
        "id": i["ID"]  # 批量抓取公司id
    }
    response = requests.post(url=url, params=params, headers=headers)
    html_json = response.json()
    time.sleep(2)
    print(html_json)

