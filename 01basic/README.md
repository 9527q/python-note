# Python 基础

- [基本数据类型](./basic-data-type.md)
- [操作汇总](./op_summary.md)
- [内置函数](./build-in-method-class.md)
- [匿名函数](./anonymous-function.md)
- [类与对象](./class.md)
- [注意](./warn.md)

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


# 基础

## [注释](https://blog.csdn.net/lnotime/article/details/81841939)

## 变量赋值

### 一个等号可以用来给多个变量赋值

> 等号左右两边量的个数必须相同
1. 正好用来交换两个变量的值
    > 不使用第三个变量就交换两个变量的值还可以用求和取差法、求差相加法、求积取商法、求商相乘法，不过必须是数值类型，而且要注意各种运算对数值的影响。
2. 拆包用

### 多个变量赋同一个值

> 会指向同一个地址

```py
a = b = c = [1,2]
print(a is b is c)  # True
```

> `is`也可以连用

### 前两条混用

```py
a,b = c,d = [[1,2],[]]
print(a is c)  # True
```

### 自操作赋值

`+ - * / % // ** & | ^`都可以和`=`相连，中间不能有空格，自操作赋值不会改变可变类型的引用地址

> **运算**  
> 优先级：指数大于乘除模余大于加减  
> 有浮点数的运算则结果为浮点数(哪怕是取模)
> 除法结果为浮点数

## 标识符、关键字

### 标识符

- 开发人员在程序中自定义的符号和名称，变量名、函数名、类名等等
- 规则
  - 字母数字下划线，数字不开头
  - Python中区分大小写
  - 大驼峰、小驼峰、下划线
  - 不能与关键字重复
    - 不建议与内置变量函数等重复

### [关键字](https://blog.csdn.net/lnotime/article/details/81369933)

- `is`可以连用
- `and`前判断为True则运行后面并返回后面的值，前判断为False则不运行后面并返回前面的值
- `or`前判断为True则不运行后面并返回前面的值，前判断为False则运行后面并返回后面的值
- `in`可以判断range()
- `True`和`False`参与数值运算时分别被作为1和0处理
- `del`

  ```py
  del [5,6,7][0]  # 删除列表指定索引元素，会报IndexError
  del {'a':'a'}['a']  # 删除字典指定key的键值对，会报KeyError
  ```

  - 还有del()方法
- `for`

  ```py
  for 临时变量 in 可迭代对象:
      代码
  ```

  - 临时变量处可以拆包
  - 若临时变量无用，用`_`代替表示占位
  - 可迭代对象
    - 实现了__iter__方法的对象就是可迭代对象
        > 实现了__iter__和__next__方法的对象就是迭代器对象
- `if` 三元表达式
  - 优先级低于普通运算（类比列表推导式）

    ```py
    >>> False or 1 if 1==2 else 3
    3
    >>> 1 + 2 if 1==2 else 4
    4
    ```

- `else`还可以用在for、`while`后面，循环正常结束时运行（continue属于正常结束）。
  - 也可以用在try语句中，位置必须紧跟在最后一个except后面。except和else只有一个会执行。
- `nonlocal` 声明外层函数的变量
  - 不能用来声明全局变量(`global`)
  - 不限制几层的外层
  - 当且仅当修改变量的指向时才需要声明，如果没声明则是创建了同名的新局部变量
    > 虽然自操作的id不会变，但也算改变变量指向
- `try`、`except`、`finally`
  - 只有属于Exception下面的异常才能被`except Exception as e:`捕获，即Exception不能捕获所有异常
        > 异常的基类是BaseException，继承自object
        > > 下面有Exception、GeneratorExit、KeyboardInterrupt、SystemExit
        >
        > 只有是对应异常类或属于其下面的子类异常才能被对应的异常捕获
  - 如果异常没有被except捕获，那将正常抛出
  - 一个try后可以接多个except来分情况处理多种异常
  - 一个except可以通过元祖的格式捕获多种异常，也可以用`as`
  - 如果不是运行过程中出现的错误，而是编译为字节码时就出错（比如语法错误），那except是捕获不了的
  - try后面可以不接except直接接finally
    - 不过没有捕获的话发生异常会正常抛出，那这个try语句就没作用了，finally也不会运行
    - 此时不能加else，else只能加在最后一个except后面
- `raise`
  - 抛出异常，加括号可自定义异常信息
  - 可抛出自定义异常
  - 普通情况下必须接一个异常
  - 在except中raise后可以不加任何东西，表示抛出此except捕获到的异常
