# [Pycharm](https://www.jetbrains.com/pycharm/)

macOS 快捷键                           | 说明
---------------------------------------|--------------------
<kbd>⌘</kbd> <kbd>,</kbd>              | 打开设置
<kbd>⌘</kbd> <kbd>↩</kbd>︎             | 删除光标选中的内容并在光标后换行
<kbd>⌘</kbd> <kbd>⇧</kbd> <kbd>F</kbd> | 全局搜索
<kbd>⇧</kbd> <kbd>↩</kbd>︎             | 光标所在行下面增加一行并移动光标到新行
<kbd>⌥</kbd> <kbd>↩︎</kbd>             | 唤出建议

Win 快捷键                                            | 说明
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

1. <kbd>Shift Shift</kbd> 打开全局查找
2. 输入 `set background image`

## 设置代码规范检查

Preferences、设置、settings -> Editor -> Inspections

在里面勾选自己想要的或者取消选中不想要的即可。

## 设置79字符竖线

设置 -> Editor -> Code Style -> Python -> Hard wrap at -> 79

## 技巧

### 修改「函数参数」、「变量」时，批量更新所有使用的地方

修改后光标置于参数或变量上，接下来选择下面之一进行操作

- <kbd>⌥</kbd> <kbd>↩︎</kbd>，选择 `Update usages of reflect signature changes`
- 直接点击左侧的 “R 编辑” 按钮

### f-string 不用写 `f`，PyCharm 能自动添加

## 问题

### Windows的PyCharm中输入法不跟随光标

1. 关闭PyCharm
2. 打开安装路径，将jre64（64位系统）文件取个别的名字，让PyCharm找不到它
3. 下载[官方的java](https://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html)
    1. 选择接受许可
    2. 选择对应系统
4. 安装刚刚下载的java
