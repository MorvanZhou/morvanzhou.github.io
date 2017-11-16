---
youku_id: XMTcxNjI5NzEyMA
youtube_id: zj-tXbuFY_4
bilibili_id: 16378529
description: 有时候数据多也是挺烦人的. 比如数据可能会挡道一些重要的东西. 那我们就可以设置 bbox 来解决被挡住的问题.
chapter: 2
title: tick 能见度
date: 2016-11-3
author: 快乐的石板桥
post-headings:
  - 生成图形
  - 调整坐标
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt9_tick_visibility.py){:target="_blank"}

{% include assign-heading.html %}

当图片中的内容较多，相互遮盖时，我们可以通过设置相关内容的透明度来使图片更易于观察，也即是通过本节中的`bbox`参数设置来调节图像信息.

首先参考之前的[例子]({% link _tutorials/data-manipulation/plt/2-4-axis2.md %}), 我们先绘制图像基本信息：

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 0.1*x

plt.figure()
plt.plot(x, y, linewidth=10)
plt.ylim(-2, 2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
```

{% include tut-image.html image-name="2_7_1.png" %}

{% include assign-heading.html %}

然后对被遮挡的图像调节相关透明度，本例中设置 x轴 和 y轴 的刻度数字进行透明度设置

```python
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))
plt.show()
```

其中`label.set_fontsize(12)`重新调节字体大小，`bbox`设置目的内容的透明度相关参，`facecolor`调节 `box` 前景色，`edgecolor` 设置边框，
本处设置边框为无，`alpha`设置透明度. 最终结果如下:

{% include tut-image.html image-name="2_7_2.png" %}


