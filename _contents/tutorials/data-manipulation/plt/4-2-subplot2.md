---
youku_id: XMTcyMTQwMzY0MA
youtube_id: 68OrRqH2B_s
description: matplotlib 的 subplot 还可以是分隔显示的, 用这种 grid 方法,个人觉得比之前那种方法要方便.
author: Wayne
chapter: 4
title: Subplot 分格显示
date: 2016-11-3
---
* 学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt16_grid_subplot.py)

matplotlib 的 subplot 还可以是分格的,这里介绍三种方法.

* Method 1: [subplot2grid](#m1)
* Method 2: [gridspec](#m2)
* Method 3: [easy to define structure](#m3)

<h4 id="m1">Method 1: subplot2grid</h4>

使用`import`导入`matplotlib.pyplot`模块, 并简写成`plt`.

```python
import matplotlib.pyplot as plt
```

使用`plt.figure()`创建一个图像窗口

```python
plt.figure()
```

使用`plt.subplot2grid`来创建第1个小图, `(3,3)`表示将整个图像窗口分成3行3列, `(0,0)`表示从第0行第0列开始作图，`colspan=3`表示列的跨度为3, `rowspan=1`表示行的跨度为1. 
`colspan`和`rowspan`缺省, 默认跨度为1. 

```python
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
```
使用`ax1.plot`在画出这个小图.

```python
ax1.plot([1, 2], [1, 2])
```
使用`ax1.set_title`来指定小图的标题.

```python
ax1.set_title('ax1_title')
```
使用`plt.subplot2grid`来创建第2个小图, `(3,3)`表示将整个图像窗口分成3行3列, `(1,0)`表示从第1行第0列开始作图，`colspan=2`表示列的跨度为2.

```python
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
```

使用`plt.subplot2grid`来创建第3个小图, `(3,3)`表示将整个图像窗口分成3行3列, `(1,2)`表示从第1行第2列开始作图，`rowspan=2`表示行的跨度为2.

```python
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
```
使用`plt.subplot2grid`来创建第4个小图, `(3,3)`表示将整个图像窗口分成3行3列, `(2,0)`表示从第2行第0列开始作图.

```python
ax4 = plt.subplot2grid((3, 3), (2, 0))
```
使用`ax4.scatter`创建一个散点图, 使用`ax4.set_xlabel`和`ax4.set_ylabel`来对x轴和y轴命名.

```python
ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')
```
使用`plt.subplot2grid`来创建第5个小图, `(3,3)`表示将整个图像窗口分成3行3列, `(2,1)`表示从第2行第1列开始作图.

```python
ax5 = plt.subplot2grid((3, 3), (2, 1))
```
<img class="course-image" src="plt4_2_1.png">

<h4 id="m2">Method 2: gridspec</h4>

使用`import`导入`matplotlib.pyplot`模块, 并简写成`plt`.

```python
import matplotlib.pyplot as plt
```

使用import导入`matplotlib.gridspec`, 并简写成`gridspec`.

```python
import matplotlib.gridspec as gridspec
```

使用`plt.figure()`创建一个图像窗口

```python
plt.figure()
```

使用`gridspec.GridSpec`将整个图像窗口分成3行3列. 

```python
gs = gridspec.GridSpec(3, 3)
```
使用`plt.subplot`来作图, `gs[0, :]`表示这个图占第0行和所有列, gs[1, :2]表示这个图占第1行和第2列前的所有列, gs[1:, 2]表示这个图占第1行后的所有行和第2列, gs[-1, 0]表示这个图占倒数第1行和第0列, gs[-1, -2]表示这个图占倒数第1行和倒数第2列. 

```python
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[-1, 0])
ax10 = plt.subplot(gs[-1, -2])
```
<img class="course-image" src="plt4_2_2.png">

<h4 id="m3">Method 3: easy to define structure</h4>

使用`plt.subplots`建立一个2行2列的图像窗口，`sharex=True`表示共享x轴坐标, `sharey=True`表示共享y轴坐标. `((ax11, ax12), (ax13, ax14))`表示第1行从左至右依次放ax11和ax12, 第2行从左至右依次放ax13和ax14. 


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
<img class="course-image" src="plt4_2_3.png">