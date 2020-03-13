匿名函数
=======

### 语法

```py
lambda 参数列表: 表达式
```

### 说明

1. lambda 是python关键字
2. 匿名函数就是指没有名字的函数
3. 匿名函数冒号后面的表达式必须有，且只能有一个，注意：是表达式，不是语句
4. 匿名函数自带 return，就是 return 表达式计算的结果，表达式计算结果是1，就返回1，是None，就返回None

### 匿名函数调用

1. 将创建好的匿名函数用一个变量接收
2. 使用变量去调用

### 举例

```py
# 创建一个匿名函数，作用是实现两个数相加
add_2 = lambda num1, num2: num1 + num2
# 调用匿名函数
add_2(1, 3)  # 会得到4
```

### 匿名函数的参数

可以没有参数
```py
# 返回 ‘刘宇琪’ 字符串的匿名函数
func = lambda : '刘宇琪'
```

也可以有一个，也可以有多个（上面那个相加函数）

```py
# 求一个数的相反数
func = lambda num : num * -1
```

也可以有默认参数
```py
# 默认计算一个数加2，如果给了b就返回a+b
func = lambda a, b=2: a + b
```

总之，所有普通函数能实现的参数格式，都可以用在匿名函数上面

### 实际应用举例

如果一个地方不关注函数的名字，不关注其说明文档，内容很简洁短小，且这个函数只有这一个地方会用到，那么就应该使用匿名函数。

举两个例子

1. `map` 有时会和 `lambda` 一起使用。有时候 `map` 要进行的处理是比较简单且只有在这一个地方会用到的，那 `lambda` 在这里就是很好的使用情况。

假设有一个 `List[int]` 格式的列表，想求每一个数的倒数，就可以使用匿名函数配合 `map` 来完成

```py
list_num = [1, 2, 3, 0, 4, 5, -1]
iter_nums_inverse = map(lambda n: 1/n if n else None, list_num)

print(list(iter_nums_inverse))  # ==> [1.0, 0.5, 0.3333333333333333, None, 0.25, 0.2, -1.0]
```

2. 定义一个 `defaultdict` 的时候经常用到。因为默认值字典需要给一个可调用的初始值，Python 自带的类型有时是不能满足需要的，那 `lambda` 在这里就很方便了。

假设图像上有几个关键点，需要把他们的坐标用字典存储，如果没给定默认为 `(0, 0)`，那么用两者配合就很好完成了

```py
from collections import defaultdict

dict_point = defaultdict(lambda : (0, 0))

dict_point['X'] = (2, 5)
print(dict_point['X'])  # ==> (2, 5)
print(dict_point['Y'])  # ==> (0, 0)
print(dict_point['Z'])  # ==> (0, 0)
```
