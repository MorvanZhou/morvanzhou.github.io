---
youku_id: XMTY0NDcxODQ4NA
youtube_id: SCMLObsel5I
bilibili_id: 16379330
title: Pandas plot 出图
description: pandas 的 plot 是基于 matplotlib 模块的. 所以如果你用过 matplotlib, pandas 的可视化功能,你也很容易上手. 视频里提到了两种 plot 的方式,其他种的和这两种的运用方式类似,大家可以自学其他的,应该会更容易上手.
author: Huiwei
date: 2016-11-3
chapter: 3
post-headings:
  - 创建一个Series
  - Dataframe 可视化
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/numpy%26pandas/18_plot.py){:target="_blank"}


这次我们讲如何将数据可视化. 
首先`import`我们需要用到的模块，除了 pandas，我们也需要使用 numpy 生成一些数据，这节里使用的 matplotlib 仅仅是用来 show 图片的, 即 `plt.show()`。

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

今天我们主要是学习如何 plot data


{% include assign-heading.html %}

这是一个线性的数据，我们随机生成1000个数据，`Series` 默认的 `index` 就是从0开始的整数，但是这里我显式赋值以便让大家看的更清楚

```python
# 随机生成1000个数据
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
 
# 为了方便观看效果, 我们累加这个数据
data.cumsum()

# pandas 数据可以直接观看其可视化形式
data.plot()

plt.show()
```

就这么简单，熟悉 matplotlib 的朋友知道如果需要`plot`一个数据，我们可以使用 `plt.plot(x=, y=)`，把`x`,`y`的数据作为参数存进去，但是`data`本来就是一个数据，所以我们可以直接`plot`。
生成的结果就是下图：

{% include tut-image.html image-name="3-8-1.png" %}



{% include google-in-article-ads.html %}

{% include assign-heading.html %}

我们生成一个1000*4 的`DataFrame`，并对他们累加

```python
data = pd.DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),
    columns=list("ABCD")
    )
data.cumsum()
data.plot()
plt.show()
```

{% include tut-image.html image-name="3-8-2.png" %}

这个就是我们刚刚生成的4个`column`的数据，因为有4组数据，所以4组数据会分别`plot`出来。`plot` 可以指定很多参数，具体的用法大家可以自己查一下[这里](http://pandas.pydata.org/pandas-docs/version/0.18.1/visualization.html){:target="_blank"}

除了`plot`，我经常会用到还有`scatter`，这个会显示散点图，首先给大家说一下在 pandas 中有多少种方法

* bar
* hist
* box
* kde
* area
* scatter
* hexbin

但是我们今天不会一一介绍，主要说一下 `plot` 和 `scatter`.
因为`scatter`只有`x`，`y`两个属性，我们我们就可以分别给`x`, `y`指定数据

```python
ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
```

然后我们在可以再画一个在同一个`ax`上面，选择不一样的数据列，不同的 `color` 和 `label`

```python
# 将之下这个 data 画在上一个 ax 上面
data.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)
plt.show()
```

下面就是我`plot`出来的图片

{% include tut-image.html image-name="3-8-3.png" %}

这就是我们今天讲的两种呈现方式，一种是线性的方式，一种是散点图。

