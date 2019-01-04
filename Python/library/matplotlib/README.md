# Matplotlib

![matplotlib](images/matplotlib.png)

Matplotlib 是一个进行数据展示的 2D 绘图库。

![matplotlib_demo](images/matplotlib_demo.png)

> Matplotlib 3.0 只支持 Python 3；Matplotlib 2.2.x 支持 Python 2，不过 bug 修复和发布到 2020 年 1 月 1 日将停止。

- [官方文档](https://matplotlib.org/index.html)
- [项目地址](https://github.com/matplotlib/matplotlib)

## marker

```py
from matplotlib.markers import MarkerStyle

print(MarkerStyle.markers)
```

[样式图案](https://matplotlib.org/api/markers_api.html#module-matplotlib.markers)

## 常见问题

### x 轴显示时间

```py
# ax 是图对象
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
plt.xticks(pd.date_range('2018-01-01', '2018-12-31'), rotation=90)
```