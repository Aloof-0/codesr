# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 0:15
# @Author   : 高冷
# @FileName  : client.py

import socket
sk = socket.socket()
a = ("127.0.0.1", 8010)
sk.connect(a)


print("客户端启动中......")

while True:
    look = sk.recv(1024)
    print("服务端：", str(look, "utf8"))

    b = input(">>").encode("utf8")
    sk.send(b)






