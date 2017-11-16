---
youku_id: XMTcyMTQzNTUyMA
youtube_id: UqL589c8quk
bilibili_id: 16378679
description: 怎么样在图片中在添加一张小的图片注解呢? 这个教程就告诉你. matplotlib 的图中图教程.
author: Jeff
chapter: 4
title: 图中图
date: 2016-11-3
post-headings:
  - 数据
  - 大图
  - 小图
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt17_plot_in_plot.py){:target="_blank"}

这次我们来讲matplotlib里一个很有意思的功能，叫做图中图(plot in plot)，最后的效果如下：

{% include tut-image.html image-name="4_3_1.png" %}

可以看到，整个Figure 1包含了三个图，其中两个小图`title inside 1`和`title inside 2`又出现在大图`title`中。这是如何做到的呢？

{% include assign-heading.html %}

首先是一些准备工作：

```python
# 导入pyplot模块
import matplotlib.pyplot as plt

# 初始化figure
fig = plt.figure()

# 创建数据
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

接着，我们来绘制大图。首先确定大图左下角的位置以及宽高：

```python
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
```

注意，4个值都是占整个`figure`坐标系的百分比。在这里，假设`figure`的大小是10x10，那么大图就被包含在由(1, 1)开始，宽8，高8的坐标系内。

将大图坐标系添加到`figure`中，颜色为r(red)，取名为title：

```python
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')
```

效果如下：

{% include tut-image.html image-name="4_3_2.png" %}

{% include assign-heading.html %}

接着，我们来绘制左上角的小图，步骤和绘制大图一样，注意坐标系位置和大小的改变：

```python
left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(y, x, 'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')
```

效果如下：

{% include tut-image.html image-name="4_3_3.png" %}

最后，我们来绘制右下角的小图。这里我们采用一种更简单方法，即直接往plt里添加新的坐标系：

```python
plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, 'g') # 注意对y进行了逆序处理
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')
```

最后显示图像：

```python
plt.show()
```

{% include tut-image.html image-name="4_3_1.png" %}
