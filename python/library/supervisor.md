# Supervisor

- [项目地址](https://github.com/Supervisor/supervisor)
- [官方文档](http://www.supervisord.org/)

## 简介

用Python开发的一套通用的进程管理程序
能将一个普通的命令行进程变为后台daemon，并监控进程状态，异常退出时能自动重启。

## 配置文件

[官方配置说明](http://www.supervisord.org/configuration.html)

## 使用

```sh
# 启动
$ supervisord

# 查看配置示例
$ echo_supervisord_conf
```

## python3安装

```sh
$ pip install git+https://github.com/Supervisor/supervisor  
```

## 修改conf后需要

```sh
$ supervisorctl reload
```