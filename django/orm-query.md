# ORM 查询

## 1. QuerySet

`django.db.models` 下面的一个类，`MyModel.objects.` 时得到的对象

### 1.1 filter 过滤(sql-where)

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

### 1.2 values 和 values_list 只取部分输出值(sql-只查某些字段的值)

- `.values(*fields)` 
  - 返回一个ValueQuerySet（QuerySet的子类）对象
  - 迭代时返回一个个字典，一个字典对应一条数据，字典的键对应传入的 fields，字典的值对应数据对象该字段的值。
  - 假如 foo 是外键字段，那么字典用键 `'foo'` 和 `'foo_id'` 取到的是相同的值，即id
- `.values_list(*fields, flat=False)` 
  - 返回一个 ValuesListQuerySet 对象，类似一个二维数据
  - 迭代时返回一个个元组，元组的顺序及值对应于参数 `fields` 及数据对象该字段的值。
  - 当 `fields` 只传递了一个字段名时，可以通过指定 `falt=True` 来将返回结果变成一维数据
  - 得到的对象可以直接和其他列表进行操作，也能被哈希。

## 1.3 select_related 关联查询(sql-join)

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

## 1.4 update 批量跟新(sql-update)

`.update(**kwargs)`

1. 更新指定字段的值
2. 返回更新了多少条（int）

## 2. Q 对象

把查询条件变成可以进行与或非操作的对象 `& | ~`

```py
from django.db.models import Q

q = Q(id__gte=80) | Q(name_contains='京')
q &= Q(addr='上海')

qs = Store.objects.filter(q)
```