- `import`、`from`
  - [循环导包](https://blog.csdn.net/lnotime/article/details/81368739)
  - [关于`from . import xx`的用法](https://blog.csdn.net/lnotime/article/details/81257735)
  - 多个被导对象用逗号连接，各自使用as
  - from格式不能用来导入`模块.函数/变量`格式，可以用来导入模块
    > 导入搜索顺序
    >
    > 1. 当前目录  
    > 2. 如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。  
    > 3. 如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/  
    > 4. 模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。  

## 函数

定义了函数也不叫面向对象(面向过程:程序是由过程或仅仅是可重用代码的函数构建起来的;面向对象:程序是由数据和功能组合而成的对象构建起来的。)

### lambda

### 参数

- 参数名不要与全局变量名同名
- 不要使用可变类型默认参数，用None代替并在函数内使用`x = None or []`来赋初值。
- 尽量使用类型标注（包括输出的）
- 不定长参数(名字不是固定的) `*args`、`**kwargs`(必须最后)；

### 传引用

如果是可变类型，把id传进去，修改那块内存当然会影响原值，因为都指向同一地址。  
如果是不可变类型，把id传进去，被另一个变量接收到，修改值时相当于把变量的引用指向了新的id，当然不会影响原变量的指向。

## 类

### 基础

- 类名(大驼峰)、属性、方法3部分构成类
- object 是Python 里所有类的最顶级父类
- 实例方法的第一个参数self可以任意命名
- 自定义类的实例的属性可以动态创建
- 基类/父类、派生类/子类
- 类属性、实例属性
  - 类属性就是类对象所拥有的属性，它被所有类对象的实例对象所共有，在内存中只存在一个副本，通过实例或类对象都可以访问
  - 实例属性只能通过实例访问，每个实例都单独存放自己的实例属性，互相之间不影响
  - 如果定义与类属性同名的实例属性，只是影响本实例使用，不会影响其他实例，如果删除该同名实例属性，值又会变回原类属性的值
  - 如果修改类属性的值，则影响所有实例访问的值（包括在修改前就创建了的实例）
  - 不能通过实例删除类属性
- 类方法、@classmethod、cls（类对象）
  - 通过实例或类对象都可以访问
  - 可以对类属性进行修改（通过cls，当然实例方法通过 类名. 也能修改）
- 静态方法、@staticmethod
  - 类、实例均可访问

### 面向对象

三大特性：封装继承多态
> 封装的意义：
>
> 1. 将属性和方法放到一起做为一个整体，然后通过实例化对象来处理；
> 2. 隐藏内部实现细节，只需要和对象及其属性和方法交互就可以了；
> 3. 对类的属性和方法增加 访问权限控制。

> 多态
>
> 定义时的类型和运行时的类型不一样，此时就成为多态 ，多态的概念是应用于Java和C#这一类强类型语言中，而Python崇尚“鸭子类型”，弱化了多态的概念。
>
> Python的多态，就是弱化类型，重点在于对象参数是否有指定的属性和方法，如果有就认定合适，而不关心对象的类型是否正确。

### 私有

属性名和方法名前加两个下划线

1. 类的私有属性 和 私有方法，都不能通过对象直接访问，但是可以在本类内部访问；
2. 类的私有属性 和 私有方法，都不会被子类继承，子类也无法访问；
3. 私有属性 和 私有方法 往往用来处理类的内部事情，不通过对象处理，起到安全作用。

> 修改属性的值
>
> - 对象名.属性名 = 数据 ----> 直接修改
> - 对象名.方法名() ----> 间接修改  
>
> 私有属性只能通过第二种方式修改，即通过一个公有方法来修改

### 新式类经典类

1. 新式类和经典类是什么

> 在Python 2及以前的版本中，由任意内置类型派生出的类（只要一个内置类型位于类树的某个位置），都属于“新式类”，都会获得所有“新式类”的特性；反之，即不由任意内置类型派生出的类，则称之为“经典类”。  
> “新式类”和“经典类”的区分在Python 3之后就已经不存在，在Python 3.x之后的版本，因为所有的类都派生自内置类型object(即使没有显示的继承object类型)，即所有的类都是“新式类”。

1. 继承顺序的区别

> 经典类的继承是深度优先，即从下往上搜索；新式类的继承顺序是采用C3算法（非广度优先,只是在部分情况下，C3算法的结果恰巧与广度优先的结果相同）  
> 新式类中，可以使用类的`mro()`方法或`__mro__`属性来查看类的搜索顺序(这也算是一个区别)

1. 类实例类型的区别

> 在经典类中，所有的类都是classobj类型，而类的实例都是instance类型。类与实例只有通过__class__属性进行关联。这样在判断实例类型时，就会造成不便：所有的实例都是instance类型。
>
> ```py
> class A():pass
> class B():pass
>
> a = A()
> b = B()
>
> if __name__ == '__main__':
>     print(type(a))
>     print(type(b))
>     print(type(a) == type(b))
> ```

> type(a) == type(b)的结果永远为True，那这样的比较就毫无意义。  
> 更为麻烦的是，经典类的实例是instance类型，而内置类的实例却不是，无法统一。  
>
> 这个问题在Python 3之后就不复存在了，因为Python3中所有的类都是新式类，新式类中类与类型已经统一：类实例的类型是这个实例所创建自的类（通常是和类实例的__class__相同），而不再是Python 2.x版本中的“instance”实例类型。

### 魔法方法、常用方法、属性
- `__init__(self)`、`__del__(self)`、`__new__(cls, *args, **kwargs)`
    - init方法用来做属性初始化或赋值操作,创建一个对象时默认被调用，不需要手动调用,当需要时当然可以主动调用，比如迭代器同时作为存储数据的可迭代对象被迭代后的复原操作
    - del方法删除对象时（引用计数为0时）调用
    - new方法第一个参数是cls类对象，代表要实例化的类
        - 必须有返回值，一个实例化出的实例，返回给init进行初始化
        - 参数必须>=init参数
- `__str__(self)`、`__repr__(self)`
    - 只能接收self一个参数
    - 必须返回字符串格式(如果不，定义时不会报错，但是下面三个方法/类实例会报错)
    - print(实例)、str(实例)或repr(实例)时调用，这也是这三个转换或操作时的本质
    > print(类)、str(类)、repr(类)时返回`__name__的值.类名`，
- `mro()`、`__mro__`
    - mro()是方法，返回一个列表
    - __mro__是属性，返回一个元祖
- `__class__`
    - 一个变量，不是方法也不是属性
        - 只能在类里面使用，指向这个类（不因继承而改变，就指向代码所在的类）
    - 也是实例的一个属性，指向创建实例的类
- `__name__`
    - 只有类能调用的类属性（实例无法调用），值为类名:str
- `__doc__`
    - 说明文档，模块/类/函数/方法的开头的三引号内容，没有就是None
### 调用父类方法
- 父类类名.父类方法(self)
    - self其实是传入一个实例，因为定义类方法里面一般用self来表示当前实例。
    - 这其实就是通过类名访问方法（实例方法、类方法）
- super 
    - 调用遵循MRO顺序表，并且能判断当前在表中的哪个位置
    - 真实的是谁调用我我就用谁的MRO顺序表
    - Python2.3后才有
## __name__、__all__、__init__.py
### __name__
- 值为字符串格式
- __name__所在模块run时其值为`'__main__'`，常用做模块测试程序入口
- __name__所在模块被其他模块调用时，其值为import后的值
    - 如果被调用过程中有类似`from . import xx`格式，__name__的值为总的import的值。
        > [关于`from . import xx`的用法](https://blog.csdn.net/lnotime/article/details/81257735)
### __all__
- 不是本来就存在的变量，需要手动定义，赋值为一个列表，里面放入字符串格式的函数、变量、类名、包名、模块名
- 作用：
    - `from xx import *`格式只能导入__all__中指定的内容（仅对此种格式起作用，from xx import xx都不起作用）
    - 将__all__放到__init__.py文件中，使用from*格式导入时自动导入其指定好的模块（如果没有则from*格式不能导入包下的模块）
### __init__.py
- 用__all__控制from*格式的导入
- 当仅导入包名时，是不能用`包名.模块名.xx`来使用模块下内容的
    - Python2中需要在__init__.py中`import 模块名`
    - Python3中需要在__init__.py中`from . import 模块名`
# 设计模式
## 单例模式
> 单例：
> 
> 确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，这个类称为单例类，单例模式是一种对象创建型模式。

> 例：
> 
> 回收站

```py
class ClsName(object):
    __instance = None
    __is_first = True  # `类名()`会依次运行new和init，用is_first标识符来让init内容只初始化一次

    def __init__(self):
        if ClsName.__is_first:
            ClsName.__is_first = False
            print('初始化')  # 初始化操作

    def __new__(cls, *args, **kwargs):  # cls后面的参数应保证‘能包含’__init__的参数
        if not cls.__instance:
            cls.__instance = object.__new__(cls)  # object的new方法只接收一个参数
        return cls.__instance
```

# 与3的区别

## 对中文的支持

1. Python3使用utf-8编码，支持中文。Python2默认使用ASCII编码，不支持中文。
2. Python2应在程序开头加入

    ```py
    # -*- coding:utf-8 -*-
    ```

    或

    ```py
    #coding=utf-8
    ```

    这样即可支持中文。
3. windows的cmd中运行Python2即使加了上述注释也不能显示正确的中文。这是因为cmd默认使用gbk编码。使用命令修改cmd编码格式即可。
    - 转换为utf-8

        ```shell
        chcp 65001
        ```

    - 转换为默认的gbk

        ```shell
        chcp 936
        ```

## 输入

Python2中raw_input和3的input相同，2的input只能接收表达式并返回表达式的结果（类似eval）

## 没有<>

# 等待

如果要让程序等在一个地方直到某个条件出现，可以用while配合sleep，让CPU还能干别的事。

# 输入输出

[底层调用](https://blog.csdn.net/lnotime/article/details/81385646)

## input

- 接收最多一个str参数作为输入提示
- 返回输入的值，str格式
- 用户回车确认输入
- 还可以用来查看程序执行情况并手动控制程序执行

## print

- 多个任意格式参数间用逗号隔开，不传参直接打印空行
- `end`参数设置结尾，默认值为`\n`
- 打印对象其实就是先把对象转换成str格式再输出
  - 其实就是找对象的__str__（或__repr__（或直接返回对象本身））

---
---
  
# [eval()](https://blog.csdn.net/lnotime/article/details/81368293)、globals()、locals()

# len()、max()、min()、any()、all()

## len

- 接收可迭代对象参数
- 调用对象的__len__方法

```py
len(mydict)  # 键值对个数
```

## max、min

- 要保证元素可进行比较
- 传入一个参数（必须是可迭代对象）返回其中最大值
  - 可选key参数，当iterable为空时返回之(只能关键字传参)
- 如果传入多个参数，返回其中最大的一个

# range、filter、map、sorted

## range

- 能用in直接判断
- 可以索引取值

## filter

filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.

## sorted

可传关键字参数key、reverse(默认为False升序)

# enumerate、zip

## enumerate

enumerate(iterable[, start]) -> iterator for index, value of iterable

接收可迭代对象，返回一个enumerate对象，不可索引取值，每个元素是索引和对应值组成的元祖

```py
for i, v in enumerate('abc'):
    print(i, v)
```

## zip

zip(iter1 [,iter2 [...]]) --> zip object

Return a zip object whose `.__next__()` method returns a **tuple** where the i-th element comes from the i-th iterable argument.  The `.__next__()` method continues until the shortest iterable in the argument sequence is exhausted and then it raises StopIteration.

不能索引取值

# open()

打开文件，返回文件对象

```py
f = open('test.txt', 'r')
```

## 参数

- r:read,w:write,a:append
- b:byte
- +:增加读/写功能
访问模式 |说明
- | -
r | 只读；指针在开头；文件不存在则报错；默认模式
w | 只写；文件存在则覆盖，否则创建新文件
a | 追加；文件存在，指针在结尾；否则创建新文件
rb | 二进制格式只读
wb | 二进制格式只写
ab | 二进制格式追加
r+ | 读写
w+ | 读写
a+ | 读追加
rb+ | 二进制格式读写
wb+ | 二进制格式读写
ab+ | 二进制格式读追加

## write、read、readlines

- `f.write()`  
  - 根据打开类型传对应类型的参数
- `f.read()` 
  - 可传num参数，表示读取数据的长度（字节）
  - 不传参表示读所有数据
  - 从指针所在位置开始读
  - 读的过程中会移动指针
- `f.readlines()`
  - 返回一个列表，每个元素是一样的数据
- `f.readline()`
- `f.close()`

# help()、exit()、quit()

## help

help(o)第一部分就是o.__doc__的内容，如果没有，就到定义句前面去找#格式的注释，如果也没有，就是None。
