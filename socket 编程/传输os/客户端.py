# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 11:39
# @Author   : 高冷
# @FileName  : 1.py

# 客户端都用sk来收发
# 只能用sk.close()关
# 收发要对应
# 如果一方结束了连接,则date, sk.recv() ，comm.recv()传的是空值
# 不允许发空值, 如果发了空值, 则会继续执行input
# ipconfig dir cd


import socket
a = ("127.0.0.1", 8003)
sk = socket.socket()
sk.connect(a)

while True:
    shuo = input("客户端:")
    sk.send(bytes(shuo, "utf8"))

    look = sk.recv(1024)
    print("服务端", str(look, "utf8"))
    if shuo == "exit":
        break
sk.close()

