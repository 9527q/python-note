# 大数据计算服务 maxcompute

## SQL

今天昨天的字符串

```sql
-- SELECT TO_CHAR(DATEADD(GETDATE(), -1, 'day'), 'yyyy-mm-dd'); -- 昨天
SELECT TO_CHAR(GETDATE(), 'yyyy-mm-dd') -- 今天
-- GETDATE: 返回系统当前时间（东八区），在一个 SQL 执行过程中，总会返回一个固定的值，可能是 SQL 执行期间的任意时间
```

分区条件中不能直接给时间函数的结果

```sql
SELECT  *
FROM    xxx --分区表，分区字段为 event_date，string格式
WHERE   event_date in (select TO_CHAR(getdate(), 'yyyy-mm-dd'))
-- WHERE   event_date = TO_CHAR(getdate(), 'yyyy-mm-dd') --会报错说没有声明分区条件
```

时间的标准格式和对应标识符: `yyyy-mm-dd hh:mi:ss`