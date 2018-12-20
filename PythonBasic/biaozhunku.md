# string
格式化字符串：
```py
from string import Template
s = Template('There are ${key1} ${key2} Quotations Symbols')
print(s.substitute(key2='Python', key1=3))  # 'There are 3 Python Quotation Symbals'
print(s.substitute(key2='Python'))  # KeyError: 'key1'
print(s.safe_substitute(key2='Python'))  # 'There are ${key1} Python Quotations Symbols'
```
# os
## 函数
`rename(oldname, newname)`

`remove(待删除文件名)` 删除文件

`mkdir('dir_name')` 创建目录

`getcwd()`  返回当前文件所在的绝对路径

`chdir('a_dir')` 改变所在位置

`listdir('路径')` 返回路径下第一层级的所有目录、文件列表

`rmdir('目录')` 删除目录

`getpid()`获取当前进程的pid
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
# threading
## 多任务
### 并发与并行
并发：
> 指的是任务数多余cpu核数，通过操作系统的各种任务调度算法，实现用多个任务“一起”执行（实际上总有一些任务不在执行，因为切换任务的速度相当快，看上去一起执行而已）

并行：
> 指的是任务数小于等于cpu核数，即任务真的是一起执行的
### 异步同步
异步：多个程序同时运行（自己运行自己的不用管别人）

同步：协同步调，多个程序按顺序运行（运行时要考虑别人，要看什么时候才该自己）

> 实现**同步控制**：互斥锁

> **锁**
>
>优点: 确保了某段关键代码只能由一个线程从头到尾完整地执行  
> 
>缺点：阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了；由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁；

> **死锁**  
>
> 在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。

> **避免死锁**
> 
> 程序设计时注意；  
> 添加超时时间；

> **银行家算法**
> 
> 背景：一个银行家如何将一定数目的资金安全地借给若干个客户，使这些客户既能借到钱完成要干的事，同时银行家又能收回全部资金而不至于破产，这就是银行家问题。  
> 银行家就像一个操作系统，客户就像运行的进程，银行家的资金就是系统的资源。  
> 
> 问题描述：一个银行家拥有一定数量的资金，有若干个客户要贷款。每个客户须在一开始就声明他所需贷款的总额。若该客户贷款总额不超过银行家的资金总数，银行家可以接收客户的要求。客户贷款是以每次一个资金单位（如1万RMB等）的方式进行的，客户在借满所需的全部单位款额之前可能会等待，但银行家须保证这种等待是有限的，可完成的。
> 
> 银行家算法是从当前状态出发，逐个按安全序列检查各客户谁能完成其工作，然后假定其完成工作且归还全部贷款，再进而检查下一个能完成工作的客户，......。如果所有客户都能完成工作，则找到一个安全序列，银行家才是安全的。
### 阻塞、就绪、运行
任务的状态
```
新建任务，启动 --> 就绪Runnable（等待调度）

就绪 <==> 运行
 ↑         ↓
堵塞Blocked(等待)

运行 --> 死亡
```
### 进程和线程
同：
- 都能完成多任务

异：
- 进程是操作系统分配资源的基本单位；线程是执行任务的基本单位；
    > 线程是在进程下一级的概念
- 线程占用资源少，基本不拥有自己的系统资源，多线程并发性高
- 每个进程都有一个PID
- 每个进程里都有一个主线程来执行任务；每个线程都是由一个进程创建的。
    > 一个程序至少有一个进程，一个进程至少有一个线程；线程不能独立存在，必须依存于进程中
- 进程间不共享全局变量（资源）；一个进程内的所有线程共享全局变量（资源）

优缺：
线程执行任务开销小，但不利于资源的管理和保护。
## 基础
```py
import threading


def f():
    pass


t = threading.Thread(target=f)
t.start()
```
- 当调用start()时，才会真正的创建线程，并且开始执行
- 主线程会等子线程结束后才结束
- 一个进程内的所有线程共享全局变量
    - 弊端是对全局变量随意修改可能造成混乱（即线程非安全：如果多个线程同时对同一个全局变量操作，会出现资源竞争问题，从而数据结果会不正确）---> 上锁（同步控制）
    > 该global还得global
## 类
`Thread()`
- init接收target、name、args:tuple、kwargs:dict、daemon:bool参数
- 返回一个线程对象
- __repr__方法：返回`'<self所属类(self名字,状态)>'`
    - 状态有`initial`初始化了没start或`started`开始了或`stopped`结束了和`daemon`守护。
- `run()`方法: 线程调用self._targe()的地方。子类想实现特殊运行就重写这个方法。注意源代码的实现逻辑。
    ```py
    try:
        if self._target:
            self._target(*self._args, **self._kwargs)
    finally:
        del self._target, self._args, self._kwargs
    ``` 
- `start()`方法：启动线程
- `join([timeout])`
- `name`
---
`Lock()`
- 返回锁对象
- `acquire()`方法，锁定
    - 使锁进入locked状态（上锁）
    - 如果锁已经进入locked状态，本句代码会使任务进入阻塞状态，直到锁被其他任务释放被本任务上锁成功
- `release()`方法，释放锁
    - 使锁进入unlocked状态（解锁）
## 函数
`enumerate()`
- Return a list of all Thread **objects** currently alive
- len(它)可以查看当前线程数

`active_count()`
- Return the number of Thread objects currently alive.The returned count is equal to the length of the list returned by enumerate()
# multiprocessing
## 类
`Process()`
- 返回进程对象
    - 会复制全局环境（有运行代码会运行）
    - 进程间不共享全局变量
- init接收group，target, name, args:tuple, kwargs:dict参数
    - 与线程对比没有daemon参数，多了group
    > 其实线程也有group，默认为None且只能为None
- `strat()`方法：启动进程
- `is_alive()`：判断进程是否还活着
- `join([timeout])`: 是否等待子进程结束或等待多少秒
- `terminate()`：立即终止子进程
- `pid`：当前进程的pid
- `name`: 当前进程的别名
---
`Queue()`
- 返回队列对象，实现进程间通信，先进先出
- init可接收maxsize参数，默认值-1
- `put(obj, block=True, timeout=None)`
    - 如果block=False或者设置了timeout的情况下，已经满了就抛异常
- `put_nowait(obj)`
    - 如果已经满了则立即抛异常
- `get(block=True, timeout=None)`
- `get_nowait()`
- `qsize()` -> int
- `empty()` -> bool
- `full()` -> bool