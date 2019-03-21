# 大数据计算服务 maxcompute

## SQL

```sql
select TO_CHAR(DATEADD(getdate(), -1, 'day'), 'yyyy-mm-dd'); -- 昨天
select TO_CHAR(getdate(), 'yyyy-mm-dd') -- 今天
```