# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 20:38
# @Author   : 高冷
# @FileName  : 服务端.py
import os
import socket

ip_port = ("127.0.0.1", 8898)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    print("waiting connect")
    conn, addr = sk.accept()
    flag = True
    while flag:

        client_bytes = conn.recv(1024)
        client_str = str(client_bytes, "utf8")
        func, file_byte_size, filename = client_str.split("|", 2)

        path = os.path.join(BASE_DIR, 'yuan', filename)
        has_received = 0
        file_byte_size = int(file_byte_size)

        f = open(path, "wb")
        while has_received < file_byte_size:
            data = conn.recv(1024)
            f.write(data)
            has_received += len(data)
        print("ending")
        f.close()
