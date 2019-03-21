# line_profiler
```py
# 查看每一行代码的运行时间
import line_profiler
import sys


def func():
    j = 0
    for i in range(10000):
        j += 5


if __name__ == '__main__':
    profile = line_profiler.LineProfiler(func)
    profile.enable()
    func()
    profile.disable()
    profile.print_stats(sys.stdout)
```
# [pyganme](https://www.pygame.org/docs/)
跨平台Python模块，专为电子游戏设计，包含图像、声音，建立在SDL基础上。
> SDL 
> 
> 一套开放源代码的跨平台多媒体开发库,多用于开发游戏、模拟器、媒体播放器等多媒体应用领域。
## 导入与初始化
```py
import pygame

pygame.init()  # 初始化pygame库，让计算机硬件准备
```
## 窗口相关操作
- 左上角为坐标原点(0,0)
```py
# 创建窗口
window = pygame.display.set_mode([窗口宽，窗口高])

# 设置窗口标题
pygame.display.set_caption("窗口标题")

# 设置窗口图标
logo_image = pygame.image.load("图标路径")
pygame.display.set_icon(logo_image)

# 指定坐标，将图片绘制到窗口
bg_image = pygame.image.load("图片路径")
window.blit(bg_image, (0, 0))

# 不管做了什么操作，最后刷新一下画面，重新加载。
pygame.display.update()
```
## 图像相关操作
```py
# 加载图片文件，返回图片对象
image = pygame.image.load("图片路径")

# 获得图片矩形对象 -> Rect(x, y, width, height)
# 默认情况下左上角的坐标是 (0, 0)
rect =  image.get_rect()

# 在原位置基础上，移动指定的偏移量 (x, y 增加)
rect.move_ip(num1, num2)

# 判断两个矩形是否相交，相交返回True，否则返回False
flag = pygame.Rect.colliderect(rect1, rect2)
```
## 事件相关操作
常见事件类型：
- QUIT　关闭窗口
- KEYDOWN　键盘按键
- 获得当前所有持续按键bools_tuple
```py
import pygame

pygame.init()
window = pygame.display.set_mode([500, 500])
while True:
    event_list = pygame.event.get()  # 获得所有事件的列表
    for event in event_list:
        if event.type == pygame.QUIT:  # 1. 鼠标点击关闭窗口事件
            print("关闭")
            pygame.quit()  # 结束pygame引擎
            exit()
        if event.type == pygame.KEYDOWN:  # 2. 键盘按下事件
            if event.key == pygame.K_SPACE:  # 空格键
                print("空格")
    pressed_keys = pygame.key.get_pressed()  # 3. 获得当前键盘所有按键的状态(按下，没有按下)，返回bool元组
    if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:  # pygame.K_w等是对应的int值
        print("w 或 上")

```
## 音效相关操作
```py
# 加载背景音乐
pygame.mixer.music.load("音乐路径")
# 循环播放背景音乐
pygame.mixer.music.play(-1)
# 停止背景音乐
pygame.mixer.music.stop()

# 加载音效
boom_sound = pygame.mixer.Sound("音效路径")
# 播放音效
boom_sound.play()
# 停止音效
boom_sound.stop()
```
注意：
1. 音效和音乐的区别是：音效要整个文件载入到Sound对象中才能播放，而音乐不用完全载入，而以流的方式播放。
2. mixer.Sound()不直接支持mp3格式音乐，可以用ogg或wav格式的音乐。
3. 音乐文件比较大，音效文件小，所以读取的方式不同。
## 文字显示操作
```py
# 设置字体和大小
font = pygame.font.SysFont("SimHei", 25)
# render(text(文本内容), antialias(抗锯齿), color(RGB))，返回文字对象
textobj = font.render("欢迎体验飞机大战游戏", 1, (255, 255, 255))
# 设置文字矩形对象位置
textrect = textobj.get_rect(centerx=300, centery=300)
# 在指定位置绘制指定文字对象
window.blit(textobj, textrect)
```
> 获取字体样式  
> `print(pygame.font.get_fonts())`

