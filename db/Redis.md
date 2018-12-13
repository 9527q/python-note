# Redis

[官网](http://redis.io)

## 安装与启动

Mac安装

```sh
brew install redis
```

Mac启动服务

```sh
brew services start redis
# 或
redis-server
```

- 可以加配置文件参数，不加时使用内置的配置
- 安装后系统内会有一个配置文件/usr/local/etc/redis.conf可以当作模板，想使用的话也需要指出
- 不同配置文件启动后是不同的数据库（在配置文件中设置）

默认端口6379

客户端登录

```sh
redis-cli
```

终端中`redis-cli [command]`相当于 登录客户端，执行命令，退出客户端

验证服务：

```sh
redis-cli ping [message]
# 显示PONG或者message则说明服务正常
```

关闭服务：

启动服务的地方关闭

```sh
redis-cli shutdown [NOSAVE|SAVE]
# 默认为save,nosave真的就不会保存数据的吗？
```

## 配置

配置项 | `/usr/local/etc/redis.conf`中的默认值 | 说明
-|-|-
`#` | 注释声明
bind | bind 127.0.0.1 ::1 | 可以访问的IP，可以多行，一行可以多个（空格隔开）如果没有指定，则所有IP均可访问
port | port 6379 | 启动使用的端口
requirepass | `# requirepass foobared` | 密码，使用的时候redis-cli还是能连上，但是不能进行任何操作，必须先`auth foobared`登录才行，没有这句的时候就是无需密码，内置配置是无需密码的
daemonize | daemonize no | 设为yes则后台启动（启动后进入后台）
databases | databases 16 | 数据库数量，进入时默认为数据库0，使用select num来切换数据库(最大15)
dbfilename | dbfilename dump.rdb | 数据库文件的名字
dir | dir /usr/local/var/db/redis/ | 数据库存储位置
loglevel | loglevel notice | 日志级别（可选项：debug、verbose、notice、warning）
logfile | logfile "" | log文件，可以通过给定空字符串来让log显示在标准输出中，如果给定空字符串并且使用`daemonize yes`的话，会存到/dev/null中
save | save 900 1<br>save 300 10<br>save 60 10000 | `save <seconds> <changes>`在secondes秒内有changes则将数据同步到数据库文件，可以多行
rdbcompression | rdbcompression yes | 存数据时是否压缩，默认为yes，压缩算法LZF，选择否可以降低CPU压力，但数据库文件会变大
appendonly | appendonly no | 是否在每次操作后更新到数据库
appendfsync | appendfsync everysec | 自动保存数据到硬盘的条件 | 还有两个可选项no、always

## 常用命令

命令 | 说明
-|-
flushdb | 清空当前数据库
flushall | 清空所有数据库