---
youku_id: XMTYxMDU5MzI2MA
youtube_id: gb6cVVg9viM
description: 使用 python 和 tkinter 来做简单的窗口程序. 排列位置 pack grid place 练习.
chapter: 2
title: pack grid place 放置位置
date: 2016-11-3
post-headings:
  - pack
  - grid
  - place
author: 潘雨 (Mr_Pan)
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk12_position.py){:target="_blank"}


{% include assign-heading.html %}

首先我们先看看我们常用的`pack()`, 他会按照上下左右的方式排列.

```python
tk.Label(window, text='1').pack(side='top')#上
tk.Label(window, text='1').pack(side='bottom')#下
tk.Label(window, text='1').pack(side='left')#左
tk.Label(window, text='1').pack(side='right')#右
```

{% include tut-image.html image-name="2-11-01.png" %}





{% include assign-heading.html %}

接下里我们在看看`grid()`, grid 是方格, 所以所有的内容会被放在这些规律的方格中.

```python
for i in range(4):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)
```

以上的代码就是创建一个四行三列的表格，其实`grid`就是用表格的形式定位的。这里的参数
`row`为行，`colum`为列，`padx`就是单元格左右间距，`pady`就是单元格上下间距。

{% include tut-image.html image-name="2-11-02.png" %}





{% include assign-heading.html %}

再接下来就是`place()`, 这个比较容易理解，就是给精确的坐标来定位，如此处给的`（20,10）`，就是将这个部件放在坐标为`（x，y）`的这个位置
后面的参数`anchor=nw`就是前面所讲的锚定点是西北角。

```python
tk.Label(window, text=1).place(x=20, y=10, anchor='nw')
```


{% include tut-image.html image-name="2-11-03.png" %}


再补充一下 Tkinter 的[必备步骤](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk12_position.py){:target="_blank"},
整个框架的全部代码就完美了.