# Jupyter Notebook

- **代码块**：一个块就叫一个代码块，不是代码的才叫
- **命令模式 Command mode**：光标不在代码块内而是选中整个代码块；代码块左侧为蓝色边；<kbd>↩︎</kbd> 进入**编辑模式**
- **编辑模式 edit**：光标在代码块内，可以输入代码；代码块左侧为绿色边；<kbd>Esc</kbd> 进入**命令模式**

## 快捷键

快捷键                         | 作用
-------------------------------|-------------------------
<kbd>Shift</kbd> <kbd>↩︎</kbd> | 运行当前代码块，光标选中下一代码块并处于**命令模式**

### 编辑模式专有快捷键

快捷键                        | 作用
-------------------------------|---------------------------------
<kbd>Esc</kbd>                 | 进入**命令模式**
<kbd>⌥</kbd> <kbd>↩︎</kbd>     | 运行当前代码块，在当前代码块后新建一个代码块，光标选中新代码块并处于命令模式

### 命令模式专有快捷键

快捷键                   | 作用
--------------------------|--------------------
<kbd>↩︎</kbd>             | 进入编辑模式
<kbd>数字1-6</kbd>        | 把代码块变成 heading n 格式
<kbd>M</kbd>              | 把代码块变成标签
<kbd>A</kbd>              | 在上面插入代码块并将光标移过去
<kbd>B</kbd>              | 在上面插入代码块并将光标移过去
<kbd>D</kbd> <kbd>D</kbd> | 删除当前代码块

## kernel 添加与删除

### 添加 kernel

1. 终端切换到要添加为 kernel 的 Python 环境
2. `pip install ipykernel`
3. `sudo python -m ipykernel install --name <kernel-name>`
   - `kernel-name`：添加的 kernel 的名称

### 删除 kernel

```shell
# 查看所有的 kernel，会列出所有 kernel 的名称和位置
$ jupyter kernelspec list
# 根据名称删除某个 kernel，`kernel-name`: 要删除的 kernel 的名称
$ sudo jupyter kernelspec remove <kernel-name>
```
