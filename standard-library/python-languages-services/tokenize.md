tokenize
========

> token: n. 象征；标志； adj. 作为标志的；
> -ize: suff. 使成...状态；使...化；
> tokenize：标识化；标记化；

`tokenize` 提供了“**对 Python 代码使用的**”词汇扫描器，是用 Python 实现的。扫描器可以给 Python 代码打上标记后返回，你可以看到每一个词或者字符是什么类型的。扫描器甚至将注释也单独标记，这样某些需要对代码进行特定风格展示的地方就很方便了。

为了简化标记流（token stream）的处理，所有的[运算符（Operators）](#operators)、[分隔符（Delimiters）](#delimiters) 和 `Ellipsis`（不是英文，就是 Python 中的一个变量，和省略号一样）都会被标记为
[OP](https://docs.python.org/zh-cn/3/library/token.html#token.OP)
（一个表示标识类型的常量）类型。具体的类型可以通过`tokenize.tokenize()` 返回的具名元祖对象的 `.exact_type` 属性查看。

`exact_type` 是一个 `@property` 修饰的方法，所以只有调用时才精确的查看到底是什么类型的文本，这样就简化了标记流的处理

## 标记的输入

主要的入口是一个生成器：

### tokenize.tokenize(readline)

生成器 `tokenize()` 需要一个参数：readline，它必须是一个可调用的对象，并且提供了与文件对象的 `io.IOBase.readline()` 相同的接口。每次调用这个函数，都应该返回一行字节类型的输入

生成器会生成有5个元素的具名元组，内容是：

- `type`：标记类型
- `string`：被标记的字符串
- `start`：一个整数组成的 2-元组：`(srow, scol)`，这个标记的开始位置的行和列。s：start；
- `end`：一个整数组成的 2-元组：`(erow, ecol)`，这个标记的结束为止的行和列。e：end；
- `line`：被标记的字符串所在的那一行，就是输入的那一行的内容

返回的具名元组还有一个额外的属性 `exact_type`，标识了类型为
[OP](https://docs.python.org/zh-cn/3/library/token.html#token.OP)
词的确切操作类型。对于所有
[OP](https://docs.python.org/zh-cn/3/library/token.html#token.OP)
以外的标记，`exact_type` 的值等于 `type` 的值。

`tokenize()` 通过查找 UTF-8 BOM 或者编码 cookie 来确认文件的源编码。

### tokenize.generate_tokens(readline)

将对 unicode 类型的字符串进行标记，而不是字节类型。

像
[tokenize()](#tokenize.tokenize(readline))
一样，readline 参数需要可调用，并且返回输入的一行，但是需要返回 str 对象，而不是 bytes。

返回的结果是一个迭代器，返回的具名元祖和 `tokenize()` 的完全一样。只不过没有 
[ENCODING](https://docs.python.org/zh-cn/3/library/token.html#token.ENCODING)
（一种表示标识类型的常量）类型的标记。（`tokenize()` 第一个返回的就是
[ENCODING](https://docs.python.org/zh-cn/3/library/token.html#token.ENCODING)
标记的内容）

[ENCODING](https://docs.python.org/zh-cn/3/library/token.html#token.ENCODING)
和
[OP](https://docs.python.org/zh-cn/3/library/token.html#token.OP)
一样是常量，还有很多，都是用来标记类型的，在 `tokenize` 库里直接用即可，是从 `token` 包里直接导过来的。

还有一个函数提供反转标记过程的功能。有些工具要标记化一个脚本、修改标记流、回写修改后的脚本，这个函数就能派上用场了。

### tokenize.untokenize(iterable)

把标记转装成 Python 源代码（指用 Python 写成的代码）。可迭代对象 iterable 返回的序列中每一个对象至少要有两个元素构成：标记类型和标记的字符串。其他的元素都会被忽略。

反转生成的脚本会作为一个单独的字符串返回。

返回的是字节类型的，使用
[ENCODING](https://docs.python.org/zh-cn/3/library/token.html#token.ENCODING)
标记的内容进行编码，如果输入中没有这个标记的，那就返回 str 类型的。

`tokenize()` 需要查出源文件的编码，它用于执行此操作的函数也是可用的：

### tokenize.detect_encoding(readline)

[detect_encoding()](#tokenize.detect_encoding(readline))
函数用来检测应该用于解码 Pyhton 源文件的编码。它需要一个参数 readline，和生成器
[tokenize()](#tokenize.tokenize(readline))
所需的相同

它最多会调用 `readline` 两次，然后返回要使用的编码（一个字符串）和它已读入的每一行（不是从字节解码的）组成的列表

它根据 PEP 263 中规定的方式从 UTF-8 BOM 或者编码 cookie 中检测编码方式。如果 BOM 和 cookie 都存在但不一致，会抛出 `SyntaxError`。如果找到 BOM，`'utf-8-sig'` 将作为编码返回。

如果没有指定编码，就返回默认的 `'utf-8'`。

使用
[open()](#tokenize.open(filename))
打开 Python 源文件：它使用
[detect_encoding()](#tokenize.detect_encoding(readline))
检测文件编码

### tokenize.open(filename)

使用
[detect_encoding()](#tokenize.detect_encoding(readline))
检测到的编码通过只读方式打开一个文件

### 异常：tokenize.TokenError

当一个文档字符串或表达式可能被分割成多行，但在文件中的任何地方都没能完成时抛出。

例如：

```py
"""文档字符串
开头
```

或者

```py
[
  1,
  2,
  3
```

注意：未关闭的单引号字符串不会引发错误。它们会被标记为
[ERRORTOKEN](https://docs.python.org/zh-cn/3/library/token.html#token.ERRORTOKEN)（一种标记类型常量）
，然后是其内容的标记化。

## 命令行用法

`tokenize` 包可以从命令行以脚本的形式执行。

```bash
python -m tokenize [-e] [filename.py]
```

有以下可选参数

### -h,&ensp;--help

展示帮助信息

### -e,&ensp;--exact

使用确切的类型展示标识类型

如果 `filename.py` 指定，它里面的内容就用作标记化，否则就在 stdin 获取输入。

## 示例

### 1、将浮点文字转换为 Decimal 对象的脚本重写器

```py
from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
from io import BytesIO

def decistmt(s):
    """用 Decimal 替换语句字符串中的浮点数。

    >>> from decimal import Decimal
    >>> s = 'print(+21.3e-5*-.1234/81.7)'
    >>> decistmt(s)
    "print (+Decimal ('21.3e-5')*-Decimal ('.1234')/Decimal ('81.7'))"

    在不同的平台，下面这句的结果可能不同。第一个是在 macOS，第二个是在 Win10。

    >>> exec(s)
    -3.21716034272e-07
    -3.217160342717258e-07

    在所有平台上，Decimal 的输出应该都是一致的。

    >>> exec(decistmt(s))
    -3.217160342717258261933904529E-7
    """
    result = []
    g = tokenize(BytesIO(s.encode('utf-8')).readline)  # 标记化字符串
    for toknum, tokval, _, _, _ in g:
        if toknum == NUMBER and '.' in tokval:  # 把数字类型的转换后保存
            result.extend([
                (NAME, 'Decimal'),
                (OP, '('),
                (STRING, repr(tokval)),
                (OP, ')')
            ])
        else:
            result.append((toknum, tokval))
    return untokenize(result).decode('utf-8')
```

### 2、使用命令行的例子

脚本：

```py
def say_hello():
    print("Hello, World!")

say_hello()
```
（文件内容就写上面这样，末尾没有空行）

会标记后输出为下面的样子，第一列是找到标记的范围，第二列是标记的类型名字，第三列是被标记的词（输入的值）

```bash
$ python -m tokenize hello.py
0,0-0,0:            ENCODING       'utf-8'
1,0-1,3:            NAME           'def'
1,4-1,13:           NAME           'say_hello'
1,13-1,14:          OP             '('
1,14-1,15:          OP             ')'
1,15-1,16:          OP             ':'
1,16-1,17:          NEWLINE        '\n'
2,0-2,4:            INDENT         '    '
2,4-2,9:            NAME           'print'
2,9-2,10:           OP             '('
2,10-2,25:          STRING         '"Hello, World!"'
2,25-2,26:          OP             ')'
2,26-2,27:          NEWLINE        '\n'
3,0-3,1:            NL             '\n'
4,0-4,0:            DEDENT         ''
4,0-4,9:            NAME           'say_hello'
4,9-4,10:           OP             '('
4,10-4,11:          OP             ')'
4,11-4,12:          NEWLINE        '\n'
5,0-5,0:            ENDMARKER      ''
```

可以使用 [-e](#-e,&ensp;--exact) 来显示确切标识名称

```bash
$ python -m tokenize -e hello.py
0,0-0,0:            ENCODING       'utf-8'
1,0-1,3:            NAME           'def'
1,4-1,13:           NAME           'say_hello'
1,13-1,14:          LPAR           '('
1,14-1,15:          RPAR           ')'
1,15-1,16:          COLON          ':'
1,16-1,17:          NEWLINE        '\n'
2,0-2,4:            INDENT         '    '
2,4-2,9:            NAME           'print'
2,9-2,10:           LPAR           '('
2,10-2,25:          STRING         '"Hello, World!"'
2,25-2,26:          RPAR           ')'
2,26-2,27:          NEWLINE        '\n'
3,0-3,1:            NL             '\n'
4,0-4,0:            DEDENT         ''
4,0-4,9:            NAME           'say_hello'
4,9-4,10:           LPAR           '('
4,10-4,11:          RPAR           ')'
4,11-4,12:          NEWLINE        '\n'
5,0-5,0:            ENDMARKER      ''
```

### 3、以编程方式标记文件的例子

1、用
[generate_tokens()](#tokenize.generate_tokens(readline))
读取 unicode 字符串而不是字节类型的。

```py
import tokenize

with tokenize.open('hello.py') as f:
    tokens = tokenize.generate_tokens(f.readline)
    for token in tokens:
        print(token)
```

结果如下，可见用
[generate_tokens()](#tokenize.generate_tokens(readline))
是得不到
[ENCODING](https://docs.python.org/zh-cn/3/library/token.html#token.ENCODING)
的

```py
TokenInfo(type=1 (NAME), string='def', start=(1, 0), end=(1, 3), line='def say_hello():\n')
TokenInfo(type=1 (NAME), string='say_hello', start=(1, 4), end=(1, 13), line='def say_hello():\n')
TokenInfo(type=54 (OP), string='(', start=(1, 13), end=(1, 14), line='def say_hello():\n')
TokenInfo(type=54 (OP), string=')', start=(1, 14), end=(1, 15), line='def say_hello():\n')
TokenInfo(type=54 (OP), string=':', start=(1, 15), end=(1, 16), line='def say_hello():\n')
TokenInfo(type=4 (NEWLINE), string='\n', start=(1, 16), end=(1, 17), line='def say_hello():\n')
TokenInfo(type=5 (INDENT), string='    ', start=(2, 0), end=(2, 4), line='    print("Hello, World!")\n')
TokenInfo(type=1 (NAME), string='print', start=(2, 4), end=(2, 9), line='    print("Hello, World!")\n')
TokenInfo(type=54 (OP), string='(', start=(2, 9), end=(2, 10), line='    print("Hello, World!")\n')
TokenInfo(type=3 (STRING), string='"Hello, World!"', start=(2, 10), end=(2, 25), line='    print("Hello, World!")\n')
TokenInfo(type=54 (OP), string=')', start=(2, 25), end=(2, 26), line='    print("Hello, World!")\n')
TokenInfo(type=4 (NEWLINE), string='\n', start=(2, 26), end=(2, 27), line='    print("Hello, World!")\n')
TokenInfo(type=61 (NL), string='\n', start=(3, 0), end=(3, 1), line='\n')
TokenInfo(type=6 (DEDENT), string='', start=(4, 0), end=(4, 0), line='say_hello()')
TokenInfo(type=1 (NAME), string='say_hello', start=(4, 0), end=(4, 9), line='say_hello()')
TokenInfo(type=54 (OP), string='(', start=(4, 9), end=(4, 10), line='say_hello()')
TokenInfo(type=54 (OP), string=')', start=(4, 10), end=(4, 11), line='say_hello()')
TokenInfo(type=4 (NEWLINE), string='', start=(4, 11), end=(4, 12), line='')
TokenInfo(type=0 (ENDMARKER), string='', start=(5, 0), end=(5, 0), line='')
```

2、或者直接使用 tokenize() 读取字节类型的：

```py
import tokenize

with open('hello.py', 'rb') as f:
    tokens = tokenize.tokenize(f.readline)
    for token in tokens:
        print(token)
```

标记化的结果与
[例2](#2、使用命令行的例子)
中一致，只是多了一些信息。

## 附表

### [所有的标记类型](https://docs.python.org/zh-cn/3/library/token.html#token.ENCODING)

### Operators

以下形符属于运算符：

```py
+       -       *       **      /       //      %       @
<<      >>      &       |       ^       ~       :=
<       >       <=      >=      ==      !=
```

### Delimiters

以下形符在语法中归类为分隔符：

```py
(       )       [       ]       {       }
,       :       .       ;       @       =       ->
+=      -=      *=      /=      //=     %=      @=
&=      |=      ^=      >>=     <<=     **=
```

句点也可出现于浮点数和虚数字面值中。连续三个句点有表示一个省略符的特殊含义。以上列表的后半部分为增强赋值操作符，在词法中作为分隔符，但也起到运算作用。

以下可打印 ASCII 字符作为其他形符的组成部分时具有特殊含义，或是对词法分析器有重要意义：

```py
'       "       #       \
```
