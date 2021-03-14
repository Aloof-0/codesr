import requests

import re
url = "https://gitee.com/login"


# 创建一个session对象
session = requests.session()

login_response = session.get(url=url)
# 得到html文本
login_html = login_response.content.decode("utf-8")

login_token = re.search(r'''input name="authenticity_token" type="hidden" value="(.*?)"''', login_html)
# 得到token文本
print(login_token.group(1))






headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/67.0.3396.87 Safari/537.36',
    "Referer": "https://gitee.com"
}
denglu_session = session.post(url=url)
data = {
    "encrypt_key": "password",
    "authenticity_token": login_token.group(1),
    "user[login]": "itcast407",
    "user[password]": "Cjcslhp123"
}

session.post(url=url, data=data, headers=headers)



# 3 向gitee.com/itcast407发送get请，验证是否登录成功
profile_url = "https://www.gitee.com/itcast407"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/67.0.3396.87 Safari/537.36',
    "Referer": "https://gitee.com"
}
response = session.get(url=profile_url, headers=headers)

with open('gitee.com.html', 'wb') as f:
    f.write(response.content)