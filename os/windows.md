# Windows

## 快捷键

快捷键 | 功能 | 补充
-|-|-
F2 | 重命名文件夹
Enter | 打开文件或目录
Backspace | 回到上一级目录
Ctrl N | 打开文件夹 | 打开一个新的资源管理器窗口，位置是当前位置
Ctrl Shift N | 新建文件夹
Alt F4 | 关闭窗口 | 在桌面时关机
Alt Enter | 查看文件属性
Win E | 打卡资源管理器
Win R | 运行
Win L | 锁屏
Win 数字 | 打开任务栏应用

## 组合键代替上下左右键_AutoHotkey

1. 新建文本文件，写入
    ```txt
    !j::send,{left}
    !l::send,{right}
    !i::send,{up}
    !k::send,{down}
    ```
    > `!`代表Alt,  
    > `^`代表Ctrl,  
    > `+`代表Shift,  
    > `#`代表Win,
2. 后缀改为.ahk
3. 设置打开方式为AutoHotkey
4. 放到开机自启目录

## 强制删除

1. 新建文本文件，写入
    ```shell
    DEL /F /A /Q \\?\%1
    RD /S /Q \\?\%1
    ```
2. 后缀改为.bat
3. 把要删除的文件或目录拖到这个bat文件图标上即可

## 打开自启动文件夹

运行 -> `shell:startup`
> 回退一级即是程序Programs文件夹，想要没有安装的软件出现在Win里，就把快捷方式放到这即可

## 文件

大小写不敏感

## cmd

命令 | 作用 | 说明
-| - | -
dir | 所有文件信息、总数量、总大小 | 包括隐藏文件
cls | 清屏
ping、ipconfig | /