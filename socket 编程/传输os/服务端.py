# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 11:39
# @Author   : 高冷
# @FileName  : server.py

# 服务段都用comm来收发
# sk.close是关闭socket连接 但comm.close是关闭当前客户端连接
# import subprocess
# import socket
#
# a = ("127.0.0.1", 8001)
# sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sk.bind(a)
# sk.listen(3)
#
#
# while 1:
#     conn, address = sk.accept()
#
#
#     data = conn.recv(1024)
#
#     change = str(data, "utf8")
#     print("waiting...")
#
#     A = subprocess.Popen(change, shell=True, stdout = subprocess.PIPE)
#     B = A.stdout.read()
#     conn.send(B)





import socket
import subprocess
ip_port = ('127.0.0.1',8003)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
print ("服务端启动...")
while True:
    conn,address = sk.accept()
    while True:
        try:

            client_data=conn.recv(1024)
        except Exception:
            break
        print (str(client_data,"utf8"))
        print ("waiting...")
        # server_response=input(">>>")
        # conn.sendall(bytes(server_response,"utf8"))
        cmd=str(client_data,"utf8").strip()
        cmd_call=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        cmd_result=cmd_call.stdout.read()
        if len(cmd_result)==0:
            cmd_result=b"no output!"
        conn.sendall(cmd_result)
        print('send data size',len(cmd_result))
        print('******************')
        print('******************')
        print('******************')














"""

import socket

number = ("127.0.0.1", 8000)
sk = socket.socket()
sk.bind(number)
sk.listen(3)

comm, addr = sk.accept()
while 1:
    sk.accept()
    while 1:
        date = comm.recv(1024)
        if not date:
          break
        print(date)
        a = input("")

        abc = bytes(a, encoding="utf8")
        comm.send(abc)

sk.close()

"""








