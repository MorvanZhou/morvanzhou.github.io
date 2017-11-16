---
youku_id: XMTcxNjE2MjkwMA
youtube_id: w83mFG5tyW4
bilibili_id: 16378461
description: 这次会说到在我们如何移动 matplotlib 中 axis 坐标轴的位置. 实现多样化的坐标轴显示.
author: 黄伟
chapter: 2
title: 设置坐标轴2
date: 2016-11-3
post-headings:
  - 设置不同名字和位置
  - 调整坐标轴
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt6_ax_setting2.py){:target="_blank"}

这次会说到在我们如何移动matplotlib 中 axis 坐标轴的位置.


{% include assign-heading.html %}

使用`import`导入模块`matplotlib.pyplot`，并简写成`plt`
使用`import`导入模块`numpy`，并简写成`np`

```python
import matplotlib.pyplot as plt
import numpy as np
```



使用`np.linspace`定义x：范围是(-3,3);个数是50.
仿真一维数据组(`x` ,`y1`)表示曲线1.
仿真一维数据组(`x` ,`y2`)表示曲线2.

```python
x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2
```



使用`plt.figure`定义一个图像窗口.
使用`plt.plot`画(`x` ,`y2`)曲线.
使用`plt.plot`画(`x` ,`y1`)曲线，曲线的颜色属性(`color`)为红色;曲线的宽度(`linewidth`)为1.0；曲线的类型(`linestyle`)为虚线.
使用`plt.xlim`设置x坐标轴范围：(-1, 2)；
使用`plt.ylim`设置y坐标轴范围：(-2, 3)；

```python
plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.xlim((-1, 2))
plt.ylim((-2, 3))
```



使用`np.linspace`定义范围以及个数：范围是(-1,2);个数是5.
使用`plt.xticks`设置x轴刻度：范围是(-1,2);个数是5.
使用`plt.yticks`设置y轴刻度以及名称：刻度为[-2, -1.8, -1, 1.22, 3]；对应刻度的名称为['really bad','bad','normal','good', 'really good'].

```python
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])
```



使用`plt.gca`获取当前坐标轴信息.
使用`.spines`设置边框：右侧边框；使用`.set_color`设置边框颜色：默认白色；
使用`.spines`设置边框：上边框；使用`.set_color`设置边框颜色：默认白色；

```python
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()
```

{% include tut-image.html image-name="2_4_1.png" %}

{% include assign-heading.html %}

使用`.xaxis.set_ticks_position`设置x坐标刻度数字或名称的位置：`bottom`.（所有位置：`top`，`bottom`，`both`，`default`，`none`）

```python
ax.xaxis.set_ticks_position('bottom')
```



使用`.spines`设置边框：x轴；使用`.set_position`设置边框位置：y=0的位置；（位置所有属性：`outward`，`axes`，`data`）

```python
ax.spines['bottom'].set_position(('data', 0))
plt.show()
```

{% include tut-image.html image-name="2_4_2.png" %}

使用`.yaxis.set_ticks_position`设置y坐标刻度数字或名称的位置：`left`.（所有位置：`left`，`right`，`both`，`default`，`none`）

```python
ax.yaxis.set_ticks_position('left')
```



使用`.spines`设置边框：y轴；使用`.set_position`设置边框位置：x=0的位置；（位置所有属性：`outward`，`axes`，`data`）
使用`plt.show`显示图像.

```python
ax.spines['left'].set_position(('data',0))
plt.show()
```

{% include tut-image.html image-name="2_4_3.png" %}
