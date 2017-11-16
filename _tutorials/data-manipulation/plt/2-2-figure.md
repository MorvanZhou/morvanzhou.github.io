---
youku_id: XMTcxNjA2OTM5Mg
youtube_id: 5IuawGiZ7_0
bilibili_id: 16378428
description: matplotlib 的 figure 就是一个 单独的 figure 小窗口, 小窗口里面还可以有更多的小图片. 我们用一个简单的例子来练习一下.
author: 黄伟
chapter: 2
title: figure 图像
date: 2016-11-3
post-headings:
  - 简单的线条
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt4_figure.py){:target="_blank"}

{% include assign-heading.html %}

matplotlib 的 figure 就是一个 单独的 figure 小窗口, 
小窗口里面还可以有更多的小图片. 

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
使用`plt.plot`画(`x` ,`y1`)曲线.

```python
plt.figure()
plt.plot(x, y1)
plt.show()
```

{% include tut-image.html image-name="2_2_1.png" %}

使用`plt.figure`定义一个图像窗口：编号为3；大小为(8, 5).
使用`plt.plot`画(`x` ,`y2`)曲线.
使用`plt.plot`画(`x` ,`y1`)曲线，曲线的颜色属性(`color`)为红色;曲线的宽度(`linewidth`)为1.0；曲线的类型(`linestyle`)为虚线.
使用`plt.show`显示图像.

```python
plt.figure(num=3, figsize=(8, 5),)
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.show()
```

{% include tut-image.html image-name="2_2_2.png" %}







