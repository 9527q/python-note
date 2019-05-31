# ORM 查询

## 1. QuerySet 查询集

`django.db.models` 下面的一个类，`MyModel.objects.` 时得到的对象

### 1.1 特性

1. 惰性执行
2. 缓存

#### 1.1.1 惰性执行
- 创建查询集不会访问数据库，直到调用数据时，才会访问数据库
- 调用数据的情况包括迭代、序列化、与 if 合用

```py
qs = Store.object.filter(is_valid=True)  # 没有查询数据库，仅仅是创建了一个查询集
print(qs.count())  # 23380 真正查询数据库的时候
``` 

#### 1.1.2 缓存

通过 `._result_cache` 标记实现

1. 只会查询一次数据库
    ```py
    books = Book.objects.filter(name__contains='刀')
    for book in books:
        print(book.name)
    for book in books:
        print(book.id)
    ```
2. 查询两次数据库
    ```py
    books = Book.objects.filter(name__contains='刀')
    for book in books:
        print(book.name)
    for book in books:
        print(book.id)
    ```
3. 查询两次数据库
    ```py
    qs = Store.object.filter(is_valid=True)  # 没有查询数据库，仅仅是创建了一个查询集
    print(qs.count())  # 23380 真正查询数据库的时候
    qs.update(is_valid=False)  # self._result_cache = None
    print(qs.count())  # 0 又一次查询数据库
    ```

### 1.2 方法

一句话方法：

- `.update(**kwargs)`，sql-update，更新某些字段的值，返回更新了多少条数据
- `.all()`，返回所有数据对象
- `.first()`，返回第一条数据对象（不一定是按照id排序的）
- `.last()`，返回最后一条数据对象
- `.count()`，返回查询结果的数量
- `.exists()`，返回查询结果是否存在
- `.order_by(*field_names)`，根据某些字段进行排序，传入字段名，字段名前带 `'-'` 表示倒序
- 可以进行切片或取下标操作，sql-limit，不支持负数索引

#### 1.2.1 filter 和 exclude 过滤(sql-where)

filter 保留符合条件的；exclude 剔除符合条件的

1. 返回 QuerySet 对象
2. 传入条件的格式是 `'字段名__条件'='值'`
3. 条件之间使用 `,` 分割，关系是且

- contains 字符串包含
  - `.filter(name__contains='刘')` 名字中包含‘刘’
  - 使用 `like %str%` 实现的
  - 各种字符都进行转义了，貌似没有漏洞
- icontains 忽略大小写的 contains
- lgte 大小关系判断
  - `.filter(age__lt=9)` 年龄小于9
  - `.filter(age__gte=9)` 年龄大于等于9
- isNull 判断空
  - `.filter(addr__isNull=False)` 地址字段有值的数据
- range 区间判断
  - 即 `between xx and yy`
  - `.filter(age__range=(9, 20)` 年龄在9和20之间
  - 左右全包含

#### 1.2.2 get

`.get(**kwargs)`

- 返回单个数据对象
- 不存在符合条件的数据时抛出 `MyModel.DoesNotExist`
- 存在多跳符合条件的数据时抛出 `MyModel.MultipleObjectsReturned`
- 会受前面的 filter 的影响

#### 1.2.3 values 和 values_list 只取部分输出值(sql-只查某些字段的值)

返回的对象只能再调用 QuerySet 的部分方法。

- `.values(*fields)` 
  - 返回一个ValueQuerySet（QuerySet的子类）对象
  - 迭代时返回一个个字典，一个字典对应一条数据，字典的键对应传入的 fields，字典的值对应数据对象该字段的值。
  - 假如 foo 是外键字段，那么字典用键 `'foo'` 和 `'foo_id'` 取到的是相同的值，即id
- `.values_list(*fields, flat=False)` 
  - 返回一个 ValuesListQuerySet 对象，类似一个二维数据
  - 迭代时返回一个个元组，元组的顺序及值对应于参数 `fields` 及数据对象该字段的值。
  - 当 `fields` 只传递了一个字段名时，可以通过指定 `falt=True` 来将返回结果变成一维数据
  - 得到的对象可以直接和其他列表进行操作，也能被哈希。

#### 1.2.4 select_related 关联查询(sql-join)

`.select_related(*fields)`

- 相当于join查询，传入外键字段名
- 返回QuerySet对象
  - 返回的对象还是原来的对象，使用的时候还是一样的使用，只是不会再重复读数据库了，已经在查询的时候连接查询了
- 不传参数不会关联查询
- 参数填写外键字段名（字符串格式），多层关联查询可以用双下划线连接多层外键
- 不能用在 `.values` 和 `.values_list` 之后

```py
# 多层关联查询(brand 和 brand.sales 都被关联查询到了)
Store.objects.select_related('brand__sales', 'creator')
# 不会关联查询
Store.objects.select_related('brand').select_related()
# 两个字段都会关联查询
Store.objects.select_related('brand').select_related('sales')
```

## 2. Q 对象

把查询条件变成可以进行与或非操作的对象 `& | ~`

```py
from django.db.models import Q

q = Q(id__gte=80) | Q(name_contains='京')
q &= Q(addr='上海')

qs = Store.objects.filter(q)
```
