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
# str、bytes、int、float、complex、bool
## str
- 字符串，不可变类型，长度不超过20的两个相同字符串变量会被Python内存优化指向同一地址
- `str(obj)`可以把对象转换成str格式，调用__str__（若没有则调用__repr__（若没有则返回对象））
- 与另一字符串比较大小时，依次比较每一个字符编码值的大小
    - 无小于有
    - 只能与字符串比较大小，否则报错
        - 不同类型判断==或!=不会报错

> **其他类似转换**
> - `repr(x)` 函数类似，不过从__repr__方法开始调用
> - `chr(x)` 将整数转换为Unicode字符
> - `ord(x)` 将一个字符转换为Unicode中所对应的整数(十进制整数)
### 格式化
格式符号 | 转换
- | -
%c | 一个字符(或整型数字，表示对应的Unicode字符，范围是range(0x110000)即0x0000至0x10FFFF，超出则报错)
%s | 字符串(会把其他任意格式的值转为字符串，会调用__str__方法，若没有则调用__repr__方法，若没有则返回对象)
%r | 调用__repr__方法，若没有则返回对象
%d | 有符号十进制整数，`%+d`可以转换正负值,`%nd`长度至少为n用空补齐可以更长,`%0nd`长度至少为n用0补齐
%u | 无符号十进制整数(与c语言对应罢了，python里都是d)，%i相同
%o | 八进制整数
%x | 十六进制整数（小写字母0x）
%X | 十六进制整数（大写字母0X）(字母变成大写)
%f | 浮点数，保留6位小数,`%.nf`保留n位小数
%e | 科学计数法（小写'e'），保留6位有效数字，即小数第6位为进位后的结果
%E | 科学计数法（大写“E”），保留6位有效数字，即小数第6位为进位后的结果
%g | 根据值的大小采用%e或%f，但最多保留6位有效数字
%G | 根据值的大小采用%e或%f，但最多保留6位有效数字

- 多个%后面传值时用`()`括起来，如果是一个值但是是一个操作也要括起来
- 八进制、十六进制、浮点数、科学计数法等都会把输入的数值转换成对应格式后再拼接到字符串中
- 八进制、十六进制不会带有格式标识符，用#可设置带有标识符
    ```py
    print('%#X' % 108)  # 0X6C
    ``` 
- 如果想要格式化的字符串中想要显示%，则`%%`即可，互相对应时会略过。
- %和标识字符之间可以加一个括号，后面传值时可用字典，键为括号中的内容。
- 字符串引号前加r可以禁用转义
- 还可以使用string模块的Template实现格式化输出
### 常见转义
- `\n`
- `\r` http处要写全\r\n
### 操作
- 运算：str之间可以相加，str与整形之间可以相乘（乘以非正整数得一个空格）
- 下标取值和切片
    - 切片：起始、结束、步长，左闭右开
        - 步长默认为1
        - 步长方向与起始→结束不同时返回空
        - 不在范围内时返回空（那个位置没有，切了个蛋，当然返回空）
    - 反转字符串`s[::-1]`（list、tuple也可）
### 常用方法
都能用位置参数传参
- find、rfind: 
    - `mystr.find(str, start=0, end=len(mystr))`
    - 返回开始的索引值，否则返回-1
    - 字符串参数可以长度大于1
    - 左闭右开，必须全包含才行
- index、rindex: 
    - `mystr.index(str, start=0, end=len(mystr)) `
    - 否则返回异常
    - 字符串参数可以长度大于1
    - 左闭右开，必须全包含才行
- count: 
    - `mystr.count(str, start=0, end=len(mystr))`
    - 左闭右开，必须全包含才行
- replace: 
    - `mystr.replace(str1, str2,  mystr.count(str1))`
    - 第三个参数表示换多少个
- split、splitlines
    - `mystr.split(str=" ", 2)`
    - split默认以空（空格、\t、\n、\r）分隔
    - splitlines以\n和\r分隔
        - 紧挨的\n\r、\n\n或\r\r之间也会分出一个空行''来
- capitalize、title、lower、upper
- startswith、endswith
- ljust、rjust、center
    - `mystr.ljust(width, fillchar=None)`
    - center左边<=右边
- lstrip、rstrip、strip
    - 各种空
- partition、rpartition
    - 按照给定字符串分割原字符串得到三元素元祖
    - 若给定字符串不在其中，则返回('str','','')或('','','str')
- isalpha、isdigit、isalnum、isspace
- join
    - 接收可迭代对象参数，元素必须也是str
- encode序列化
    - `mystr.encode(encoding="utf-8", errors="strict")`
    - 返回bytes类型
    - errors参数规定错误处理方案，'strict'表示encoding错误就报错，另外还有ignore、replace等
