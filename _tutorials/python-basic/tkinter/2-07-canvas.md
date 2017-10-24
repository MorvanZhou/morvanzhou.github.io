---
youku_id: XMTYwODY4ODMwNA
youtube_id: TgcyOBZDgw8
description: 使用 python 和 tkinter 来做简单的窗口程序. 画布 canvas 练习.
chapter: 2
title: Canvas 画布
date: 2016-11-3
post-headings:
  - Canvas部件
  - 触发功能
author: 潘雨 (Mr_Pan)
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk8_canvas.py){:target="_blank"}
  * [需要的图片地址](/static/results/tkinter/ins.gif)


运行之后的效果将会像下面的图片一样.

{% include tut-image.html image-name="2-07-01.png" %}

如果点击move这个button, 效果就会如下.

{% include tut-image.html image-name="2-07-02.png" %}





{% include assign-heading.html %}

```python
canvas = tk.Canvas(window, bg='blue', height=100, width=200)
canvas.pack()
```

这里的参数和以往学过的部件一样，所以就不再一一解释。
如果你想下载那个 instagram 的图标, 可以点击[这里下载](/static/results/tkinter/ins.gif), 或者直接右键保存下面的图像.

{% include tut-image.html image-name="ins.gif" %}

```python
image_file = tk.PhotoImage(file='ins.gif')
image = canvas.create_image(10, 10, anchor='nw', image=image_file)
```

这里的代码主要是实现我们最终看到的在左上角的那张小图片。
`image_file = tk.PhotoImage(file='ins.gif')`这一句是创造一个变量存放`ins.gif`这张图片。
`image = canvas.create_image(10, 10, anchor='nw', image=image_file)`里面的参数`10,10`就是图片放入画布的坐标，
而这里的`anchor=nw`则是把图片的左上角作为锚定点，在加上刚刚给的坐标位置，即可将图片位置确定。
最后一个参数的意思大家应该都知道，就是将刚刚存入的图片变量，赋值给`image`。

```python
x0, y0, x1, y1= 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
```

这段代码主要实现的是画一条直线，后面`()`中给的参数就是线段两点的坐标，两点确定一条直线。此处给的就是从坐标(50,50)到(80,80)画一条直线。

```python
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')  #创建一个圆，填充色为`red`红色
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)  #创建一个扇形
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)   #创建一个矩形
```

这里面就是创建扇形时多了两个没见过的参数`start=0`和`extent=180`，其实就是从0度到180度，就好像扇子的边打开一样。在我们看来就是个半圆，
如果改为`extent=90`，我们看到的就是一个1/4圆






{% include assign-heading.html %}

```python
def moveit():
    canvas.move(rect, 0, 2)
```

这里的触发不再是以往的print_selection了，哈哈，那么这里的是怎么样的功能呢，首先我们从单词理解来看就是移动的函数，在视频中也演示过了，
就是我们每点一次`button` 矩形就会移动这里`canvas.move(rect, 0, 2)`的参数`(rect,0,2)`就是移动`rect`这个变量，即我们看到的矩形
后面的0和2，也就是横坐标移动0个单位，纵坐标移动2个单位，简单的说就是每次点击，横向不动，纵向移动两个单位。

再补充一下 Tkinter 的[必备步骤](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk8_canvas.py){:target="_blank"},
整个框架的全部代码就完美了.