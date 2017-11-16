---
youku_id: XMTcyMTQwMzY0MA
youtube_id: 68OrRqH2B_s
bilibili_id: 16378646
description: matplotlib 的 subplot 还可以是分隔显示的, 用这种 grid 方法,个人觉得比之前那种方法要方便.
author: Wayne
chapter: 4
title: Subplot 分格显示
date: 2016-11-3
post-headings:
  - subplot2grid
  - gridspec
  - subplots
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt16_grid_subplot.py){:target="_blank"}

matplotlib 的 subplot 还可以是分格的,这里介绍三种方法.


{% include assign-heading.html %}

使用`import`导入`matplotlib.pyplot`模块, 并简写成`plt`. 使用`plt.figure()`创建一个图像窗口

```python
import matplotlib.pyplot as plt

plt.figure()
```

使用`plt.subplot2grid`来创建第1个小图, `(3,3)`表示将整个图像窗口分成3行3列, `(0,0)`表示从第0行第0列开始作图，`colspan=3`表示列的跨度为3, `rowspan=1`表示行的跨度为1. 
`colspan`和`rowspan`缺省, 默认跨度为1. 

```python
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax1.plot([1, 2], [1, 2])    # 画小图
ax1.set_title('ax1_title')  # 设置小图的标题
```

使用`plt.subplot2grid`来创建第2个小图, `(3,3)`表示将整个图像窗口分成3行3列, `(1,0)`表示从第1行第0列开始作图，`colspan=2`表示列的跨度为2.
同上画出 `ax3`, `(1,2)`表示从第1行第2列开始作图，`rowspan=2`表示行的跨度为2. 再画一个 `ax4` 和 `ax5`, 使用默认 `colspan, rowspan`.

```python
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))
```

使用`ax4.scatter`创建一个散点图, 使用`ax4.set_xlabel`和`ax4.set_ylabel`来对x轴和y轴命名.

```python
ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')
```

{% include tut-image.html image-name="4_2_1.png" %}

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

使用`import`导入`matplotlib.pyplot`模块, 并简写成`plt`.
使用`import`导入`matplotlib.gridspec`, 并简写成`gridspec`.

```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
```

使用`plt.figure()`创建一个图像窗口, 使用`gridspec.GridSpec`将整个图像窗口分成3行3列. 

```python
plt.figure()
gs = gridspec.GridSpec(3, 3)
```

使用`plt.subplot`来作图, `gs[0, :]`表示这个图占第0行和所有列, `gs[1, :2]`表示这个图占第1行和第2列前的所有列, 
`gs[1:, 2]`表示这个图占第1行后的所有行和第2列, `gs[-1, 0]`表示这个图占倒数第1行和第0列, `gs[-1, -2]`表示这个图占倒数第1行和倒数第2列. 

```python
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[-1, 0])
ax10 = plt.subplot(gs[-1, -2])
```

{% include tut-image.html image-name="4_2_2.png" %}

{% include assign-heading.html %}

使用`plt.subplots`建立一个2行2列的图像窗口，`sharex=True`表示共享x轴坐标, `sharey=True`表示共享y轴坐标. 
`((ax11, ax12), (ax13, ax14))`表示第1行从左至右依次放`ax11`和`ax12`, 第2行从左至右依次放`ax13`和`ax14`. 

```python
f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
```

使用`ax11.scatter`创建一个散点图. 

```python
ax11.scatter([1,2], [1,2])
```

`plt.tight_layout()`表示紧凑显示图像, `plt.show()`表示显示图像. 

```python
plt.tight_layout()
plt.show()
```

{% include tut-image.html image-name="4_2_3.png" %}