## bytes
### 方法
- decode反序列化
    - `mybytes.decode(encoding="utf-8", errors="strict")`
    - 返回str类型
## int
- 整型，不可变类型，-5~256存在小整数池中。相同值会被内存优化到同一地址。
- `int(obj)`可以把数值(也可以是2816进制)或字符串(内容是数值)转换成整型
    - 正负数都是去掉小数部分（向0靠近）
    - `int(str,base)`可以把有/没有进制标识符的base进制整数的字符串转换成10进制

> **其他类似转换**
> - `hex(x)` 将10进制整数转换成16进制字符串
> - `oct(x)` 将10进制整数转换成8进制字符串
> - `bin(x)` 将10进制整数转换为一个二进制字符串

> **其他**
> 
> Python中其他格式只要标明标识符即可直接当做数值编写程序，不过会被自动转换成10进制
> 
> Python程序中的数值中可以有下划线，阅读清晰（比如十进制的3位一顿，或2进制4位一顿）
## float
- 浮点型，不可变类型，会被内存优化。
- 受限于计算机的二进制本质，浮点数并不精确
## complex
- 复数`complex(real [,imag])`
    - 如果没有虚部可以不写第二个参数
    - 如果直接给一个内容为虚数的字符串，则不能给第二个参数
        - 字符串中的加减号两边不能有空格
- 可进行正常复数运算
- 直接给变量赋值`1 + 2j`也可以创建复数（大小写j均可）

### 操作
```py
a = complex(3,3)
print(a.real)  # 3.0 实部，总是浮点数
print(a.imag)  # 3.0 虚部，总是浮点数
print(a.conjugate())  # a的共轭复数
print(a)  # (3+3j) 注意带括号,所以字符串格式化时也会带有括号
print(abs(a))  # 复数的模
```



---
---
## bool
只有True和False是bool类型，别的都不是
# list
- 与另一以列表判断大小时，依次比较每个元素的大小
    - 无元素小于有元素
    - 只能同列表比较大小，否则报错
        - 不同类型判断==或!=不会报错
    > 元祖类似
- `list()`接收字符串参数则每个字符作为列表的一个元素
    - 接收字典参数得到keys列表
## 操作
### 切片、索引
### 运算操作
- `+`
    - 仅限列表之间
- `*`
    - 只能乘整数
    - 乘以非正整数得空列表
### 列表推导式
多个for左边的级别高
### 判断in
- in
- `mylist.__contains__(o)` --> True/False
## 方法
- append、extend、insert
    - insert把原有元素向后移动
- index、count
    - index可以接收start和end参数，左闭右开
        - 不存在则报错
    - count只能接收一个参数（与str的count不同）
- pop、remove、clear
    - pop默认删除最后一个，可传索引参数，会报错
    - remove传元素参数，会报错
- sort、reverse
    - sort默认由小到大排序
        - reverse=True则由大到小
        - key参数传一个函数，传入列表每个元素，返回自定义的比较值
        - 操作原列表
    - reverse()方法将列表倒置
        - 操作原列表
---
---
# tuple
不可变类型，元素不可修改，如果元素是可变类型，则元素内部可修改
## 定义
```py
a = tuple(1)
a = (1,)  # 逗号，这句最少一个值
```
## 操作
- 切片和索引
    - 切片返回的是元祖
- `+`
    - 仅限列表之间
- `*`
    - 只能乘整数
    - 乘以非正整数得空列表
- 比较大小同列表
## 方法
- count、index
    - 同list
# set
## 定义
```py
a = set()
a = {1,}  # 逗号，这句最少一个值，不能没有值{,}
```
## 操作
- 只能与另一集合比较大小
    - 包含时大于为True（或被包含的小于）
    - 不相同时!=为True
    - 其余均为False
- 集合之间的运算符有`& | ^ -`
    - 减法为去掉重复部分
- 可判断in
## 方法
- add、update
    - update拆分可迭代对象再加入到集合中
- remove、pop、discard、clear
    - remove删除指定元素，会报错
    - pop随机删除，会报错，不能传参
    - discard删除指定元素，不会报错



---
---
# dict
字典
- 不能比较大小
- [键必须是不可变类型](https://blog.csdn.net/lnotime/article/details/81192207)
## 操作
- in判断的是键
- 通过`字典[键]`来增改查
    - 查的时候如果没有这个键会报错
- 没有可用的运算法则
## 方法
- get
    - 存在则返回值，不存在则返回None
- clear
- keys、values、items、
    - 返回dict_keys等类型，不能用索引取值，打印与列表长相一样
    - items中元素是元祖类型
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