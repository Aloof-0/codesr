import requests

url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
page = input("请输入第几页(最多7页):")

params = {
    "on": True,
    "page": page,  # 页数
    "pageSize": 15,
    "productName": "",
    "conditionType": 1,
    "applyname": "",
    "applysn": ""
}
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"
}

response = requests.post(url=url, params=params, headers=headers)
html_json = response.json()
if __name__ == "__main__":
    print(html_json)
