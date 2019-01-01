# string

格式化字符串：

```py
from string import Template
s = Template('There are ${key1} ${key2} Quotations Symbols')
print(s.substitute(key2='Python', key1=3))  # 'There are 3 Python Quotation Symbals'
print(s.substitute(key2='Python'))  # KeyError: 'key1'
print(s.safe_substitute(key2='Python'))  # 'There are ${key1} Python Quotations Symbols'
```