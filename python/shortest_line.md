# 平面上的多个点的最短连接

## 每次计算所有已连接点到所有未连接点的距离，连接最短的那条

```py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19950901)
n = 100
x_low, x_high, y_low, y_high = 0, 100, 0, 100


def shortest_lines(points: list) -> list:
    """找出最短路径"""
    outs = {i: p for i, p in enumerate(points)}  # 未连接的点
    ins = {0: outs.pop(0)}  # 已连接的点
    lines = []  # 连接线

    def dist(point1, point2):
        """计算两个点的距离"""
        return np.sum((point1 - point2) ** 2)

    while outs:
        # 找到最短路径
        p0, p1, ko, ki = min(((out_p, in_p, ko, ki) for ko, out_p in outs.items() for ki, in_p in ins.items()),
                             key=lambda p: dist(p[0], p[1]))
        ins[ko] = outs.pop(ko)
        lines.append((ki, ko))

    return lines


def plot(points: list, lines: list):
    """画出路径"""
    for l in lines:
        p1, p2 = points[l[0]], points[l[1]]
        xs, ys = [p1[0], p2[0]], [p1[1], p2[1]]
        plt.plot(xs, ys, marker='o')
    plt.show()


def main():
    points = [np.array([np.random.randint(x_low, x_high), np.random.randint(y_low, y_high)]) for _ in range(n)]
    lines = shortest_lines(points)
    plot(points, lines)


if __name__ == '__main__':
    main()
```

![shortest_line](images/shortest_line.png)
