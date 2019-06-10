# [![pandas](images/pandas_logo.png)](http://pandas.pydata.org/)

Python Data Analysis Library

> *pandas* is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

对数据的操作都是创建新数据，而不是在原有数据上操作

## 1. 导入库、数据


```python
import pandas as pd
import numpy as np  # 一般都会用到 numpy 库
```


```python
# df = pd.read_csv('query.csv', header=0)  # header 可以指定标题行
# df = pd.read_excel('query.csv')
df = pd.DataFrame(
    {
        "id": [1001, 1002, 1003, 1004, 1005, 1006], 
        "date": pd.date_range('20130102', periods=6),
        "city": ['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
        "age": [23, 44, 54, 32, 34, 32],
        "category":['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
        "price":[1200, np.nan, 2133, 5433, np.nan, 4432]
    },
    columns = ['id', 'date', 'city', 'category', 'age', 'price'])
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>city</th>
      <th>category</th>
      <th>age</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>2013-01-02</td>
      <td>Beijing</td>
      <td>100-A</td>
      <td>23</td>
      <td>1200.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>2013-01-03</td>
      <td>SH</td>
      <td>100-B</td>
      <td>44</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>2013-01-04</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
      <td>2133.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>2013-01-05</td>
      <td>Shenzhen</td>
      <td>110-C</td>
      <td>32</td>
      <td>5433.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>2013-01-06</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1006</td>
      <td>2013-01-07</td>
      <td>BEIJING</td>
      <td>130-F</td>
      <td>32</td>
      <td>4432.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
type(df)
```




    pandas.core.frame.DataFrame



## 2. 查看基本信息


```python
df.shape  # 维度
```




    (6, 6)




```python
df.info()  # 数据表基本信息（维度、列名称、数据格式、所占空间等）
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 6 entries, 0 to 5
    Data columns (total 6 columns):
    id          6 non-null int64
    date        6 non-null datetime64[ns]
    city        6 non-null object
    category    6 non-null object
    age         6 non-null int64
    price       4 non-null float64
    dtypes: datetime64[ns](1), float64(1), int64(2), object(2)
    memory usage: 368.0+ bytes



```python
df.dtypes  # 每一列数据的格式
```




    id                   int64
    date        datetime64[ns]
    city                object
    category            object
    age                  int64
    price              float64
    dtype: object




```python
df['city'].dtype  # 某一列格式
```




    dtype('O')




```python
df.isnull()  # 是否是空值
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>city</th>
      <th>category</th>
      <th>age</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['price'].isnull()  # 具体某一列是否是空值
```




    0    False
    1     True
    2    False
    3    False
    4     True
    5    False
    Name: price, dtype: bool




```python
df['category'].unique()  # 某一列的唯一值
```




    array(['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'], dtype=object)




```python
df.values  # 整个数据表的值
```




    array([[1001, Timestamp('2013-01-02 00:00:00'), 'Beijing ', '100-A', 23,
            1200.0],
           [1002, Timestamp('2013-01-03 00:00:00'), 'SH', '100-B', 44, nan],
           [1003, Timestamp('2013-01-04 00:00:00'), ' guangzhou ', '110-A',
            54, 2133.0],
           [1004, Timestamp('2013-01-05 00:00:00'), 'Shenzhen', '110-C', 32,
            5433.0],
           [1005, Timestamp('2013-01-06 00:00:00'), 'shanghai', '210-A', 34,
            nan],
           [1006, Timestamp('2013-01-07 00:00:00'), 'BEIJING ', '130-F', 32,
            4432.0]], dtype=object)




```python
df.columns  # 所有列名
```




    Index(['id', 'date', 'city', 'category', 'age', 'price'], dtype='object')




```python
df.head(3)  # 前 3 行数据，默认 n=5
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>city</th>
      <th>category</th>
      <th>age</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>2013-01-02</td>
      <td>Beijing</td>
      <td>100-A</td>
      <td>23</td>
      <td>1200.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>2013-01-03</td>
      <td>SH</td>
      <td>100-B</td>
      <td>44</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>2013-01-04</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
      <td>2133.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail(n=3)  # 后10行数据，默认 n=5
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>city</th>
      <th>category</th>
      <th>age</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>2013-01-05</td>
      <td>Shenzhen</td>
      <td>110-C</td>
      <td>32</td>
      <td>5433.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>2013-01-06</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1006</td>
      <td>2013-01-07</td>
      <td>BEIJING</td>
      <td>130-F</td>
      <td>32</td>
      <td>4432.0</td>
    </tr>
  </tbody>
