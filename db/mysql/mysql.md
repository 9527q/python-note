# 原理

## 存储引擎

| InnoDB（默认） | MyISAM
-|-|-
适用场景 | OLTP/在线业务 | OLAP/数据分析
性能 | 读写性能均衡 | 批量读写性能好
锁 | 行锁 | 表锁
事物 | 支持 | 不支持
外键 | 支持 | 不支持
存储结构 | 结构和数据混合 | 结构和数据分离

## InnoDB 存储结构

表/段（数据段，索引段）/区（逻辑空间单位）/页（磁盘管理单位）/行

## 索引

索引结构：B+树（平衡多叉树）

聚集索引、联合索引

索引缺点

- 数据选择性低的字段不适合建索引
- 写多读少的字段不适合建索引，维护开销大
- 大字段（如 text）不适合建索引
- 索引太多会占表空间

## 备份和复制

- 文件备份：rsync
- 逻辑备份（库、表）：mysqldump
- 增量备份：xtrabackup
- 二进制备份：binlog
- 主从复制：server binlog -> client relaylog

## 开发规范

库

- 主从结构，主写从读
- 存储引擎：InnoDB
- 字符集：utf8/utf8mb4
- 线上线下环境隔离
- 尽量不在 MySQL 层面做计算，读取后在应用程序做计算
- 避免使用外键、存储过程、触发器、定时器等，增加维护成本
- 分库分表：单库百张表考虑分库，单表千万数据考虑分表

表

- 最好遵循第三范式，综合心能考虑可适当冗余
- 必须设置主键，建议使用自增ID
- 选取合适的数据类型、合适的精度，能用数值型就不用字符型
- 字段避免使用NULL
- 字段加注释
- 禁止保存大数据字段，如图片、文件等
- 禁止保存明文密码

## 查询优化

- 优化工具
  - explain
  - 慢查询（大于 1s）
- 按需取用
  - 避免全表扫描
  - 限制查询范围，where xxx
  - 避免 `select *`（例外：优先使用 `select count(*)`）
  - 避免返回大数据量，加 limit
  - 减少访问次数（网络、硬盘开销大）
- 优先使用索引
  - 在 where、order by、join 列建立索引
  - 联合索引的最左匹配原则
- 导致索引失效二全表扫描
  - where is null
  - !=
  - or、in、not in（可使用between）
  - like '%xx'
  - 字段运算（替换为右值）
  - 函数运算
- 子查询/连接的权衡
  - 尽量避免子查询和 join，尤其是多层子查询、多表 join
  - 避免大表子查询和 join，用 where 限制范围
  - 对于复杂的子查询和 join，用内存、缓存代替

## 外部命令

导出数据库数据到 `.sql` 文件。

```sh
mysqldump -u username -p database > datafile.sql
```

导入 `.spl` 文件到数据库中。

```sh
mysql -u username -p database < datafile.sql
```

## 内部命令

- 大小写不敏感

查看变量值

```sql
show variables like 'xxx';
```

新建变量

```sql
set @dt = now();
```

用户创建与授权

```sql
-- 创建用户
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
--'host'：该用户可登录的主机，本机可设为'localhost'，任意主机可设为'%'
--'password'：密码，可以为空''，也可以不写从identified之后的东西，即不用密码就能登录数据库

-- 授权
GRANT privileges ON databasename.tablename TO 'username'@'host' WITH GRANT OPTION;
--privileges：要设置的操作权限，比如select、insert、update等，全部权限的话就用all
--所有数据库或者所有表名用*代替，比如*.*
--with grant option表示被授权的用户有给别的用户授权的功能，不需要的话可以不加

-- 撤销授权
REVOKE privilege ON databasename.tablename FROM 'username'@'host';
--授权与取消授权时使用的db.tb应该使用相同的格式

-- 查看权限
SHOW GRANTS FOR 'username'@'host';

-- 设置更改密码
SET PASSWORD FOR 'username'@'host' = PASSWORD('newpassword');
--如果是当前登录用户的话就不用写for ''@''了

-- 删除用户
DROP USER 'username'@'host';
```

运行 .sql 文件

```sql
SOURCE filepath/filename.sql
```

日志开启与关闭

```sql
set global general_log_file='path/file_name.log';
--必须以.log为后缀，注意保证mysql对该文件有写权限

set global general_log=on;  --开启
--设置开启的时候会向 .log 中写入一些东西，如果全都删了就无法记录了，此时关闭再开启即可

set global general_log=off;  --关闭
```

## 常见问题

### 字段名和关键字重名

字段用  ``` ` ```（1旁边的那个）引起来

### 什么是utf8mb4？utf8 + emoji表情

```sql
create database oss_dev character set utf8mb4;
```

此处设置为utf8mb4会触发MySQL 5.7 默认的index prefix限制，须配合innodb_large_prefix=ON使用，不过应该是自动设置为ON了。