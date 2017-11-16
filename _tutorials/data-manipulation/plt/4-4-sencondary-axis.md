---
youku_id: XMTcyMTQ1OTkzMg
youtube_id: cFO72oNbmZo
bilibili_id: 16378714
description: 有时候我们会要用到次坐标轴, 在一种图上两个 y 轴. 同样可以用 matplotlib 做到,而且很简单.
author: Jeff
chapter: 4
title: 次坐标轴
date: 2016-11-3
post-headings:
  - 第一个y坐标
  - 第二个y坐标
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt18_secondary_yaxis.py){:target="_blank"}

{% include assign-heading.html %}

有时候我们会用到次坐标轴，即在同个图上有第2个y轴存在。同样可以用matplotlib做到，而且很简单。

首先，我们做一些准备工作：

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)

y1 = 0.05 * x**2

y2 = -1 * y1
```

可以看到，`y2`和`y1`是互相倒置的。接着，获取figure默认的坐标系 `ax1`：

```python
fig, ax1 = plt.subplots()
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

对`ax1`调用`twinx()`方法，生成如同镜面效果后的`ax2`：

```python
ax2 = ax1.twinx()
```

接着进行绘图, 将 `y1`, `y2` 分别画在 `ax1`, `ax2` 上：

```python
ax1.plot(x, y1, 'g-')   # green, solid line

ax1.set_xlabel('X data')

ax1.set_ylabel('Y1 data', color='g')

ax2.plot(x, y2, 'b-') # blue

ax2.set_ylabel('Y2 data', color='b')

```

显示图像：

```python
plt.show()
```

{% include tut-image.html image-name="4_4_1.png" %}
