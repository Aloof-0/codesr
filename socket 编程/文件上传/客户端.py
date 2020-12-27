# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 20:38
# @Author   : 高冷
# @FileName  : 客户端.py
import os
import socket

ip_port = ("127.0.0.1", 8898)
sk = socket.socket()
sk.connect(ip_port)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print("客户端启动....")

while True:
    inp = input("please input:")

    if inp.startswith("post"):
        method, local_path = inp.split("|", 1)
        local_path = os.path.join(BASE_DIR, local_path)
        file_byte_size = os.stat(local_path).st_size
        file_name = os.path.basename(local_path)
        post_info = "post|%s|%s" % (file_byte_size, file_name)
        sk.sendall(bytes(post_info, "utf8"))
        has_sent = 0
        file_obj = open(local_path, "rb")
        while has_sent < file_byte_size:
            data = file_obj.read(1024)
            sk.sendall(data)
            has_sent += len(data)
        file_obj.close()
        print("上传成功")
