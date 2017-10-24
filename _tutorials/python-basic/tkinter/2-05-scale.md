---
youku_id: XMTYwODE0Njg2MA
youtube_id: rRZdcHKZQw8
description: 使用 python 和 tkinter 来做简单的窗口程序. 拉动条 scale 练习.
chapter: 2
title: Scale 尺度
date: 2016-11-3
post-headings:
  - scale 部件
  - 触发功能
author: 潘雨 (Mr_Pan)
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk6_scale.py){:target="_blank"}


这一次的效果将会像下面的图片一样.

{% include tut-image.html image-name="2-05-01.jpg" %}

如果拖动滚动条, 效果就会如下.

{% include tut-image.html image-name="2-05-02.jpg" %}

{% include tut-image.html image-name="2-05-03.jpg" %}




{% include assign-heading.html %}

```python
s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()
```

这里的参数`label`是指scale部件的名称，即在这里scale部件名称为`try me`

* 参数`from_=5，to=11`的意思就是从5到11，即这个滚动条最小值为5，最大值为11（这里使用from_是因为在python中有from这个关键词）
* 参数`orient=tk.HORIZONTAL`在这里就是设置滚动条的方向，如我们所看到的效果图，这里`HORIZONTAL`就是横向。
* 参数`length`这里是指滚动条部件的长度，但注意的是和其他部件width表示不同，width表示的是以字符为单位，比如`width=4`，就是4个字符的长度，而此处的`length=200`，是指我们常用的像素为单位，即长度为200个像素
* 参数`resolution=0.01`这里我们可以借助数学题来理解，我们做的很多数学题都会让我们来保留几位小数，此处的0.01就是保留2位小数，即效果图中的5.00 9.00等等后面的两位小数，如果保留一位就是`resolution=0.1`
这里的`showvalue`就是设置在滚动条上方的显示。`showvalue=0`显示的就是效果图，上方无结果显示，如果改为`showvalue=1`，则会显示为：

{% include tut-image.html image-name="2-05-04.jpg" %}

参数`tickinterval`设置的就是坐标的间隔，此处为`tickinterval=2`，显示的即为效果图中的5.00 7.00 9.00 11.00 如果改为`tickinterval=3`则为5.00 8.00 11.00：


{% include tut-image.html image-name="2-05-05.jpg" %}




{% include assign-heading.html %}

```python
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection(v):
    l.config(text='you have selected ' + v)
```

这里相比前面多了参数`v`，这里的参数`v`即将滚动条定位的数据，即如效果图中最开始，定位到5.00，`label`中显示you have selected 5.00

再补充一下 Tkinter 的[必备步骤](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk6_scale.py){:target="_blank"},
整个框架的全部代码就完美了.
