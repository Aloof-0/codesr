# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 21:56
# @Author   : 高冷
# @FileName  : clmit.py


import socket
ip_port = ('127.0.0.1',8879)
sk = socket.socket()
sk.connect(ip_port)
print ("客户端启动：")
while True:
    inp = input('cdm:>>>').strip( )
    if len(inp)==0:
        continue
    if inp=="q":
        break
    sk.sendall(bytes(inp,"utf8"))
    server_response=sk.recv(1024)
    print (str(server_response,"gbk"))
    print('receive data size',len(server_response))
    if inp == 'exit':
        break
sk.close()