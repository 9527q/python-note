# Django

## ORM

相关命令

- `python manage.py makemigrations` 生成迁移文件
- `python manage.py sqlmigrate` 查看实际执行的 SQL 语句
- `python manage.py migrate` 真正迁移
- 发生冲突，使用 `python manage.py migrate app {指定的migrations}` 回退再重新 migrate

### 开发

- 清楚每一句代码对应怎么样的 SQL 语句和执行过程

### 模型类定义

- Model 用大驼峰命名法，数据库自动转为 {app小写}_{model名称小写}
- Model 的外键，数据库会自动转为 {外键名称小写}_id，并创建一条外键

#### 模型类的属性（字段）

参数:

- related_name
    - 值为字符串，外键字段专用
    - 外键反查时使用的名字，可以不指定（使用 `.模型类名小写_set` 反查（一对多外键））
    - 若模型类Book有n个外键字段都指向模型类Person，那至少其中n-1个字段应该指定related_name的值
    - 多个外键（无论在不在同一模型类中）只要指向同一个模型类，那么他们的related_name的值就不能相同

### 增删改查操作

#### Manager方法

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

#### 过滤方法

- filter
    - contains使用的是like %str%实现的
    - 判断空使用isNull=True
    - range 相当于between and，后面接2元列表参数

#### 对象方法

- get_属性名_display()
    很多模型类的属性（表的字段）存的都是数值，再通过choice来对应到真实的选项也就是admin的显示值，可以通过obj.get_属性名_display()来拿到显示值

#### 更新值

update方法能跟在filter后面，并且查到多个就更新多个，一个也没查到也不会出错

### admin站点

- raw_id_fields
    - 元组，外键字段对应的属性名
    - 填入后站点中选择值时是放大镜搜索，会弹出新窗口选择，在编辑页会显示为id值，适合外键对应表的数据很多的情况
    - 不填的外键在选择值时是下拉列表的样子，适合外键对应表的数据较少的情况

## request

### 查看url

```py
request.path # 获取不带参数URL（不带主机IP地址）
request.get_host() # 获取主机地址（带有端口号）
```

### 查看SQL语句

```py
from django.db import connection
...
print(connection.queries)
```

## 常见问题

1. URL中传递user_id有什么用
    即使登录校验过了也不能确定user_id就是真的
2. 多个查询语句也可能是一句执行的
    ```py
    # 会被优化成一句，不管两个判断的结果如何
    warehouse_list_obj = Warehouse.objects.select_related("city").all().order_by("-order")
    if query_name:
        warehouse_list_obj = warehouse_list_obj.filter(name__contains=query_name)
    if query_city_id:
        warehouse_list_obj = warehouse_list_obj.filter(city__id=query_city_id)
    ```