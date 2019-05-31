# ORM 使用

## 1. 数据对象

```py
obj = Store.objects.first()
```

### 1.1 get_属性名_display：choices 字段的展示值

```py
obj.get_stage_display()  # 阶段名称
```
