# Pycharm

由JetBrains公司使用Java开发的强大的 Python IDE，很好用

> ALL THE PYTHON TOOLS IN ONE PLACE

[Pycharm官网](https://www.jetbrains.com/pycharm/)

## 安装

[官方下载安装指南](https://www.jetbrains.com/pycharm/download/)，不论 Windows、macOS 还是 Linux官网都有完善的安装指导，Ubuntu 16.04 及更高版甚至支持通过命令安装

## 快捷键

### macOS

options                                | explain
---------------------------------------|-----------------------
<kbd>⌘</kbd> <kbd>,</kbd>              | 打开设置
<kbd>⌘</kbd> <kbd>↩</kbd>︎             | 删除光标选中的内容并在光标处换行(光标不动)
<kbd>⇧</kbd> <kbd>↩</kbd>︎             | 光标所在行下面增加一行并移动光标到新行
<kbd>⌘</kbd> <kbd>⇧</kbd> <kbd>F</kbd> | 全局搜索

### Windows

options                                            | explain
---------------------------------------------------|-------------------
<kbd>Ctrl</kbd> <kbd>/</kbd>                       | 行注释/取消行注释
<kbd>Ctrl</kbd> <kbd>B</kbd>                       | 查看源代码（Ctrl 左键）
<kbd>Ctrl</kbd> <kbd>D</kbd>                       | 在光标所在行下面复制当前行
<kbd>Ctrl</kbd> <kbd>X</kbd>                       | 剪切光标所在行
<kbd>Ctrl</kbd> <kbd>F4</kbd>                      | 关闭当前py文件
<kbd>Ctrl</kbd> <kbd>F5</kbd>                      | 运行上一次运行的py文件
<kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>L</kbd>        | 整理代码（缩进、空格等）
<kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>数字键</kbd> | 当前行加书签
<kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>F10</kbd>    | 运行光标所在py文件
<kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>↕️</kbd>     | 移动当前行
<kbd>Alt</kbd> <kbd>1</kbd>                        | 打开/关闭资源管理器
<kbd>Alt</kbd> <kbd>4</kbd>                        | 打开/关闭运行状态窗口
<kbd>Alt</kbd> <kbd>←、→</kbd>                      | 在打开的py文件之间切换
<kbd>Alt</kbd> <kbd>Insert</kbd>                   | 当前位置新建文件
<kbd>Alt</kbd> <kbd>左键</kbd>                     | 选中多个光标位置
<kbd>Shift</kbd> <kbd>F6</kbd>                     | 修改文件或目录名
<kbd>Shift</kbd> <kbd>Enter</kbd>                  | 在光标所在行下创建行并缩进至适当位置
<kbd>Shift</kbd> <kbd>Tab</kbd>                    | 回退缩进
<kbd>Shift</kbd> <kbd>Shift</kbd>                  | 全局查找
中键摁住滑动鼠标                                   | 选中多个光标位置
<kbd>Tab</kbd>                                     | 缩进

## 背景图片设置

1. Shift Shift 打开全局查找
2. 输入 set background image

## 设置代码规范检查

Preferences、设置、settings -> Editor -> Inspections

在里面勾选自己想要的或者取消选中不想要的即可。

## 设置79字符竖线

设置 -> Editor -> Code Style -> Python -> Hard wrap at -> 79

## 问题

### Windows的PyCharm中输入法不跟随光标

1. 关闭PyCharm
2. 打开安装路径，将jre64（64位系统）文件取个别的名字，让PyCharm找不到它
3. 下载[官方的java](https://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html)
    1. 选择接受许可
    2. 选择对应系统
4. 安装刚刚下载的java

<!-- 
断网激活码
BJUYHHRZXO-eyJsaWNlbnNlSWQiOiJCSlVZSEhSWlhPIiwibGljZW5zZWVOYW1lIjoiSmV0QiDlhajlrrbmobYiLCJhc3NpZ25lZU5hbWUiOiIiLCJhc3NpZ25lZUVtYWlsIjoiIiwibGljZW5zZVJlc3RyaWN0aW9uIjoiIiwiY2hlY2tDb25jdXJyZW50VXNlIjpmYWxzZSwicHJvZHVjdHMiOlt7ImNvZGUiOiJJSSIsImZhbGxiYWNrRGF0ZSI6IjIwMTktMTAtMjEiLCJwYWlkVXBUbyI6IjIwMjAtMTAtMjAifSx7ImNvZGUiOiJBQyIsImZhbGxiYWNrRGF0ZSI6IjIwMTktMTAtMjEiLCJwYWlkVXBUbyI6IjIwMjAtMTAtMjAifSx7ImNvZGUiOiJEUE4iLCJmYWxsYmFja0RhdGUiOiIyMDE5LTEwLTIxIiwicGFpZFVwVG8iOiIyMDIwLTEwLTIwIn0seyJjb2RlIjoiUFMiLCJmYWxsYmFja0RhdGUiOiIyMDE5LTEwLTIxIiwicGFpZFVwVG8iOiIyMDIwLTEwLTIwIn0seyJjb2RlIjoiR08iLCJmYWxsYmFja0RhdGUiOiIyMDE5LTEwLTIxIiwicGFpZFVwVG8iOiIyMDIwLTEwLTIwIn0seyJjb2RlIjoiRE0iLCJmYWxsYmFja0RhdGUiOiIyMDE5LTEwLTIxIiwicGFpZFVwVG8iOiIyMDIwLTEwLTIwIn0seyJjb2RlIjoiQ0wiLCJmYWxsYmFja0RhdGUiOiIyMDE5LTEwLTIxIiwicGFpZFVwVG8iOiIyMDIwLTEwLTIwIn0seyJjb2RlIjoiUlMwIiwiZmFsbGJhY2tEYXRlIjoiMjAxOS0xMC0yMSIsInBhaWRVcFRvIjoiMjAyMC0xMC0yMCJ9LHsiY29kZSI6IlJDIiwiZmFsbGJhY2tEYXRlIjoiMjAxOS0xMC0yMSIsInBhaWRVcFRvIjoiMjAyMC0xMC0yMCJ9LHsiY29kZSI6IlJEIiwiZmFsbGJhY2tEYXRlIjoiMjAxOS0xMC0yMSIsInBhaWRVcFRvIjoiMjAyMC0xMC0yMCJ9LHsiY29kZSI6IlBDIiwiZmFsbGJhY2tEYXRlIjoiMjAxOS0xMC0yMSIsInBhaWRVcFRvIjoiMjAyMC0xMC0yMCJ9LHsiY29kZSI6IlJNIiwiZmFsbGJhY2tEYXRlIjoiMjAxOS0xMC0yMSIsInBhaWRVcFRvIjoiMjAyMC0xMC0yMCJ9LHsiY29kZSI6IldTIiwiZmFsbGJhY2tEYXRlIjoiMjAxOS0xMC0yMSIsInBhaWRVcFRvIjoiMjAyMC0xMC0yMCJ9LHsiY29kZSI6IkRCIiwiZmFsbGJhY2tEYXRlIjoiMjAxOS0xMC0yMSIsInBhaWRVcFRvIjoiMjAyMC0xMC0yMCJ9LHsiY29kZSI6IkRDIiwiZmFsbGJhY2tEYXRlIjoiMjAxOS0xMC0yMSIsInBhaWRVcFRvIjoiMjAyMC0xMC0yMCJ9LHsiY29kZSI6IlJTVSIsImZhbGxiYWNrRGF0ZSI6IjIwMTktMTAtMjEiLCJwYWlkVXBUbyI6IjIwMjAtMTAtMjAifV0sImhhc2giOiIxNDk3NTE1Ni8wIiwiZ3JhY2VQZXJpb2REYXlzIjo3LCJhdXRvUHJvbG9uZ2F0ZWQiOmZhbHNlLCJpc0F1dG9Qcm9sb25nYXRlZCI6ZmFsc2V9-iVF7LEL/XJsofTwwRudhfUWOzxx13tVbWDTjwG/LTknVjf3aHo/w75RT6wqx+OonmOrJruZajSa9ykfCRu65t4dH8N4B9cTDKphBcPmJ8YTu1CBIdICZDqSgPLuMiewhxjqxM1pZF5cR/y1lwFk+HelbrLLqeAotctQ1oNcWQdjViwXTwQvK+Pkm48r5jRfDEU9Lze2y4xIryLkp8aSWE9rMMNE0FNaJv2+Fe6+10JhE1szLGvxTzahWb2zn3XMqML4BeJSFR5AtxnuQ/q+/P2gI1g0HRZl2NksFXp/7TLHNA0HW1yNbM9/Vf1zTPO5QCYUALR+3PKDXqgbLXuABLg==-MIIElTCCAn2gAwIBAgIBCTANBgkqhkiG9w0BAQsFADAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBMB4XDTE4MTEwMTEyMjk0NloXDTIwMTEwMjEyMjk0NlowaDELMAkGA1UEBhMCQ1oxDjAMBgNVBAgMBU51c2xlMQ8wDQYDVQQHDAZQcmFndWUxGTAXBgNVBAoMEEpldEJyYWlucyBzLnIuby4xHTAbBgNVBAMMFHByb2QzeS1mcm9tLTIwMTgxMTAxMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxcQkq+zdxlR2mmRYBPzGbUNdMN6OaXiXzxIWtMEkrJMO/5oUfQJbLLuMSMK0QHFmaI37WShyxZcfRCidwXjot4zmNBKnlyHodDij/78TmVqFl8nOeD5+07B8VEaIu7c3E1N+e1doC6wht4I4+IEmtsPAdoaj5WCQVQbrI8KeT8M9VcBIWX7fD0fhexfg3ZRt0xqwMcXGNp3DdJHiO0rCdU+Itv7EmtnSVq9jBG1usMSFvMowR25mju2JcPFp1+I4ZI+FqgR8gyG8oiNDyNEoAbsR3lOpI7grUYSvkB/xVy/VoklPCK2h0f0GJxFjnye8NT1PAywoyl7RmiAVRE/EKwIDAQABo4GZMIGWMAkGA1UdEwQCMAAwHQYDVR0OBBYEFGEpG9oZGcfLMGNBkY7SgHiMGgTcMEgGA1UdIwRBMD+AFKOetkhnQhI2Qb1t4Lm0oFKLl/GzoRykGjAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBggkA0myxg7KDeeEwEwYDVR0lBAwwCgYIKwYBBQUHAwEwCwYDVR0PBAQDAgWgMA0GCSqGSIb3DQEBCwUAA4ICAQAF8uc+YJOHHwOFcPzmbjcxNDuGoOUIP+2h1R75Lecswb7ru2LWWSUMtXVKQzChLNPn/72W0k+oI056tgiwuG7M49LXp4zQVlQnFmWU1wwGvVhq5R63Rpjx1zjGUhcXgayu7+9zMUW596Lbomsg8qVve6euqsrFicYkIIuUu4zYPndJwfe0YkS5nY72SHnNdbPhEnN8wcB2Kz+OIG0lih3yz5EqFhld03bGp222ZQCIghCTVL6QBNadGsiN/lWLl4JdR3lJkZzlpFdiHijoVRdWeSWqM4y0t23c92HXKrgppoSV18XMxrWVdoSM3nuMHwxGhFyde05OdDtLpCv+jlWf5REAHHA201pAU6bJSZINyHDUTB+Beo28rRXSwSh3OUIvYwKNVeoBY+KwOJ7WnuTCUq1meE6GkKc4D/cXmgpOyW/1SmBz3XjVIi/zprZ0zf3qH5mkphtg6ksjKgKjmx1cXfZAAX6wcDBNaCL+Ortep1Dh8xDUbqbBVNBL4jbiL3i3xsfNiyJgaZ5sX7i8tmStEpLbPwvHcByuf59qJhV/bZOl8KqJBETCDJcY6O2aqhTUy+9x93ThKs1GKrRPePrWPluud7ttlgtRveit/pcBrnQcXOl1rHq7ByB8CFAxNotRUYL9IF5n3wJOgkPojMy6jetQA5Ogc8Sm7RG6vg1yow==


-您好！关于您购买的订单：738716160237998370，以下是您的发货信息！ 
激活码太长，请直接点进去下载(别用迅雷下载) 
https://www.lanzous.com/i7k5w3c
******激活码必须下载到电脑在复制，不然失效，如何激活：软件菜单-帮助-注册，把激活码全部复制到软件激活窗口中的Activation code****** 
激活不成功 请看这里： https://shimo.im/docs/8icBv925HHESLZ1w/ 
感谢您的惠顾，欢迎下次光临！

 -->