</table>
</div>



## 3. 数据清洗


```python
df.fillna(value=80)  # 用 80 填充空值
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>city</th>
      <th>category</th>
      <th>age</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>2013-01-02</td>
      <td>Beijing</td>
      <td>100-A</td>
      <td>23</td>
      <td>1200.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>2013-01-03</td>
      <td>SH</td>
      <td>100-B</td>
      <td>44</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>2013-01-04</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
      <td>2133.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>2013-01-05</td>
      <td>Shenzhen</td>
      <td>110-C</td>
      <td>32</td>
      <td>5433.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>2013-01-06</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1006</td>
      <td>2013-01-07</td>
      <td>BEIJING</td>
      <td>130-F</td>
      <td>32</td>
      <td>4432.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['price'] = df['price'].fillna(df['price'].mean())  # 使用列 price 的均值对NA进行填充
df['price']
```




    0    1200.0
    1    3299.5
    2    2133.0
    3    5433.0
    4    3299.5
    5    4432.0
    Name: price, dtype: float64




```python
df['city'] = df['city'].map(str.strip)  # 去除city字段的字符空格
df['city']
```




    0      Beijing
    1           SH
    2    guangzhou
    3     Shenzhen
    4     shanghai
    5      BEIJING
    Name: city, dtype: object




```python
df['city'] = df['city'].str.lower()  # 大小写转换
df['city']
```




    0      beijing
    1           sh
    2    guangzhou
    3     shenzhen
    4     shanghai
    5      beijing
    Name: city, dtype: object




```python
df['price'] = df['price'].astype('int')  # 更改数据格式
df['price'].dtype
```




    dtype('int64')




```python
df = df.rename(columns={'category': 'category-size'}) # 更改列名
df.columns
```




    Index(['id', 'date', 'city', 'category-size', 'age', 'price'], dtype='object')




```python
df['city'].drop_duplicates(keep='last')  # 删除先出现的重复值
```




    1           sh
    2    guangzhou
    3     shenzhen
    4     shanghai
    5      beijing
    Name: city, dtype: object




```python
df['city'].replace('sh', 'shanghai')
```




    0      beijing
    1     shanghai
    2    guangzhou
    3     shenzhen
    4     shanghai
    5      beijing
    Name: city, dtype: object



## 4. 数据预处理


