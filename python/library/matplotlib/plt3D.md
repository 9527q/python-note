# 简单的三维图像

[官方文档](https://matplotlib.org/tutorials/toolkits/mplot3d.html)

先得到三维图像对象

```py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 增加一个坐标轴

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  # 1.0.0 之前的版本写法：`ax = Axes3D(fig)`
```

## 曲线图

```py
# Axes3D： 3D 图像类，使用时用三维对象代替
# zs：z 数据， 与 xs、ys 等大小的数组，或者一个实数值
# zdir：哪个方向朝 z（上）
Axes3D.plot(xs, ys, *args, zdir='z', **kwargs)
```

例子

```py
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

# Prepare arrays x, y, z
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

ax.plot(x, y, z, label='parametric curve')  # 参数曲线
ax.legend()

plt.show()
```

![plt3D_line_demo](images/plt3D_line_demo.png)

### 散点图

```py
# s：size
# c：color
# depthshade：是否按深度决定颜色深浅
Axes3D.scatter(xs, ys, zs=0, zdir='z', s=20, c=None, depthshade=True, *args, **kwargs)
```

```py
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility. 可复现
np.random.seed(19950901)


def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
```

![plt3D_scatter_demo](images/plt3D_scatter_demo.png)

### 线框图

```py
# X, Y, Z : 2d arrays
#   Data values.
# rcount, ccount : int
#   各个方向上的采样数量，默认为 50，2.0 以后的版本才有。与采样步长互斥，都为默认值则采样数量有效，都给定则报错。
# rstride，cstride： int
#   各个方向上的采样步长，默认为 1，
#   'classic' 模式会默认采用采样步长。
Axes3D.plot_wireframe(X, Y, Z, *args, **kwargs)
```

```py
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grab some test data.
X, Y, Z = axes3d.get_test_data(0.05)

# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()
```

![plt3D_wireframe_demo](images/plt3D_wireframe_demo.png)

### 曲面

```py
# X, Y, Z : 2d arrays，Data values.
# rcount, ccount : int 默认 50
# rstride, cstride : int 默认 10
# color : color-like
# cmap : Colormap
# facecolors : array-like of colors.
# norm : Normalize : Normalization for the colormap.
# vmin, vmax : float : Bounds for the normalization.
# shade : bool : Whether to shade the face colors.
Axes3D.plot_surface(X, Y, Z, *args, norm=None, vmin=None, vmax=None, lightsource=None, **kwargs)
```

例子1

```py
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.Blues,
                       linewidth=0, antialiased=True)  # anti-aliasing，AA，抗锯齿

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)  # z 轴刻度范围
ax.zaxis.set_major_locator(LinearLocator(10))  # z 轴刻度数量
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  # z 轴刻度显示格式

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)  # shrink：收缩比例；aspect：高宽比
plt.show()
```

![plt3D_surface_demo00](images/plt3D_surface_demo00.png)

例子2

```py
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make data
u = np.linspace(0, 2 * np.pi, 100)  # 两端值，个数
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface
ax.plot_surface(x, y, z, color='b')
plt.show()
```

![plt3D_surface_demo01](images/plt3D_surface_demo01.png)
