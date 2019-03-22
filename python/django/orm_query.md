# ORM 查询

## QuerySet

values 和 values_list

- values(*fields) 返回一个ValueQuerySet（QuerySet的子类）对象，迭代时返回一个个字典，一个字典对应一个对象，字典的键对应传入的 fields 的值。当不传参数时，返回所有字段的值。参数 field 可以使用 `__` 语法。
  - 假如 foo 是外键字段，那么字典用键 'foo' 和 'foo_id' 都可以取得相同的值
- values_list(*fields, flat=False) 返回的 ValuesListQuerySet 对象在迭代时得到一个个元组，元组的值对应于参数 fields。当 fields 只传递了一个字段名时，可以通过指定 falt=True 来将迭代结果变成一个单独的值而不是一个单值元组。

### Q 对象

就是把一些条件变成一个整体，Q 与 Q 之间可以进行与或非（&|～）操作

## 操作

### Manager方法

- select_related()
  - 相当于join查询，只对外键字段有用
  - 返回QuerySet对象
  - 如果不传参数不会关联查询（网上说的是查出所有的外键（和外键的外键的。。。），但是查看sql日志发现并没有关联查询）所以要填写上你想要的字段名
  - 参数填写外键字段名（字符串格式），多层关联查询可以用双下划线连接多层外键（未查看sql语句）depth参数可以限制连接查询的层数如select_related(depth=2)
  - 返回的对象还是原来的对象，使用的时候还是一样的使用，拿数据还是一样的拿，只是不会再读数据库了，已经在查询的时候连接查询了
  - 可以使用两个下划线连接限制下一层、下下一层。。。的连接查询使用的外键，比如A.objects.select_related('b__c__d').all()
    - 外键不用加id就是模型类的外键属性名就行
- 外键对象获取
  - 一对多和多对多的关系定义方直接使用属性名即可查到
    - 另一方反查的话是 `关系建立方类名小写_set`
    - 如果定义了related_name则使用其

### 过滤方法

- filter
  - contains使用的是like %str%实现的
  - 判断空使用isNull=True
  - range 相当于between and，后面接2元列表参数

### 对象方法

- get_属性名_display()
    很多模型类的属性（表的字段）存的都是数值，再通过choice来对应到真实的选项也就是admin的显示值，可以通过obj.get_属性名_display()来拿到显示值

### 更新值

update方法能跟在filter后面，并且查到多个就更新多个，一个也没查到也不会出错

### 查看SQL语句

```py
from django.db import connection

...

print(connection.queries)
```