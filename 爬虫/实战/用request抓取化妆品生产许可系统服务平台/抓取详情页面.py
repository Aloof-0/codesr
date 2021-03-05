import requests

url = r"http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"

params = {
    "id": "ca832f5a08864be389f75690318a5d47"  # 公司id
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"
}

response = requests.post(url=url, params=params, headers=headers)
html_json = response.json()
if __name__ == "__main__":
    print(html_json)
