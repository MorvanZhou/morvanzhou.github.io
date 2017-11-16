---
youku_id: XMTcxNjA0MjM2MA
youtube_id: 4Y7f0znUT6E
bilibili_id: 16378407
description: 使用 matplotlib 做一个简单的画图练习, 熟悉最基础的用法.
author: 黄伟
chapter: 2
title: 基本用法
date: 2016-11-3
post-headings:
  - 基础应用
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt3_simple_plot.py){:target="_blank"}

{% include assign-heading.html %}

使用`import`导入模块`matplotlib.pyplot`，并简写成`plt`
使用`import`导入模块`numpy`，并简写成`np`

```python
import matplotlib.pyplot as plt
import numpy as np
```

使用`np.linspace`定义x：范围是(-1,1);个数是50.
仿真一维数据组(`x` ,`y`)表示曲线1.

```python
x = np.linspace(-1, 1, 50)
y = 2*x + 1
```

使用`plt.figure`定义一个图像窗口.
使用`plt.plot`画(`x` ,`y`)曲线.
使用`plt.show`显示图像.

```python
plt.figure()
plt.plot(x, y)
plt.show()
```

{% include tut-image.html image-name="2_1.png" %}
