# Django

## 命令行命令

- `python manage.py makemigrations` 生成迁移文件
- `python manage.py migrate` 迁移
- `python manage.py shell` 可以进入python交互模式，但是是执行了 manage.py 的，即是交互模式的环境中具有当前项目环境和配置的，比如可以导入某个模型类等，都不会报错
- `python manage.py runserver 0.0.0.0:8080` 启动项目

## request

### 查看url

```py
request.path # 获取不带参数URL（不带主机IP地址）
request.get_host() # 获取主机地址（带有端口号）
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