# 数据类型

## str

有特殊声明的用空字符（\s）连接的多行字符串，特殊声明只对所在行有效；有特殊声明的使用三引号标志的字符串，特殊声明对全体内容有效

```py
name = 'Eric'
message = (f"Hi {name}. "
    "You are a {profession}. "
    "You were in {affiliation}.")

print(message)  # 没有报错，说明 f-string 没对后面两行起作用

# 结果
#
# Hi Eric. You are a {profession}. You were in {affiliation}.
```