> RGB(R=Red，G = Green，B = Blue）
>
> RGB色彩模式使用RGB模型为图像中每一个像素的RGB分量分配一个0~255范围内的强度值。  
> 
> 例如：纯红色R值为255，G值为0，B值为0；灰色的R、G、B三个值相等（除了0和255）；  
> 白色的R、G、B都为255；黑色的R、G、B都为0。 
>  
> RGB图像只使用三种颜色，就可以使它们按照不同的比例混合，在屏幕上重现2^24=16777216种颜色。

# wmi
```py
import wmi
def sys_version():
    c = wmi.WMI()

    # 操作系统版本，版本号，32位/64位
    print('\nOS:')
    sys = c.Win32_OperatingSystem()[0]
    print(sys.Caption, sys.BuildNumber, sys.OSArchitecture)

    # CPU类型 CPU内存
    print('\nCPU:')
    processor = c.Win32_Processor()[0]
    print(processor.Name.strip())
    Memory = c.Win32_PhysicalMemory()[0]
    print(int(Memory.Capacity)//1048576,'M')

    # 硬盘名称，硬盘剩余空间，硬盘总大小
    print('\nDISK:')
    for disk in c.Win32_LogicalDisk(DriveType=3):
        print(disk.Caption,'free:', int(disk.FreeSpace)//1048576,'M\t', 'All:', int(disk.Size)//1048576,'M')

    # 获取MAC和IP地址
    print('\nIP:')
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
        print("MAC: %s" % interface.MACAddress)
        for ip_address in interface.IPAddress:
            print("\tIP: %s" % ip_address)

    # BIOS版本 生产厂家 释放日期
    print('\nBIOS:')
    bios = c.Win32_BIOS()[0]
    print(bios.Version)
    print(bios.Manufacturer)
    print(bios.ReleaseDate)


sys_version()
```
# matplotlib
```py
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D  # 不能删，三维需要

def initial_image():

    # define x\y
    x = np.arange(0.0, 2.0, 0.05)
    s = np.sin(np.pi * x)

    # set color and linestyle
    plt.plot(x, s, "yo-")

    # set tilte and x\y labels
    plt.title("it's just a test")
    plt.xlabel("x-label")
    plt.ylabel("y-label")

    plt.grid() # set gridding
    plt.savefig("initial_img.png") # save image
    plt.show() # show the image

def two_images():

    x = np.arange(0.0, 2.0, 0.1)
    s1 = np.sin(np.pi * x)
    s2 = x * 2

    plt.subplot(2, 1, 1) # devide 2 rows and 1 cols and get first row
    plt.plot(x, s1, "yo-")
    plt.title("it's a two_imgs demo")
    plt.xlabel("xx1")
    plt.ylabel("yy1")
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(x, s2, "r.-")
    plt.xlabel("xx2")
    plt.ylabel("yy2")
    plt.grid()
    plt.savefig("two_images.png")
    plt.show()

def Histogram_demo():
    # set u and &
    mean = 100
    sigma = 10

    # produce normal distribution , 10000个数
    x = mean + sigma * np.random.randn(10000)

    num_bins = 50  # 共50个格子
    # 直方图函数， normed=1即和为1,
    # 返回50个概率、直方块左边线的x值、各个方块对象
    n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='yellow', alpha=0.5)
    y = mlab.normpdf(bins, mean, sigma)  # 一条逼近的曲线

    plt.plot(bins, y, "r--")
    plt.title("Histogram of XXX: $\mu=100$, $\sigma=10$")
    plt.xlabel("x-label")
    plt.ylabel("y-label")
    plt.grid()
    plt.subplots_adjust(left=0.15)
    plt.savefig("Histogram_demo.png")
    plt.show()

def d3_points():
    x_list = [[3,3,2],[4,3,1],[1,2,3],[1,1,2],[2,1,2]]
    fig = plt.figure() # 得到画面
    ax = fig.gca(projection='3d') # 得到3d坐标的图
    # 画点
    for x in x_list:
        ax.scatter(x[0],x[1],x[2],c='r')
    plt.savefig("d3_image.png")
    plt.show()

def d3_plane():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1,projection='3d')  # 一行一列第一个
    X = np.arange(1, 10, 1)
    Y = np.arange(1, 10, 1)
    X,Y = np.meshgrid(X, Y)  # 将坐标向量变为坐标矩阵，列为x的长度，行为y的长度
    Z = 3*X + 2*Y + 30

    # 构建平面
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=True)

    ax.set_xlabel("x-label", color='r')
    ax.set_ylabel("y-label", color='g')
    ax.set_zlabel("z-label", color='b')

    ax.set_zlim3d(0, 100) # 设置z坐标轴
    fig.colorbar(surf, shrink=0.5, aspect=5) # 图例

    plt.savefig("d3_plane.png")
    plt.show()

def d3_hookface():
    fig = plt.figure()  # 得到画面
    ax = fig.gca(projection='3d')  # 得到3d坐标的图
    X = np.arange(-5, 5, 0.1)
    Y = np.arange(-5, 5, 0.1)
    X,Y = np.meshgrid(X, Y)  # 将坐标向量变为坐标矩阵，列为x的长度，行为y的长度
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    # 曲面，x,y,z坐标，横向步长，纵向步长，颜色，线宽，是否渐变
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)

    ax.set_xlabel("x-label", color='r')
    ax.set_ylabel("y-label", color='g')
    ax.set_zlabel("z-label", color='b')

    ax.zaxis.set_major_locator(LinearLocator(10))  # 设置z轴标度
    ax.zaxis.set_major_formatter(FormatStrFormatter('%0.02f'))  # 设置z轴精度
    # shrink颜色条伸缩比例0-1, aspect颜色条宽度（反比例，数值越大宽度越窄）
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.savefig("d3_hookface.png")
    plt.show()

def main():
    initial_image()
    two_images()
    Histogram_demo()
    d3_points()
    d3_plane()
    d3_hookface()

if __name__ == '__main__':
    main()
```