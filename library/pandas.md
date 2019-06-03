# [![pandas](images/pandas_logo.png)](http://pandas.pydata.org/)

Python Data Analysis Library

> pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

```py
import numpy as np  # 一般都会用到 numpy 库
import pandas as pd

# 1. 导入文件、数据（3种方式，最后得到的都是 DataFrame 类型的数据对象）
df = pd.read_csv('filename.csv', header=0)  # header 可以指定标题行
# df = pd.read_excel('filename.xlsX')
# df = pd.DataFrame(数据)

```