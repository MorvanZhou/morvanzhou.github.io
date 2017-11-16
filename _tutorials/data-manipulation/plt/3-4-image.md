---
youku_id: XMTcyMTM2NTA2NA
youtube_id: rqR9429ajg4
bilibili_id: 16378596
description: 使用 matplotlib 展示图片 image 的方法. 用最简单的例子来实现 image 的画图.
author: Hao
chapter: 3
title: Image 图片
date: 2016-11-3
post-headings:
  - 随机矩阵画图
  - 出图方式
  - colorbar
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt13_image.py){:target="_blank"}

{% include assign-heading.html %}

这一节我们讲解怎样在**matplotlib**中打印出图像。这里我们打印出的是纯粹的数字，而非自然图像。
我们今天用这样 3x3 的 2D-array 来表示点的颜色，每一个点就是一个pixel。

```python
import matplotlib.pyplot as plt
import numpy as np

a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)
```

今天做出的图像就是这个样子：

{% include tut-image.html image-name="3_4_1.png" %}

三行三列的格子，**a**代表每一个值，图像右边有一个注释，白色代表值最大的地方，颜色越深值越小。

下面我们来看代码：

```python
plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
```

我们之前选cmap的参数时用的是：`cmap=plt.cmap.bone`，而现在，我们可以直接用单引号传入参数。
`origin='lower'`代表的就是选择的原点的位置。

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

我们在这个[链接](http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html){:target="_blank"}
可以看到**matplotlib**官网上对于内插法的不同方法的描述。下图是一个示例：

{% include tut-image.html image-name="3_4_2.png" %}

这里我们使用的是内插法中的 [Nearest-neighbor](https://en.wikipedia.org/wiki/Nearest-neighbor_interpolation){:target="_blank"} 的方法，其他的方式也都可以随意取选。

{% include assign-heading.html %}

下面我们添加一个`colorbar` ，其中我们添加一个`shrink`参数，使`colorbar`的长度变短为原来的92%：

```python
plt.colorbar(shrink=.92)

plt.xticks(())
plt.yticks(())
plt.show()
```

这样我们2D图像就创建完毕了。

{% include tut-image.html image-name="3_4_1.png" %}






