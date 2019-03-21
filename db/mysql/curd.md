# 增删改查

CURD：创建（Create）、更新（Update）、读取（Retrieve）和删除（Delete）

## 查

LIMIT

```sql
LIMIT m  --查询前m个
LIMIT n,m  --查询第n个开始的m个
```

JOIN

不写什么 JOIN 的时候默认是 INNER JOIN

## 增  

INSERT

```sql
-- 表1事先是不存在的
select value1,value2
into table1
from table2;

-- 表1的三个字段和表2的三个字段一一对应
insert into table1 (value1,value2,value3) -- 如果不标注哪些关键字，那么给入值的顺序必须和被插入表字段的顺序相同
select value4,value5,value6 -- 使用 select 结果作为 values 值的时候不需要写 values 关键字，不需要加括号
from table2;

-- ON DUPLICATE KEY
-- 当遇到唯一值重复时则执行后面的 UPDATE 语句
-- 是 MySQL 的特有语法，并不是 SQL 标准语法
-- duplicate: v. 重复；复制 adj. 完全一样的
INSERT INTO TABLE (a,b,c) VALUES
(1,2,3),
(2,5,7),
(3,3,6),
(4,8,2)
ON DUPLICATE KEY UPDATE b=VALUES(b);
```

## 删

删除表

```sql
DROP TABLE tb_name; -- 删除整个表，包括内部数据和表本身
TRUNCATE TABLE tb_name; -- 删除数据释放空间，但表结构还在，变成一个十成新的空表了
DELETE TABLE tb_name [where ...]; -- 删除整个表的数据或某些数据，不释放空间（例如ID还是会保留）
-- truncate 在各种表上无论是大的还是小的都非常快，使用的系统和事务日志资源少，是一个DDL语言，所以会被隐式提交，不可撤销
-- delete 语句每次删除一行，并在事务日志中为所删除的每行记录一项，可以进行roll back
-- truncate 将重新设置高水平线和所有的索引。在对整个表和索引进行完全浏览时，经过 truncate 操作后的表比Delete操作后的表要快得多
-- truncate 不能触发任何Delete触发器
-- 当表被清空后表和表的索引讲重新设置成初始大小，而delete则不能
-- 不能清空父表
```