# 安装与使用

前提条件

- NodeJS (v4.0.0及以上)
- Windows, Linux, Unix, or Mac OS X

## 安装

```sh
npm install gitbook-cli -g
```

`gitbook-cli` 是一个在相同系统上安装和使用多个GitBook版本的工具，在创建一个book的时候可以帮助我们自动安装需要的GitBook版本。

## 初始化书籍

```sh
gitbook init [path]
# 可选参数 <path> 表示在哪个路径下执行命令，默认为当前路径
```

1. 如果路径下没有 `SUMMARY.md` 文件，会创建它，内容如下，其中存放着书籍目录
    ```md
    # Summary

    * [Introduction](README.md)
    ```
2. 依据 `SUMMARY.md` 中的内容创建对应的文件(夹)，md文件中的内容只有对应书籍目录名的一级标题
    - 例如根据上面的内容，会在 `SUMMARY.md` 同级创建一个README.md文件，内容如下
         ```md
         # Introduction
         ```

## 创建书籍文件

```sh
gitbook build
# 当前路径下已经有 SUMMARY.md 文件，并且其中的目录所用到的文件(夹)也都存在
```

会在当前路径下创建 `_book` 文件夹，里面保存了这个书籍启动所需的所有文件

## 启动服务

```sh
gitbook serve
# 一个书籍所需的文件都齐备的情况下才可以运行
# 如果没有_book文件会自动用build命令生成一个
```

启动服务，默认端口为4000，这时就能通过网络访问了，例如本机访问 http://localhost:4000 ，内容与md文档中的内容实时同步

## 调试

可以在命令后面加上 `--log=debug --debug` 来获取更多信息

## 问题

已经安装了NodeJS但使用npm时还是报如下错误

```sh
/usr/bin/env: node: No such file or directory
```

解决：创建一个连接指向nodejs

```sh
ln -s /usr/bin/nodejs /usr/bin/node
```
