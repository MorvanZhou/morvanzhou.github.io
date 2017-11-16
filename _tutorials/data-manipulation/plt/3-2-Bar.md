---
youku_id: XMTcxNjM5NDI1Ng
youtube_id: dmGRCJIEWrE
bilibili_id: 16378554
description: matplotlib 中的 bar 条形图, 柱状图是如何使用的呢. 这就是一个简单好玩的例子.
author: Hao
chapter: 3
title: Bar 柱状图 
date: 2016-11-3
post-headings:
  - 生成基本图形
  - 加颜色和数据
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt11_bar.py){:target="_blank"}
  

本节我们介绍一下用`matplotib`来制作一个柱状图，今天的结果如下图：

{% include tut-image.html image-name="3_2_1.png" %}

今天的柱状图分成上下两部分，每一个柱体上都有相应的数值标注，并且取消坐标轴的显示。

{% include assign-heading.html %}

向上向下分别生成12个数据，X为 0 到 11 的整数 ，Y是相应的[均匀分布](https://en.wikipedia.org/wiki/Uniform_distribution){:target="_blank"}的随机数据。
使用的函数是`plt.bar`，参数为X和Y：

```python
import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1)
plt.bar(X, -Y2)

plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()
```


这样我们就生成了下图所示的柱状图基本框架：

{% include tut-image.html image-name="3_2_2.png" %}

{% include assign-heading.html %}

下面我们就颜色和数值进行优化。
用`facecolor`设置主体颜色，`edgecolor`设置边框颜色为白色，

```python
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
```

现在的结果呈现：

{% include tut-image.html image-name="3_2_3.png" %}

接下来我们用函数`plt.text`分别在柱体上方（下方）加上数值，用`%.2f`保留两位小数，横向居中对齐`ha='center'`，纵向底部（顶部）对齐`va='bottom'`：

```python
for x, y in zip(X, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')
```

最终的结果就像开始一样：

{% include tut-image.html image-name="3_2_1.png" %}