```python
df1 = pd.DataFrame({
    "id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008], 
    "gender": ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],
    "pay": ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y'],
    "m-point": [10, 12, 20, 40, 40, 40,  30,20]
})
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>male</td>
      <td>Y</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>female</td>
      <td>N</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>male</td>
      <td>Y</td>
      <td>20</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1006</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1007</td>
      <td>male</td>
      <td>N</td>
      <td>30</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1008</td>
      <td>female</td>
      <td>Y</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_inner = pd.merge(df, df1, how='inner')  # 交集
df_inner
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>2013-01-02</td>
      <td>beijing</td>
      <td>100-A</td>
      <td>23</td>
      <td>1200</td>
      <td>male</td>
      <td>Y</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>2013-01-03</td>
      <td>sh</td>
      <td>100-B</td>
      <td>44</td>
      <td>3299</td>
      <td>female</td>
      <td>N</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>2013-01-04</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
      <td>2133</td>
      <td>male</td>
      <td>Y</td>
      <td>20</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>2013-01-05</td>
      <td>shenzhen</td>
      <td>110-C</td>
      <td>32</td>
      <td>5433</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>2013-01-06</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>3299</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1006</td>
      <td>2013-01-07</td>
      <td>beijing</td>
      <td>130-F</td>
      <td>32</td>
      <td>4432</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_left = pd.merge(df, df1, how='left')  # 左连接
df_left
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>2013-01-02</td>
      <td>beijing</td>
      <td>100-A</td>
      <td>23</td>
      <td>1200</td>
      <td>male</td>
      <td>Y</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>2013-01-03</td>
      <td>sh</td>
      <td>100-B</td>
      <td>44</td>
      <td>3299</td>
      <td>female</td>
      <td>N</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>2013-01-04</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
      <td>2133</td>
      <td>male</td>
      <td>Y</td>
      <td>20</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>2013-01-05</td>
      <td>shenzhen</td>
      <td>110-C</td>
      <td>32</td>
      <td>5433</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>2013-01-06</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>3299</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1006</td>
      <td>2013-01-07</td>
      <td>beijing</td>
      <td>130-F</td>
      <td>32</td>
      <td>4432</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_right = pd.merge(df, df1, how='right')  # 右连接
df_right
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>2013-01-02</td>
      <td>beijing</td>
      <td>100-A</td>
      <td>23.0</td>
      <td>1200.0</td>
      <td>male</td>
      <td>Y</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>2013-01-03</td>
      <td>sh</td>
      <td>100-B</td>
      <td>44.0</td>
      <td>3299.0</td>
      <td>female</td>
      <td>N</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>2013-01-04</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54.0</td>
      <td>2133.0</td>
      <td>male</td>
      <td>Y</td>
      <td>20</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>2013-01-05</td>
      <td>shenzhen</td>
      <td>110-C</td>
      <td>32.0</td>
      <td>5433.0</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>2013-01-06</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34.0</td>
      <td>3299.0</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1006</td>
      <td>2013-01-07</td>
      <td>beijing</td>
      <td>130-F</td>
      <td>32.0</td>
      <td>4432.0</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1007</td>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>male</td>
      <td>N</td>
      <td>30</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1008</td>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>female</td>
      <td>Y</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_outer = pd.merge(df, df1, how='outer')  # 外链接
df_outer
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>2013-01-02</td>
      <td>beijing</td>
      <td>100-A</td>
      <td>23.0</td>
      <td>1200.0</td>
      <td>male</td>
      <td>Y</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>2013-01-03</td>
      <td>sh</td>
      <td>100-B</td>
      <td>44.0</td>
      <td>3299.0</td>
      <td>female</td>
      <td>N</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>2013-01-04</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54.0</td>
      <td>2133.0</td>
      <td>male</td>
      <td>Y</td>
      <td>20</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>2013-01-05</td>
      <td>shenzhen</td>
      <td>110-C</td>
      <td>32.0</td>
      <td>5433.0</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>2013-01-06</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34.0</td>
      <td>3299.0</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1006</td>
      <td>2013-01-07</td>
      <td>beijing</td>
      <td>130-F</td>
      <td>32.0</td>
      <td>4432.0</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1007</td>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>male</td>
      <td>N</td>
      <td>30</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1008</td>
      <td>NaT</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>female</td>
      <td>Y</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_inner.set_index('id')  # 设置索引列
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1001</th>
      <td>2013-01-02</td>
      <td>beijing</td>
      <td>100-A</td>
      <td>23</td>
      <td>1200</td>
      <td>male</td>
      <td>Y</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1002</th>
      <td>2013-01-03</td>
      <td>sh</td>
      <td>100-B</td>
      <td>44</td>
      <td>3299</td>
      <td>female</td>
      <td>N</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1003</th>
      <td>2013-01-04</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
      <td>2133</td>
      <td>male</td>
      <td>Y</td>
      <td>20</td>
    </tr>
    <tr>
      <th>1004</th>
      <td>2013-01-05</td>
      <td>shenzhen</td>
      <td>110-C</td>
      <td>32</td>
      <td>5433</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
    </tr>
    <tr>
      <th>1005</th>
      <td>2013-01-06</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>3299</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
    </tr>
    <tr>
      <th>1006</th>
      <td>2013-01-07</td>
      <td>beijing</td>
      <td>130-F</td>
      <td>32</td>
      <td>4432</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_inner.sort_values(by=['age'])  # 按照特定列的值排序
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>2013-01-02</td>
      <td>beijing</td>
      <td>100-A</td>
      <td>23</td>
      <td>1200</td>
      <td>male</td>
      <td>Y</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>2013-01-05</td>
      <td>shenzhen</td>
      <td>110-C</td>
      <td>32</td>
      <td>5433</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1006</td>
      <td>2013-01-07</td>
      <td>beijing</td>
      <td>130-F</td>
      <td>32</td>
      <td>4432</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>2013-01-06</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>3299</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>2013-01-03</td>
      <td>sh</td>
      <td>100-B</td>
      <td>44</td>
      <td>3299</td>
      <td>female</td>
      <td>N</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>2013-01-04</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
      <td>2133</td>
      <td>male</td>
      <td>Y</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 如果prince列的值>3000，group列显示high，否则显示low
df_inner['group'] = np.where(df_inner['price'] > 3000, 'high', 'low')
df_inner
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
      <th>group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>2013-01-02</td>
      <td>beijing</td>
      <td>100-A</td>
      <td>23</td>
      <td>1200</td>
      <td>male</td>
      <td>Y</td>
      <td>10</td>
      <td>low</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>2013-01-03</td>
      <td>sh</td>
      <td>100-B</td>
      <td>44</td>
      <td>3299</td>
      <td>female</td>
      <td>N</td>
      <td>12</td>
      <td>high</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>2013-01-04</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
      <td>2133</td>
      <td>male</td>
      <td>Y</td>
      <td>20</td>
      <td>low</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>2013-01-05</td>
      <td>shenzhen</td>
      <td>110-C</td>
      <td>32</td>
      <td>5433</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>2013-01-06</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>3299</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
      <td>high</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1006</td>
      <td>2013-01-07</td>
      <td>beijing</td>
      <td>130-F</td>
      <td>32</td>
      <td>4432</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 对复合多个条件的数据进行分组标记
df_inner.loc[(df_inner['city'] == 'beijing') & (df_inner['price'] >= 4000), 'sign'] = 1
df_inner
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
      <th>group</th>
      <th>sign</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>2013-01-02</td>
      <td>beijing</td>
      <td>100-A</td>
      <td>23</td>
      <td>1200</td>
      <td>male</td>
      <td>Y</td>
      <td>10</td>
      <td>low</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>2013-01-03</td>
      <td>sh</td>
      <td>100-B</td>
      <td>44</td>
      <td>3299</td>
      <td>female</td>
      <td>N</td>
      <td>12</td>
      <td>high</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>2013-01-04</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
      <td>2133</td>
      <td>male</td>
      <td>Y</td>
      <td>20</td>
      <td>low</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>2013-01-05</td>
      <td>shenzhen</td>
      <td>110-C</td>
      <td>32</td>
      <td>5433</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>2013-01-06</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>3299</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
      <td>high</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1006</td>
      <td>2013-01-07</td>
      <td>beijing</td>
      <td>130-F</td>
      <td>32</td>
      <td>4432</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 对 category-size 字段的值依次进行分列，并创建数据表，索引值为 df_inner 的索引列，列名称为 category 和 size
pd.DataFrame((x.split('-') for x in df_inner['category-size']), index=df_inner.index, columns=['category', 'size'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>100</td>
      <td>B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>110</td>
      <td>A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>110</td>
      <td>C</td>
    </tr>
    <tr>
      <th>4</th>
      <td>210</td>
      <td>A</td>
    </tr>
    <tr>
      <th>5</th>
      <td>130</td>
      <td>F</td>
    </tr>
  </tbody>
</table>
</div>




```python
split = _
# 将完成分裂后的数据表和原df_inner数据表进行匹配
df_inner=pd.merge(df_inner,split,right_index=True, left_index=True)
df_inner
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
      <th>group</th>
      <th>sign</th>
      <th>category</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>2013-01-02</td>
      <td>beijing</td>
      <td>100-A</td>
      <td>23</td>
      <td>1200</td>
      <td>male</td>
      <td>Y</td>
      <td>10</td>
      <td>low</td>
      <td>NaN</td>
      <td>100</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>2013-01-03</td>
      <td>sh</td>
      <td>100-B</td>
      <td>44</td>
      <td>3299</td>
      <td>female</td>
      <td>N</td>
      <td>12</td>
      <td>high</td>
      <td>NaN</td>
      <td>100</td>
      <td>B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>2013-01-04</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
      <td>2133</td>
      <td>male</td>
      <td>Y</td>
      <td>20</td>
      <td>low</td>
      <td>NaN</td>
      <td>110</td>
      <td>A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>2013-01-05</td>
      <td>shenzhen</td>
      <td>110-C</td>
      <td>32</td>
      <td>5433</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
      <td>NaN</td>
      <td>110</td>
      <td>C</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>2013-01-06</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>3299</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
      <td>high</td>
      <td>NaN</td>
      <td>210</td>
      <td>A</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1006</td>
      <td>2013-01-07</td>
      <td>beijing</td>
      <td>130-F</td>
      <td>32</td>
      <td>4432</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
      <td>1.0</td>
      <td>130</td>
      <td>F</td>
    </tr>
  </tbody>
