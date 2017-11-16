---
youku_id: XMTcyMTM3NjU2MA
youtube_id: Zm1cDw7DnUA
bilibili_id: 16378629
description: matplotlib 是可以组合许多的小图,放在一张大图里面显示的. 使用到的方法叫作 subplot.
author: Wayne
chapter: 4
title: Subplot 多合一显示
date: 2016-11-3
post-headings:
  - 均匀图中图
  - 不均匀图中图
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt15_subplot.py){:target="_blank"}

{% include assign-heading.html %}

matplotlib 是可以组合许多的小图, 放在一张大图里面显示的. 使用到的方法叫作 subplot.  

使用`import`导入`matplotlib.pyplot`模块, 并简写成`plt`. 使用`plt.figure`创建一个图像窗口.

```python
import matplotlib.pyplot as plt

plt.figure()
```

使用`plt.subplot`来创建小图. `plt.subplot(2,2,1)`表示将整个图像窗口分为2行2列, 当前位置为1. 使用`plt.plot([0,1],[0,1])`在第1个位置创建一个小图.

```python
plt.subplot(2,2,1)
plt.plot([0,1],[0,1])
```

`plt.subplot(2,2,2)`表示将整个图像窗口分为2行2列, 当前位置为2. 使用`plt.plot([0,1],[0,2])`在第2个位置创建一个小图.

```python
plt.subplot(2,2,2)
plt.plot([0,1],[0,2])
```

`plt.subplot(2,2,3)`表示将整个图像窗口分为2行2列,当前位置为3. `plt.subplot(2,2,3)`可以简写成`plt.subplot(223)`, matplotlib同样可以识别. 使用`plt.plot([0,1],[0,3])`在第3个位置创建一个小图.

```python
plt.subplot(223)
plt.plot([0,1],[0,3])
```

`plt.subplot(224)`表示将整个图像窗口分为2行2列, 当前位置为4. 使用`plt.plot([0,1],[0,4])`在第4个位置创建一个小图.   

```python
plt.subplot(224)
plt.plot([0,1],[0,4])

plt.show()  # 展示
```

{% include tut-image.html image-name="4_1_1.png" %}

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

如果希望展示的小图的大小不相同, 应该怎么做呢?
以上面的4个小图为例, 如果把第1个小图放到第一行, 而剩下的3个小图都放到第二行.  

使用`plt.subplot(2,1,1)`将整个图像窗口分为2行1列, 当前位置为1.
使用`plt.plot([0,1],[0,1])`在第1个位置创建一个小图.

```python
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])
```

使用`plt.subplot(2,3,4)`将整个图像窗口分为2行3列, 当前位置为4. 
使用`plt.plot([0,1],[0,2])`在第4个位置创建一个小图.

```python
plt.subplot(2,3,4)
plt.plot([0,1],[0,2])
```

这里需要解释一下为什么第4个位置放第2个小图. 上一步中使用`plt.subplot(2,1,1)`将整个图像窗口分为2行1列, 第1个小图占用了第1个位置, 也就是整个第1行.
这一步中使用`plt.subplot(2,3,4)`将整个图像窗口分为2行3列, 于是整个图像窗口的第1行就变成了3列, 也就是成了3个位置, 于是第2行的第1个位置是整个图像窗口的第4个位置. 

使用`plt.subplot(235)`将整个图像窗口分为2行3列,当前位置为5.  使用`plt.plot([0,1],[0,3])`在第5个位置创建一个小图.
同上, 再创建`plt.subplot(236)`.

```python
plt.subplot(235)
plt.plot([0,1],[0,3])

plt.subplot(236)
plt.plot([0,1],[0,4])

plt.show()  # 展示
```

{% include tut-image.html image-name="4_1_2.png" %}


