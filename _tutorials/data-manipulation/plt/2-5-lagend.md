---
youku_id: XMTcxNjE5MzA0OA
youtube_id: dGZyoX72iEg
bilibili_id: 16378490
description: matplotlib 中的 legend 图例就是为了帮我们展示出每个数据对应的名称. 更好的让读者认识到你的数据结构.
chapter: 2
title: Legend 图例
date: 2016-11-3
author: 快乐的石板桥
post-headings:
  - 添加图例
  - 调整位置和名称
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt7_legend.py){:target="_blank"}

{% include assign-heading.html %}

matplotlib 中的 `legend` 图例就是为了帮我们展示出每个数据对应的图像名称. 更好的让读者认识到你的数据结构.

上次课我们了解到关于坐标轴设置方面的一些内容，代码如下：

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
#set x limits
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# set new sticks
new_sticks = np.linspace(-1, 2, 5)
plt.xticks(new_sticks)
# set tick labels
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
```

本节中我们将对图中的两条线绘制图例，首先我们设置两条线的类型等信息（蓝色实线与红色虚线).

```python
# set line syles
l1, = plt.plot(x, y1, label='linear line')
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')
```

`legend`将要显示的信息来自于上面代码中的 `label`. 所以我们只需要简单写下一下代码, plt 就能自动的为我们添加图例.

```python
plt.legend(loc='upper right')
```

参数 `loc='upper right'` 表示图例将添加在图中的右上角. 

{% include tut-image.html image-name="2_5_1.png" %}

{% include assign-heading.html %}

如果我们想单独修改之前的 `label` 信息, 给不同类型的线条设置图例信息. 我们可以在 `plt.legend` 输入更多参数.
如果以下面这种形式添加 legend, 我们需要确保, 在上面的代码 `plt.plot(x, y2, label='linear line')` 和 
`plt.plot(x, y1, label='square line')`
中有用变量 `l1` 和 `l2` 分别存储起来. 而且需要注意的是 `l1,` `l2,`要以逗号结尾, 因为`plt.plot()` 返回的是一个列表.

```python
plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')
```

这样我们就能分别重新设置线条对应的 `label` 了.

最后我们得到带有图例信息的图片.

{% include tut-image.html image-name="2_5_2.png" %}

其中'loc'参数有多种，'best'表示自动分配最佳位置，其余的如下：

```python
 'best' : 0,          
 'upper right'  : 1,
 'upper left'   : 2,
 'lower left'   : 3,
 'lower right'  : 4,
 'right'        : 5,
 'center left'  : 6,
 'center right' : 7,
 'lower center' : 8,
 'upper center' : 9,
 'center'       : 10,
```