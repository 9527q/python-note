# MySQL

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

大小写不敏感

### 查看变量值

```sql
show variables like 'xxx';
```

### 用户创建与授权

创建用户

```sql
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
--'host'：该用户可登录的主机，本机可设为'localhost'，任意主机可设为'%'
--'password'：密码，可以为空''，也可以不写从identified之后的东西，即不用密码就能登录数据库
```

授权

```sql
GRANT privileges ON databasename.tablename TO 'username'@'host' WITH GRANT OPTION;
--privileges：要设置的操作权限，比如select、insert、update等，全部权限的话就用all
--所有数据库或者所有表名用*代替，比如*.*
--with grant option表示被授权的用户有给别的用户授权的功能，不需要的话可以不加
```

撤销授权

```sql
REVOKE privilege ON databasename.tablename FROM 'username'@'host';
--授权与取消授权时使用的db.tb应该使用相同的格式
```

查看权限

```sql
SHOW GRANTS FOR 'username'@'host';
```

设置更改密码

```sql
SET PASSWORD FOR 'username'@'host' = PASSWORD('newpassword');
--如果是当前登录用户的话就不用写for ''@''了
```

删除用户

```sql
DROP USER 'username'@'host';
```

## 开启查询日志

日志开启与关闭

```sql
set global general_log_file='path/file_name.log';
--必须以.log为后缀，注意保证mysql对该文件有写权限

set global general_log=on;  --开启
--设置开启的时候会向 .log 中写入一些东西，如果全都删了就无法记录了，此时关闭再开启即可

set global general_log=off;  --关闭
```

## 增删改查

```sql
limit m  --查询前m个
limit n,m  --查询第n个开始的m个
```

## 常见问题

### 字段名和关键字重名

字段用  ``` ` ```（1旁边的那个）引起来

### 什么是utf8mb4？utf8 + emoji表情

```sql
create database oss_dev character set utf8mb4;
```

此处设置为utf8mb4会触发MySQL 5.7 默认的index prefix限制，须配合innodb_large_prefix=ON使用，不过应该是自动设置为ON了。