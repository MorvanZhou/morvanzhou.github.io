---
youku_id: XMTcxNjMzMDEyOA
youtube_id: EPDaHAbLPs4
bilibili_id: 16378542
description: 当然, matplotlib 是可以做散点图 scatter 的. 而且还可以做散点图很多特效, 我们来做一个练习.
author: Hao
chapter: 3
title: Scatter 散点图
date: 2016-11-3
post-headings:
  - 散点图
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt10_scatter.py){:target="_blank"}


本节我们将讲述各种不同的plot的方式。之前我们讲到了如何plot线，今天我们讲述如何plot散点图。
今天用到的例子最终呈现的结果如下图：

{% include tut-image.html image-name="3_1_1.png" %}

{% include assign-heading.html %}

首先，先引入`matplotlib.pyplot`简写作`plt`,再引入模块`numpy`用来产生一些随机数据。生成1024个呈[标准正态分布](https://zh.wikipedia.org/wiki/%E6%AD%A3%E6%80%81%E5%88%86%E5%B8%83){:target="_blank"}的二维数据组 (平均数是0，方差为1) 作为一个数据集，并图像化这个数据集。每一个点的颜色值用`T`来表示：

```python
import matplotlib.pyplot as plt
import numpy as np

n = 1024    # data size
X = np.random.normal(0, 1, n) # 每一个点的X值
Y = np.random.normal(0, 1, n) # 每一个点的Y值
T = np.arctan2(Y,X) # for color value
```



数据集生成完毕，现在来用`scatter`plot这个点集，鼠标点上去，可以看到这个函数的各个parameter的描述，如下图：

{% include tut-image.html image-name="3_1_2.png" %}



输入`X`和`Y`作为location，`size=75`，颜色为`T`，`color map`用默认值，透明度`alpha` 为 50%。
x轴显示范围定位(-1.5，1.5)，并用`xtick()`函数来隐藏x坐标轴，y轴同理：

```python
plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks(())  # ignore xticks
plt.ylim(-1.5, 1.5)
plt.yticks(())  # ignore yticks

plt.show()

```



这些就是本节内容，下节我们将介绍怎么运用条形图`bar`。