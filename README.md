[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![](https://img.shields.io/github/repo-size/9527q/python-note.svg?label=Repo%20size&style=flat-square)

Python
======

![python](images/python.png)

- Python 是一种解释型、面向对象、动态数据类型的高级程序设计语言。
- 由荷兰人 *Guido van Rossum* 于 1989 年底发明，第一个公开发行版发行于1991年
- 像 Perl 语言一样，Python 源代码同样遵循 GPL(GNU General Public License)协议
- Python 的解释器如今有多个语言实现，我们常用的是 CPython（官方版本的C语言实现），其他还有 Jython（可以运行在Java平台）、IronPython（可以运行在.NET和Mono平台）、PyPy（Python实现的，支持JIT即时编译）

目录
- [Python 2 以来的新东西](./diff23/README.md)
- [标准库](./standard-library/README.md)

## 优点

- 简单、易学、免费、开源、高级语言、规范的代码(极佳的可读性)
- 可移植性(多平台轻松移植)
- 解释型语言(对应编译型语言)
    > 编译型语言 比如C或C++写的程序可以从源文件转换到二进制代码。当运行程序时，把程序从硬盘复制到内存中并且运行。
    >
    > 解释型语言 直接从源代码运行程序。在计算机内部，解释器把源代码转换成字节码，然后再翻译成机器语言并运行。
- 面向对象(OO)
    > 面向过程: 程序是由过程或仅仅是可重用代码的函数构建起来的
    > 
    > 面向对象: 程序是由数据和功能组合而成的对象构建起来的
- 可扩展性(比如关键算法用C++实现)
- 丰富的库(标准库就很强大，“功能齐全”)

## 缺点

效率(解释型语言)

## 应用

- Web应用开发
- 操作系统管理、服务器运维的自动化脚本
    > 在很多操作系统里，Python是标准的系统组件。  
    > 一般说来，Python编写的系统管理脚本在可读性、性能、代码重用度、扩展性几方面都优于普通的shell脚本。
- 网络爬虫
- 科学计算
- 桌面软件
- 服务器软件（网络软件）
- 游戏
- 构思实现，产品早起原型和迭代

## 终端执行python

`$ python`进入python环境

第一行提示版本号和更新日期

下面的`>>>`是提示符，这里可以输入Python代码

Ctrl D 或者执行 `exit()` 退出

在 IPython 中使用 `Ctrl D` 后还需要确认一下才能退出
