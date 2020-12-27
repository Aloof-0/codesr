# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 21:56
# @Author   : 高冷
# @FileName  : sever.py


import socket
import subprocess
ip_port = ('127.0.0.1',8879)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
print("服务端启动...")
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

    conn.close()