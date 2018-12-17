# Python

## 终端执行python

`$ python`进入python环境

第一行提示版本号和更新日期

下面的`>>>`是提示符，这里可以输入Python代码

`Ctrl D` 或者执行 `exit()` 退出

在 IPython 中使用 `Ctrl D` 后还需要确认一下才能退出

## 创建空集合

```py
s = set()
s = {i for i in []}  # 推导式产生的一定是集合类型，不会因为空数据而变成字典
```

## 查看解释器位置

```py
import sys
sys.executable
```

## 参数

### -u

```sh
python -u fname.py
```

标准错误(std.err)和标准输出(std.out)的输出规则：

标准错误直接输出到屏幕，有一个输出一个；标准输出先放缓存里，遇到换行或者积累到一定大小才输出

所以下面程序的实际结果是 `stderr1stderr2stdout1stdout2`

```py
import sys

sys.stdout.write("stdout1")
sys.stderr.write("stderr1")
sys.stdout.write("stdout2")
sys.stderr.write("stderr2")
```

`-u` 参数的作用就是声明 unbuffered

### -m

mod

```sh
python -m fname.py
```

> run library module as a script (terminates option list)

将python模块当作脚本运行，例如

```py
python -m SimpleHTTPServer    #python2中启动一个简单的http服务器
python -m http.server    #python3中启动一个简单的http服务器
```

但是我怎么感觉像是把脚本当作模块来运行呢？因为会改变 `__name__` 啊