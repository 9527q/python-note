# 机器学习 PAI

SQL脚本 组件

- 输入数据已自动映射成t1~t4,使用方式如：select * from ${t1}
- 用户也可以直接输入maxcompute表名使用，也就是说不要读数据表组件也可以
- 如果读取分区表，必须有分区条件
- 支持 maxcompute SQL 的所有语法
