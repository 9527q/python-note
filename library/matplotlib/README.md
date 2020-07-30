# Matplotlib

Matplotlib 是一个进行数据展示的 2D 绘图库。

- [官方文档](https://matplotlib.org/)
- [点的 marker](https://matplotlib.org/api/markers_api.html#module-matplotlib.markers)

## 常见问题

### x 轴显示时间

```py
# ax 是图对象
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
plt.xticks(pd.date_range('2018-01-01', '2018-12-31'), rotation=90)
```

### 中文显示

macOS

```python
# 加在程序开头
plt.rcParams["font.family"] = 'Arial Unicode MS'
```
