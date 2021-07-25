# arping 查看mac地址
"""
arping 主要是看是否有 网关冲突/是否有IP冲突 如果有可能是受到攻击了
arping 192.168.10.1 -c 1
arping -c 1 192.168.10.1 | grep "bytes from" | cut -d " " -f 5 | cut -d "(" -f 2 | cut -d ")" -f 1
"""

# 使用Netdiscover 进行被动/主动探测局域网内存活的机器
"""
netdiscover -i etho(网卡) -r 192.168.1.0/24(网段)
netdiscover -p 被动探测 仅仅是嗅探(隐秘性更高)
"""

# window 查看局域网内的ip
"""
1.   ipconfig/ALL
2.   for /L %i IN (1,1,254) DO ping -w 2 -n 1 192.168.0.%i
3.   arp -a
"""

# nmap扫描ip
"""
nmap -sn 扫描192.168.10.0 这个网段

nmap -sn 192.168.10.0/24 或者 nmap -sn 192.168.10.1 -254
-sn参数说明 表示只ping扫描，不进行端口扫描

nmap -sS半连接扫描 -p找出端口 范围 80,81 或者500-600
"""

# nc是netcat的简写,有着网络界的瑞士军刀的美誉.因为它短小精悍,功能实用,被设计为一个简单,可靠的网络工具
"""
nc的作用:
1. 实现人员TCP/UDP 端口的侦听,nc可以作为server 以 TCP 或者 UDP 方式侦听指定端口
2. 端口的扫描, nc可以作为client 发起client发起 TCP 或者UDP连接
3. 机器之间传输文件
4. 机器之前网络测速
nc 参数
- nv 表示我们扫描的目标是个IP地址不做域名解析
- w 表示超市时间
- z 表示进行端口扫描

例子:
nc -nv -w 1 -z 192.168.1.1 1-100
"""
