# Markdown

![markdown](images/Markdown.png)

Markdown 是一种轻量级标记语言，创始人为约翰·格鲁伯（John Gruber）。它允许人们“使用易读易写的纯文本格式编写文档，然后转换成有效的XHTML（或者HTML）文档”。Markdown 文档的后缀为 .md。

其实 Markdwon 就是指一种格式、一种标记，使用这种格式来编写纯文本文档，通过工具可以轻松的得到想要的样式。现在这个笔记就是通过编写 Markdown 文档再配合 gitbook 呈现出来的。

单纯的一个 Markdown 文档里面只是包含格式标记的文字而已，它必须和一个工具相配合才能展现其力量。现在很多的笔记软件（如印象、有道云）、博客网站（如CSDN、简书）、代码/文本编辑器（Pycharm、VS Code、Sublime）都直接支持或有插件支持编写、预览及导出 Markdown 格式文档。甚至有一些文本编辑器是专门用来编写 Markdown 文档的。

## 1. 准备一个支持 Markdown 的编辑器

使用任何支持 Markdown 的工具都可以，他们顶多有细微的差别。我平常使用的是 VS Code。安装成功后再安装相应的扩展。

![markdown_vscode](images/markdown_vscode.png)

- *Markdown All in One* 有很多 Markdown 编写过程中的实用功能（如各种快捷键）
- *Markdown Preview Enhanced* 是一个白色的 Markdown 预览插件，并且支持很多导出格式
- *markdownlint* 是一个 Markdown 语法检查工具
  > 只适合追求文档格式高标准的，因为不满足这些标准 Markdown 也照样正常工作
- 其他还有很多好用的扩展，可以点击扩展查看具体情况

新建一个 Markdown 文档，在其中右键选择 「Markdown Preview Enhanced: Open Preview」（Mac版快捷键为 `⌘K V`），就能实时查看渲染的结果。

## 2. Markdown 语法

Markdown 语法非常简单，几分钟就可以会用大部分语法。

### 2.1 标题

用 # 标记的是标题，会独占一行，文档中的写法和对应的样子：

```md
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```

# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题

### 2.2 横线

```md
---
```

---

### 2.3 字体

也可以 * 和 _ 配合使用实现 加粗斜体

```md
*斜体方式1*

_斜体方式2_

**加粗方式1**

__加粗方式2__

***加粗斜体1***

___加粗斜体2___
```

*斜体方式1*

_斜体方式2_

**加粗方式1**

__加粗方式2__

***加粗斜体1***

___加粗斜体2___

### 2.4 列表

#### 2.4.1 无序列表

```md
Markdown 的特性

- 轻量
  - 标记语法用量非常小
  - 为纯文本，不需要其他东西
- 易读
  - 原纯文本读起来不会有任何阻碍
  - 甚至更加清晰
- 易写
```

Markdown 的特性

- 轻量
  - 标记语法用量非常小
  - 为纯文本，不需要其他东西
- 易读
  - 原纯文本读起来不会有任何阻碍
  - 甚至更加清晰
- 易写

#### 2.4.2 有序列表

```md
编写 Markdown 文档过程

1. 准备支持 Markdown 的编辑器
   1. 搜索有道云笔记
   2. 下载并安装
   3. 新建 Markdown 格式笔记
2. 按照 Markdown 语法编写文档
   1. 敲呀敲键盘
3. 预览或导出为所需格式（htm、pdf等）
```

编写 Markdown 文档过程

1. 准备支持 Markdown 的编辑器
   1. 搜索有道云笔记
   2. 下载并安装
   3. 新建 Markdown 格式笔记
2. 按照 Markdown 语法编写文档
   1. 敲呀敲键盘
3. 预览或导出为所需格式（htm、pdf等）

#### 2.4.3 TODO 列表

```md
- [x] 起床
  - [x] 穿衣服
  - [ ] 洗漱
- [ ] 学习
- [x] 睡觉
```

![markdown_todolist](images/markdown_todolist.png)

### 2.5 引用

```md
> There is only one God, and his name is Death. And there is only one thing we say to Death: "Not today." ——*Game of Thrones*
```

> There is only one God, and his name is Death. And there is only one thing we say to Death: "Not today." ——*Game of Thrones*

#### 2.5.1 引用格式的妙用：包含关系

```md
> 人工智能
> > 机器学习
> > > 神经网络
> > > > 深度学习
```

> 人工智能
> > 机器学习
> > > 神经网络
> > > > 深度学习

### 2.6 代码

#### 2.6.1 使用缩进标记代码

*文档写法*：

```md
普通文字

    # Python 代码
    print('I am Groot.')

```

*渲染后*：

普通文字

    # Python 代码
    print('I am Groot.')

#### 2.6.2 ```

使用 `````` 和语言简称或全称标记代码

*文档写法*：

    ```py
    # Python 代码
    print('I am Groot.')
    ```

*渲染后*：

```py
# Python 代码
print('I am Groot.')
```

#### 2.6.3 ``

```md
查看系统运行情况的命令是 `top`
```

查看系统运行情况的命令是 `top`

### 2.7 链接和图片

```md
- [Markdown 百科](https://zh.wikipedia.org/wiki/Markdown)
- ![Markdwon 图标](images/Markdown.png)
```

- [Markdown 百科](https://zh.wikipedia.org/wiki/Markdown)
- ![Markdwon 图标](images/Markdown.png)

### 2.8 表格

```md
表头1 | 表头2 | 表头3 | 表头4
-|:-|:-:|-:
内容左对齐列 | 内容和表头左对齐列 | 内容和表头居中列 | 内容和表头右对齐列
*斜体* | **加粗** | [Markdown 百科](https://zh.wikipedia.org/wiki/Markdown)
**_加粗斜体_** | 这就是表格 | 表格内容 | ![Markdwon 图标](images/Markdown.png) | 表格内容
```

表头1 | 表头2 | 表头3 | 表头4
-|:-|:-:|-:
内容左对齐列 | 内容和表头左对齐列 | 内容和表头居中列 | 内容和表头右对齐列
*斜体* | **加粗** | [Markdown 百科](https://zh.wikipedia.org/wiki/Markdown)
**_加粗斜体_** | 这就是表格 | 表格内容 | ![Markdwon 图标](images/Markdown.png) | 表格内容

### 2.9 数学公式

### 2.10 流程图
