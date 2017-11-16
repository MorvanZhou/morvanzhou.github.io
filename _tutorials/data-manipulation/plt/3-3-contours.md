---
youku_id: XMTcyMTQ1MjAwNA
youtube_id: Sb4NKsYbULI
bilibili_id: 16378569
description: 用 matplotlib 画等高线, 用一个最简单的例子来阐述如何画出等高线图.
author: Hao
chapter: 3
title: Contours 等高线图
date: 2016-11-3
post-headings:
  - 画等高线
  - 添加高度数字
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt12_contours.py){:target="_blank"}

本节讲解如何用`matplotlib`生成等高线图。今天的结果如下图所示：

{% include tut-image.html image-name="3_3_1.png" %}

{% include assign-heading.html %}


数据集即三维点 (x,y) 和对应的高度值，共有256个点。高度值使用一个 height function `f(x,y)` 生成。
x, y 分别是在区间 [-3,3] 中均匀分布的256个值，并用`meshgrid`在二维平面中将每一个x和每一个y分别对应起来，编织成栅格:

```python
import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X,Y = np.meshgrid(x, y)
```

接下来进行颜色填充。使用函数`plt.contourf`把颜色加进去，位置参数分别为：X, Y, f(X,Y)。透明度0.75，并将 f(X,Y) 的值对应到color map的暖色组中寻找对应颜色。

```python
# use plt.contourf to filling contours
# X, Y and value for (X,Y) point
plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
```


接下来进行等高线绘制。使用`plt.contour`函数划线。位置参数为：X, Y, f(X,Y)。颜色选黑色，线条宽度选0.5。现在的结果如下图所示，只有颜色和线条，还没有数值Label：

```python
# use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
```

{% include tut-image.html image-name="3_3_2.png" %}

{% include assign-heading.html %}

其中，8代表等高线的密集程度，这里被分为10个部分。如果是0，则图像被一分为二。

最后加入Label，`inline`控制是否将Label画在线里面，字体大小为10。并将坐标轴隐藏：

```python
plt.clabel(C, inline=True, fontsize=10)
plt.xticks(())
plt.yticks(())
```

最终结果即：

{% include tut-image.html image-name="3_3_1.png" %}













