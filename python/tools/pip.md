# PIP

## Ubuntu安装pip

```sh
$ sudo apt-get install python-pip
$ sudo apt-get install python3-pip
```

## 安装相关库

```sh
$ pip install -r requirements.txt
```

## 升级pip到指定版本

```sh
$ python3 -m pip install --user --upgrade pip==9.0.3
```

### 升级后报错

报错信息：
> qly@qlyComputer:~$ pip
> Traceback (most recent call last):
>       File "/usr/bin/pip", line 9, in <module>
>           from pip import main
> ImportError: cannot import name 'main'

发现即使卸载pip并重新安装后问题也存在
是由于pip更新为10.0.0后库里面的函数有所变动造成的

解决办法：
修改/usr/bin/pip文件

1. 修改的内容如下
    > 原文：from pip import main 
    > 修改后：from pip._internal import main
    - 此时应该就能正常用了
2. 如果还不行，继续更改
    ```py
    # 修改前
    from pip import main  
    if __name__ == '__main__':  
        sys.exit(main()) 
    # 修改后
    from pip import __main__  # 这行也要修改
    if __name__ == '__main__':  
        sys.exit(__main__._main())  # 增加__main__._
    ```