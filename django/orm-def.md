# ORM 定义

对象关系映射 Object Relational Mapping

## 1. 命名

- 模型类类名用大驼峰命名法，数据库表名为为 {小写app名}_{小写模型类名}
- 外键字段在数据库中的字段名是 {小写外键属性名}_id，会真的在数据库层面创建外键

## 2. 字段参数

### 2.1 `related_name`

- 值为字符串，外键字段专用
- 外键反查时使用的名字，可以不指定（使用 `.模型类名小写_set` 反查）
- 显然
  - 一个模型类下有 n 个外键的指向都是同一个模型类时，其中至少 n-1 个必须指定 `related_name` 的值
  - 所有指向同一个模型类的外键字段（不论在不在一个模型类中），只要定义了 `related_name`，互相之间这个值就不可以相同

