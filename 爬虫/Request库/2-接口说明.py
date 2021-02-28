# 使用requests库前都要导入requests库
import requests

# 发送GET,POST,PUT,DELETE,HEAD 以及 OPTIONS 请求
a = requests.get('https://postman-echo.com/get')
b = requests.post('https://postman-echo.com/post')
c = requests.put('https://postman-echo.com/put')
d = requests.delete('https://postman-echo.com/delete')
f = requests.head('https://postman-echo.com/get')
print(a, b, c, d, f)
