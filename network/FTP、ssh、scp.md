# ftp ssh scp

## FTP

FTP 是File Transfer Protocol（文件传输协议）的英文简称，而中文简称为“文传协议”。用于Internet上的控制文件的双向传输。

同时，它也是一个应用程序（Application）。基于不同的操作系统有不同的FTP应用程序，而所有这些应用程序都遵守同一种协议以传输文件。

## ssh

SSH为Secure Shell的缩写，由 IETF 的网络工作小组（Network Working Group）所制定；SSH 为建立在应用层和传输层基础上的安全协议。

SSH是目前较可靠，专为远程登录会话和其他网络服务提供安全性的协议。常用于远程登录，以及用户之间进行资料拷贝。

利用SSH协议可以有效防止远程管理过程中的信息泄露问题。SSH最初是 UNIX 系统上的一个程序，后来又迅速扩展到其他操作平台。SSH 在正确使用时可弥补网络中的漏洞。SSH 客户端适用于多种平台。

使用SSH服务，需要安装相应的服务器和客户端。
> linux安装ssh服务器
> ```sh
> sudo apt install openssh-server
> ```
> > 使用ssh访问，如访问出现错误。可查看是否有该文件 ～/.ssh/known_ssh 尝试删除该文件解决。

ssh远程登录:

```sh
ssh 用户名@IP
```

## scp

scp命令用于复制文件和目录。

scp是 secure copy的缩写, scp是Linux系统下基于ssh登陆进行安全的远程文件拷贝命令。(所以使用该命令的前提条件要求目标主机已经成功安装openssh-server)

```sh
scp -r 目标用户名@目标主机IP地址：/目标文件的绝对路径  /保存到本机的绝对/相对路径
scp -r FolderName RemoteUserName@RemoteHostIp:RemoteFolder  # 上传
scp -r RemoteUserName@RemoteHostIp:RemoteFolder FolderName  # 下载
scp -r itcast@192.168.1.100:/home/itcast/QQ_dir/ ./mytest/lisi  # 例
```

- `-r`表示目录，如果拷贝文件不用则加
- 在后续会提示输入“yes”此时，只能输“yes”而不能简单输入“Y”