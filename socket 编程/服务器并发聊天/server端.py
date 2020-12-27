# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 0:15
# @Author   : 高冷
# @FileName  : server端.py


import socketserver

class MYTCPhandle(socketserver.BaseRequestHandler):
    def handle(self):
        #print self.request,self.client_address,self.server
        conn = self.request
        a = "hello world".encode("utf8")
        self.request.sendall(a)  #给客户端发一条信息内容

        # 一直侦听客户端发送过来的消息

        while True:
            client_data = conn.recv(1024)   #接受客户端发送过来的消息，1024代表最多只能在缓冲区拿数据的大小，缓冲区默认为8K
            print("客户端", str(client_data,"utf8"))


            b = input(">>").encode("utf8")
            conn.send(b)  # 向客户端发送消息
            if client_data == 'exit':
                print ('连接的客户端已断开')
                break





        # self.data = self.request.recv(1024)
        # print(str(self.data).encode("utf8"))

        # c = input(">>>")
        # self.request.sendall(bytes(c, "utf8"))

if __name__ == "__main__":
    sever = socketserver.ThreadingTCPServer(("127.0.0.1", 8010), MYTCPhandle)
    sever.serve_forever()


