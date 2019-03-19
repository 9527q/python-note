# 注意

一些基础的小地方，可能自己认为的是对的，但当时是不敢确认的，要试一下才敢确认。
一些值得注意的小点，真的很小，但当时很急就是发现不了问题在哪。

## 运算优先级

指数运算 > 乘除

```py
>>> 9 ** 1/2
4.5
```

and/or > if-else

```py
>>> 3 or 0 if 0 else 2
2
```

> **对这种都是选择出不同结果的，怎么创建验证条件？**
>
> 每一个选择，都创建一个结果仅自己能接触到的条件。比如上面的or 和 if-else，就应该让or的结果是前面的，if-else的结果是后面的，这样当两者在一起时，就知道谁先起作用谁后起作用了。真的，想出这个例子费了我好几分钟。

if-else > 逗号

```py
>>> 1, 2 if 3 else 4, 5
(1, 2, 5)
```

## 奇怪的错误

### 明明看着没错误却报语法错误？

比如这个报错，猜猜可能是什么原因？

```py
  File "/Users/ikeliu/lyq/Python/P3/t3.py", line 3
    for i in range(lt):
      ^
SyntaxError: invalid syntax
```

其实代码是这样的

```py
lt = [1, 2, 3

for i in range(lt):
    print(i)
```

真正的原因是列表在定义的时候**少了一个右括号**，对于不熟练的人，找一个功能齐全的**开发环境**是不错的选择。

### 明明传的是一个值却得到了元祖？

比如这个例子为什么输出和预想不一样？

```py
>>> def add(n1, n2):
...     """n1 + n2"""
...     a = n1,
...     b = n2,
...     return a + b
...
>>> add(3, 4)
(3, 4)
```

其实是**多了一个逗号**，平常写代码的时候尽量避免小毛病、个人特殊风格

```py
>>> 'Oh',
('Oh',)
```

### 报错中出现了不存在的字符串？

```py
# 动词 --> 过去式
d = {'do': 'did', 'go': 'went', 'ride': 'rode', 'write': 'wrote',
     'fly': 'flew', 'break': 'broke', 'run': 'ran', 'eat': 'ate',
     'drink': 'drank', 'cut': 'cut'}
# 动词
ks = ['do', 'go', 'ride', 'write', 'fly'
      'break', 'run', 'eat', 'drink', 'cut']

for k in ks:
    print(k, d[k])

# 运行后报错
# Traceback (most recent call last):
#   File "/Users/ikeliu/lyq/Python/P3/t3.py", line 10, in <module>
#     print(k, d[k])
# KeyError: 'flybreak'
```

我是在配置 Django 的 admin 时，遇到这个错误，真是怎么看都没错，而且报错的 fieldname 是我根本就没有的。当时内容很长的 tuple 有好几个，精力都在不要多写不要缺少上了，整理换行的时候不小心就弄丢了一个逗号。**括号里多个字符串之间只有空字符时会被拼接成一个字符串**，这样真的好吗？

```py
a = ['hello ' 'world']
b = {'hello ' ''
     'world'}
c = {'hello '
     'world':3}

print(a, b, c)
# ['hello world'] {'hello world'} {'hello world': 3}
```