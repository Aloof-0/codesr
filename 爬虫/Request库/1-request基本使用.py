import requests

# 1.构建目标url地址
url = "https://www.baidu.com"

# 2.往目标url地址 发送请求,获取响应对象
response = requests.get(url)
print(response)
print(type(response))
# 3.从响应对象中通过对象属性提取数据[状态码, 响应头， 响应体]

# 状态码
print(response.status_code)
# 响应的cookie
print(response.cookies)
# 响应头
print(response.headers)
# content属性
# print(response.content)
# 将bytes类型转化成字符串
# print(response.content.decode("utf8"))


# 提取响应数据的方案二
# text 属性 :响应体字符串[存在乱码问题] 原因编码和解码格式不一样导致
response.encoding = "utf8"  # ISO-8859-1 国际标准的编码格式
print(response.text)
