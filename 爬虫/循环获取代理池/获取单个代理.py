import requests


def get_proxy():

    return requests.get("http://127.0.0.1:5010/get_all/").json()

proxy = get_proxy()
for i in proxy:
    print({"http": "http://{}".format(i.get("proxy"))})
