# socket

```py
import socket
```

套接字：网络通信过程中端点的抽象表示，包含进行网络通信必需的五种信息：连接使用的协议，本地主机的IP地址，本地进程的协议端口，远地主机的IP地址，远地进程的协议端口。

## 创建、关闭socket

```py
# socket(AddressFamily, Type)
us = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp_socket
print('一些操作')
us.close()  # 不用的时候关闭
```

- Address Family：可以选择 AF_INET（用于 Internet 进程间通信） 或者 AF_UNIX（用于同一台机器进程间通信）,实际工作中常用AF_INET
- Type：套接字类型，可以是 SOCK_STREAM（流式套接字，主要用于 TCP 协议）或者 SOCK_DGRAM（数据报套接字，主要用于 UDP 协议）

默认的属性是主动的，使用listen将其变为被动的

## udp

bind、sendto、recvfrom

```py
udp_socket.bind(('', 7788))  # ip一般不用写，表示本机的任何一个ip
us.sendto(send_data.encode('utf-8'), ('192.168.1.103', 8080))  # 参：data:bytes, addr:tuple(ip:str, port:int)
bytes_data, addr = us.recvfrom(1024)  # 1024：接收最大字节数；阻塞等待；返回对方sendto里传入的全部原格式参数
```

### 获取本机ip和程序端口

```py
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # udp
s.connect(('1.1.1.1',80))  # 不会连接成功，不会阻塞住，不会报错
print(s.getsockname())
```

## tcp

客户端：connect、send、recv

```py
tcp_client_socket.connect((server_ip, server_port))  # 参：tuple(ip:str, port:int)；阻塞
tcp_client_socket.send(send_data.encode("gbk"))  # 参：data:bytes
recvData = tcp_client_socket.recv(1024)  # 参：1024:接收最大字节数，返回对方send的原格式参数; 阻塞
```

服务器：bind，accept，recv，send

```py
tcp_server_socket.bind(address)  # 参：tuple(ip:str, port:int)
tcp_server_socket.listen(128)  # 128：表示允许的最大同时链接数，超了就会拒绝。如果传小于0会赋值为0，有默认值（即可以不传）
# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
# client_socket用来为这个客户端服务
# tcp_server_socket就可以省下来专门等待其他新客户端的链接
client_socket, clientAddr = tcp_server_socket.accept()  # 阻塞
# 接收对方发送过来的数据
recv_data = client_socket.recv(1024)  # 接收1024个字节
client_socket.send(somedatas)
# 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
client_socket.close()
```

关闭listen后的套接字意味着被动套接字关闭了，会导致新的客户端不能够链接服务器，但是之前已经链接成功的客户端正常通信。

当客户端的套接字调用close后，服务器端会recv解堵塞，并且返回的长度为0，因此服务器可以通过返回数据的长度来区别客户端是否已经下线