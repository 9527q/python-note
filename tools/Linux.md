# Linux

## 常用命令

命令 | 说明
-|-
cd | 返回家目录
cd - | 返回上次的位置
df -h | 查看各文件系统空间使用情况
top | 查看系统实时运行情况
`sudo service <serve name> <opt>` | opt: status/start/stop`,服务状态、开启、关闭
locale | 将语言环境的信息写到标准输出

## 常用文件

文件 | 说明
-|-
/var/log/syslog | 系统日志
/etc/hosts |
/etc/apt/sources.list | 软件源

## 修改Ubuntu软件源

1. 修改源文件
    >修改为清华源
    >阿里源则将地址替换为：`http://mirrors.aliyun.com/ubuntu/`
    >注意不同Ubuntu版本是不同的
2. `sudo apt-get update`
    访问源列表里的每个网址，并读取软件列表，然后保存在本地电脑
3. sudo apt-get upgrade
    把本地已安装的软件，与刚下载的软件列表里对应软件进行对比，如果发现已安装的软件版本太低，就会提示你更新

## 切换到超级用户

ikeliu@ubuntu:~$ su
然后输入超级用户的密码即可
输入正确密码后提示‘认证失败’
Ubuntu安装后，root用户默认是被锁定的，不允许登录，也不允许`su`到root，这时用`sudo passwd`命令修改一下密码就可以su到root用户了，注意必须加sudo，直接passwd修改的是当前用户的密码。

## Ubuntu安装搜狗输入法

官网下载安装包放到Ubuntu
sudo apt install gdebi
右键点击安装包，打开方式选择GDebi Package Installer
再点击安装即可
安装好后修改系统的「语言支持」的「键盘输入法系统」为fcitx，重启即可