</table>
</div>



## 5. 数据提取

loc 按标签取，iloc 按位置取，ix 同时按标签和位置取


```python
df_inner.loc[3]  # 行号为3的数据
```




    id                              1004
    date             2013-01-05 00:00:00
    city                        shenzhen
    category-size                  110-C
    age                               32
    price                           5433
    gender                        female
    pay                                Y
    m-point                           40
    group                           high
    sign                             NaN
    category                         110
    size                               C
    Name: 3, dtype: object




```python
df_inner.iloc[0:5]  # 前四条数据
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
      <th>group</th>
      <th>sign</th>
      <th>category</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>2013-01-02</td>
      <td>beijing</td>
      <td>100-A</td>
      <td>23</td>
      <td>1200</td>
      <td>male</td>
      <td>Y</td>
      <td>10</td>
      <td>low</td>
      <td>NaN</td>
      <td>100</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>2013-01-03</td>
      <td>sh</td>
      <td>100-B</td>
      <td>44</td>
      <td>3299</td>
      <td>female</td>
      <td>N</td>
      <td>12</td>
      <td>high</td>
      <td>NaN</td>
      <td>100</td>
      <td>B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>2013-01-04</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
      <td>2133</td>
      <td>male</td>
      <td>Y</td>
      <td>20</td>
      <td>low</td>
      <td>NaN</td>
      <td>110</td>
      <td>A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>2013-01-05</td>
      <td>shenzhen</td>
      <td>110-C</td>
      <td>32</td>
      <td>5433</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
      <td>NaN</td>
      <td>110</td>
      <td>C</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>2013-01-06</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>3299</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
      <td>high</td>
      <td>NaN</td>
      <td>210</td>
      <td>A</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_inner.reset_index()  # 重设索引，增加了一个index索引列
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>id</th>
      <th>date</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
      <th>group</th>
      <th>sign</th>
      <th>category</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1001</td>
      <td>2013-01-02</td>
      <td>beijing</td>
      <td>100-A</td>
      <td>23</td>
      <td>1200</td>
      <td>male</td>
      <td>Y</td>
      <td>10</td>
      <td>low</td>
      <td>NaN</td>
      <td>100</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1002</td>
      <td>2013-01-03</td>
      <td>sh</td>
      <td>100-B</td>
      <td>44</td>
      <td>3299</td>
      <td>female</td>
      <td>N</td>
      <td>12</td>
      <td>high</td>
      <td>NaN</td>
      <td>100</td>
      <td>B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>1003</td>
      <td>2013-01-04</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
      <td>2133</td>
      <td>male</td>
      <td>Y</td>
      <td>20</td>
      <td>low</td>
      <td>NaN</td>
      <td>110</td>
      <td>A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>1004</td>
      <td>2013-01-05</td>
      <td>shenzhen</td>
      <td>110-C</td>
      <td>32</td>
      <td>5433</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
      <td>NaN</td>
      <td>110</td>
      <td>C</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>1005</td>
      <td>2013-01-06</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>3299</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
      <td>high</td>
      <td>NaN</td>
      <td>210</td>
      <td>A</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>1006</td>
      <td>2013-01-07</td>
      <td>beijing</td>
      <td>130-F</td>
      <td>32</td>
      <td>4432</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
      <td>1.0</td>
      <td>130</td>
      <td>F</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_inner = df_inner.set_index('date')  # 设置日期列为索引列
df_inner
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
      <th>group</th>
      <th>sign</th>
      <th>category</th>
      <th>size</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>1001</td>
      <td>beijing</td>
      <td>100-A</td>
      <td>23</td>
      <td>1200</td>
      <td>male</td>
      <td>Y</td>
      <td>10</td>
      <td>low</td>
      <td>NaN</td>
      <td>100</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>1002</td>
      <td>sh</td>
      <td>100-B</td>
      <td>44</td>
      <td>3299</td>
      <td>female</td>
      <td>N</td>
      <td>12</td>
      <td>high</td>
      <td>NaN</td>
      <td>100</td>
      <td>B</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>1003</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
      <td>2133</td>
      <td>male</td>
      <td>Y</td>
      <td>20</td>
      <td>low</td>
      <td>NaN</td>
      <td>110</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>1004</td>
      <td>shenzhen</td>
      <td>110-C</td>
      <td>32</td>
      <td>5433</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
      <td>NaN</td>
      <td>110</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1005</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>3299</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
      <td>high</td>
      <td>NaN</td>
      <td>210</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2013-01-07</th>
      <td>1006</td>
      <td>beijing</td>
      <td>130-F</td>
      <td>32</td>
      <td>4432</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
      <td>1.0</td>
      <td>130</td>
      <td>F</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_inner[:'2013-01-05']  # 5号之前的数据
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
      <th>group</th>
      <th>sign</th>
      <th>category</th>
      <th>size</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>1001</td>
      <td>beijing</td>
      <td>100-A</td>
      <td>23</td>
      <td>1200</td>
      <td>male</td>
      <td>Y</td>
      <td>10</td>
      <td>low</td>
      <td>NaN</td>
      <td>100</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>1002</td>
      <td>sh</td>
      <td>100-B</td>
      <td>44</td>
      <td>3299</td>
      <td>female</td>
      <td>N</td>
      <td>12</td>
      <td>high</td>
      <td>NaN</td>
      <td>100</td>
      <td>B</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>1003</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
      <td>2133</td>
      <td>male</td>
      <td>Y</td>
      <td>20</td>
      <td>low</td>
      <td>NaN</td>
      <td>110</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>1004</td>
      <td>shenzhen</td>
      <td>110-C</td>
      <td>32</td>
      <td>5433</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
      <td>NaN</td>
      <td>110</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_inner.iloc[:3, :2]  # 前三条数据，前两列
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>city</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>1001</td>
      <td>beijing</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>1002</td>
      <td>sh</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>1003</td>
      <td>guangzhou</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_inner.iloc[[0, 2, 5], [4, 5]]  # 0、2、5行，4、5列数据
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price</th>
      <th>gender</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>1200</td>
      <td>male</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>2133</td>
      <td>male</td>
    </tr>
    <tr>
      <th>2013-01-07</th>
      <td>4432</td>
      <td>female</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_inner.ix[:'2013-01-04', :4]  # 前2行，前四列数据  ix 不建议使用
```

    /Users/ikeliu/appli/anaconda3/lib/python3.6/site-packages/ipykernel_launcher.py:1: DeprecationWarning: 
    .ix is deprecated. Please use
    .loc for label based indexing or
    .iloc for positional indexing
    
    See the documentation here:
    http://pandas.pydata.org/pandas-docs/stable/indexing.html#ix-indexer-is-deprecated
      """Entry point for launching an IPython kernel.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>1001</td>
      <td>beijing</td>
      <td>100-A</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>1002</td>
      <td>sh</td>
      <td>100-B</td>
      <td>44</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>1003</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_inner['city'].isin(['beijing'])  # 判断包含
```




    date
    2013-01-02     True
    2013-01-03    False
    2013-01-04    False
    2013-01-05    False
    2013-01-06    False
    2013-01-07     True
    Name: city, dtype: bool




```python
df_inner.loc[df_inner['city'].isin(['beijing','shanghai'])]  # 展示在北京上海中的行
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
      <th>group</th>
      <th>sign</th>
      <th>category</th>
      <th>size</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>1001</td>
      <td>beijing</td>
      <td>100-A</td>
      <td>23</td>
      <td>1200</td>
      <td>male</td>
      <td>Y</td>
      <td>10</td>
      <td>low</td>
      <td>NaN</td>
      <td>100</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1005</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>3299</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
      <td>high</td>
      <td>NaN</td>
      <td>210</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2013-01-07</th>
      <td>1006</td>
      <td>beijing</td>
      <td>130-F</td>
      <td>32</td>
      <td>4432</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
      <td>1.0</td>
      <td>130</td>
      <td>F</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(df_inner['category'].str[:3])  # 提取category列的前三个字符组成一个数据表
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>100</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>100</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>110</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>110</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>210</td>
    </tr>
    <tr>
      <th>2013-01-07</th>
      <td>130</td>
    </tr>
  </tbody>
</table>
</div>



## 6. 数据筛选


```python
# 与
df_inner.loc[(df_inner['age'] > 25) & (df_inner['city'] == 'beijing'), ['id','city','age','category','gender']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>city</th>
      <th>age</th>
      <th>category</th>
      <th>gender</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-07</th>
      <td>1006</td>
      <td>beijing</td>
      <td>32</td>
      <td>130</td>
      <td>female</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 或
df_inner.loc[(df_inner['age'] > 25) | (df_inner['city'] == 'beijing'), ['id','city','age','category','gender']].sort_values(['age']) 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>city</th>
      <th>age</th>
      <th>category</th>
      <th>gender</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>1001</td>
      <td>beijing</td>
      <td>23</td>
      <td>100</td>
      <td>male</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>1004</td>
      <td>shenzhen</td>
      <td>32</td>
      <td>110</td>
      <td>female</td>
    </tr>
    <tr>
      <th>2013-01-07</th>
      <td>1006</td>
      <td>beijing</td>
      <td>32</td>
      <td>130</td>
      <td>female</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1005</td>
      <td>shanghai</td>
      <td>34</td>
      <td>210</td>
      <td>male</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>1002</td>
      <td>sh</td>
      <td>44</td>
      <td>100</td>
      <td>female</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>1003</td>
      <td>guangzhou</td>
      <td>54</td>
      <td>110</td>
      <td>male</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 非
df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age','category','gender']].sort_values(['id']) 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>city</th>
      <th>age</th>
      <th>category</th>
      <th>gender</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-03</th>
      <td>1002</td>
      <td>sh</td>
      <td>44</td>
      <td>100</td>
      <td>female</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>1003</td>
      <td>guangzhou</td>
      <td>54</td>
      <td>110</td>
      <td>male</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>1004</td>
      <td>shenzhen</td>
      <td>32</td>
      <td>110</td>
      <td>female</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1005</td>
      <td>shanghai</td>
      <td>34</td>
      <td>210</td>
      <td>male</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 计数 .count()
df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age','category','gender']].city.count()
```




    4




```python
# 使用query函数
df_inner.query('city == ["beijing", "shanghai"]')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
      <th>group</th>
      <th>sign</th>
      <th>category</th>
      <th>size</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>1001</td>
      <td>beijing</td>
      <td>100-A</td>
      <td>23</td>
      <td>1200</td>
      <td>male</td>
      <td>Y</td>
      <td>10</td>
      <td>low</td>
      <td>NaN</td>
      <td>100</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1005</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>3299</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
      <td>high</td>
      <td>NaN</td>
      <td>210</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2013-01-07</th>
      <td>1006</td>
      <td>beijing</td>
      <td>130-F</td>
      <td>32</td>
      <td>4432</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
      <td>1.0</td>
      <td>130</td>
      <td>F</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 求和 .sum()
df_inner.query('city == ["beijing", "shanghai"]').price.sum()
```




    8931



## 7. 数据汇总


```python
df_inner.groupby('city').count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
      <th>group</th>
      <th>sign</th>
      <th>category</th>
      <th>size</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>beijing</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>guangzhou</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>sh</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>shanghai</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>shenzhen</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_inner.groupby('city')['id'].count()
```




    city
    beijing      2
    guangzhou    1
    sh           1
    shanghai     1
    shenzhen     1
    Name: id, dtype: int64




```python
df_inner.groupby(['city','size'])['id'].count()
```




    city       size
    beijing    A       1
               F       1
    guangzhou  A       1
    sh         B       1
    shanghai   A       1
    shenzhen   C       1
    Name: id, dtype: int64




```python
# 对city字段进行汇总，并分别计算prince的合计和均值
df_inner.groupby('city')['price'].agg([len,np.sum, np.mean])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>len</th>
      <th>sum</th>
      <th>mean</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>beijing</th>
      <td>2</td>
      <td>5632</td>
      <td>2816</td>
    </tr>
    <tr>
      <th>guangzhou</th>
      <td>1</td>
      <td>2133</td>
      <td>2133</td>
    </tr>
    <tr>
      <th>sh</th>
      <td>1</td>
      <td>3299</td>
      <td>3299</td>
    </tr>
    <tr>
      <th>shanghai</th>
      <td>1</td>
      <td>3299</td>
      <td>3299</td>
    </tr>
    <tr>
      <th>shenzhen</th>
      <td>1</td>
      <td>5433</td>
      <td>5433</td>
    </tr>
  </tbody>
</table>
</div>



## 8. 数据统计


```python
df_inner.sample(n=3)  # 随机采样
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
      <th>group</th>
      <th>sign</th>
      <th>category</th>
      <th>size</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-04</th>
      <td>1003</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
      <td>2133</td>
      <td>male</td>
      <td>Y</td>
      <td>20</td>
      <td>low</td>
      <td>NaN</td>
      <td>110</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>1004</td>
      <td>shenzhen</td>
      <td>110-C</td>
      <td>32</td>
      <td>5433</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
      <td>NaN</td>
      <td>110</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2013-01-07</th>
      <td>1006</td>
      <td>beijing</td>
      <td>130-F</td>
      <td>32</td>
      <td>4432</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
      <td>1.0</td>
      <td>130</td>
      <td>F</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 自定义采样权重
weights = [0, 0, 0, 0, 0.5, 0.5]
df_inner.sample(n=2, weights=weights)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
      <th>group</th>
      <th>sign</th>
      <th>category</th>
      <th>size</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-06</th>
      <td>1005</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>3299</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
      <td>high</td>
      <td>NaN</td>
      <td>210</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2013-01-07</th>
      <td>1006</td>
      <td>beijing</td>
      <td>130-F</td>
      <td>32</td>
      <td>4432</td>
      <td>female</td>
      <td>Y</td>
      <td>40</td>
      <td>high</td>
      <td>1.0</td>
      <td>130</td>
      <td>F</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 不放回采样
df_inner.sample(n=2, replace=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>city</th>
      <th>category-size</th>
      <th>age</th>
      <th>price</th>
      <th>gender</th>
      <th>pay</th>
      <th>m-point</th>
      <th>group</th>
      <th>sign</th>
      <th>category</th>
      <th>size</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-06</th>
      <td>1005</td>
      <td>shanghai</td>
      <td>210-A</td>
      <td>34</td>
      <td>3299</td>
      <td>male</td>
      <td>N</td>
      <td>40</td>
      <td>high</td>
      <td>NaN</td>
      <td>210</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>1003</td>
      <td>guangzhou</td>
      <td>110-A</td>
      <td>54</td>
      <td>2133</td>
      <td>male</td>
      <td>Y</td>
      <td>20</td>
      <td>low</td>
      <td>NaN</td>
      <td>110</td>
      <td>A</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 统计
df_inner.describe().round(2).T
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>id</th>
      <td>6.0</td>
      <td>1003.50</td>
      <td>1.87</td>
      <td>1001.0</td>
      <td>1002.25</td>
      <td>1003.5</td>
      <td>1004.75</td>
      <td>1006.0</td>
    </tr>
    <tr>
      <th>age</th>
      <td>6.0</td>
      <td>36.50</td>
      <td>10.88</td>
      <td>23.0</td>
      <td>32.00</td>
      <td>33.0</td>
      <td>41.50</td>
      <td>54.0</td>
    </tr>
    <tr>
      <th>price</th>
      <td>6.0</td>
      <td>3299.33</td>
      <td>1523.35</td>
      <td>1200.0</td>
      <td>2424.50</td>
      <td>3299.0</td>
      <td>4148.75</td>
      <td>5433.0</td>
    </tr>
    <tr>
      <th>m-point</th>
      <td>6.0</td>
      <td>27.00</td>
      <td>14.63</td>
      <td>10.0</td>
      <td>14.00</td>
      <td>30.0</td>
      <td>40.00</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>sign</th>
      <td>1.0</td>
      <td>1.00</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 标准差
df_inner['price'].std()
```




    1523.3516556155596




```python
# 协方差
df_inner['price'].cov(df_inner['m-point'])
```




    17263.200000000004




```python
# 所有数据列间的协方差
df_inner.cov()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>age</th>
      <th>price</th>
      <th>m-point</th>
      <th>sign</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>id</th>
      <td>3.5</td>
      <td>-0.7</td>
      <td>1.946000e+03</td>
      <td>25.4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>age</th>
      <td>-0.7</td>
      <td>118.3</td>
      <td>-1.354000e+03</td>
      <td>-31.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>price</th>
      <td>1946.0</td>
      <td>-1354.0</td>
      <td>2.320600e+06</td>
      <td>17263.2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>m-point</th>
      <td>25.4</td>
      <td>-31.0</td>
      <td>1.726320e+04</td>
      <td>214.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>sign</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 相关性
df_inner['price'].corr(df_inner['m-point'])
```




    0.7746655561708526




```python
# 所有数据列之间的相关性
df_inner.corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>age</th>
      <th>price</th>
      <th>m-point</th>
      <th>sign</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>id</th>
      <td>1.000000</td>
      <td>-0.034401</td>
      <td>0.682824</td>
      <td>0.928096</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>age</th>
      <td>-0.034401</td>
      <td>1.000000</td>
      <td>-0.081720</td>
      <td>-0.194833</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>price</th>
      <td>0.682824</td>
      <td>-0.081720</td>
      <td>1.000000</td>
      <td>0.774666</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>m-point</th>
      <td>0.928096</td>
      <td>-0.194833</td>
      <td>0.774666</td>
      <td>1.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>sign</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## 9. 输出


```python
# Excel
df_inner.to_excel('name.xlsx', sheet_name='sheet_name')
```


```python
# csv
df_inner.to_csv('name.csv')
```
