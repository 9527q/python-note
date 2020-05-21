# 操作汇总

## 字符串格式化 f-string

F字符串（f-string）格式：`f"{expr}"`，Python3.6 引入，不仅更易读，更简洁，而且速度更快！使用的协议和 str.format() 相同。

%-formatting 和 str.format() 现在都属于旧时代的格式化方案了。[一篇总结：过去两种方案的局限以及 f-string 使用细致讲解](https://mlln.cn/2018/05/19/python3%20f-string格式化字符串的高级用法/)。[PEP 489](https://www.python.org/dev/peps/pep-0498/)关于 f-string 的所有东西。

- 更易读、更简介、更快
- 实时生成（可以封装一个函数来利用这一点）
- 大括号中不能为空
- 普通大括号字符转义格式：`{{`，`}}`

普通使用
```py
>>> a = 1
>>> f'{a}2'
'12'
>>> F'{a}2'
'12'
```

速度比较
```py
In [4]: %%timeit 
   ...: name = 'eric' 
   ...: age = 74 
   ...: '%s is %s.' % (name, age)                                                                      
202 ns ± 1.53 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [5]: %%timeit 
   ...: name = 'eric' 
   ...: age = 74 
   ...: '{} is {}.'.format(name, age)                                                                      
291 ns ± 0.87 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [6]: %%timeit 
   ...: name = 'eric' 
   ...: age = 74 
   ...: f'{name} is {age}.'                                                                  
153 ns ± 0.397 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```