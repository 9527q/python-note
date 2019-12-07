# ORM 使用

## 数据对象的方法

```py
obj = Store.objects.first()
obj.get_stage_display()  # get_属性名_display：choices 字段的展示值，不存在时返回字段原值
obj._state.adding  # bool 是否是新增的对象（还没有数据库数据对应：True）
```
