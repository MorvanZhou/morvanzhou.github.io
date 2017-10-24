---
youku_id: XMTYxMDUyMDEyNA
youtube_id: WoHYMSlRdrU
description: 使用 python 和 tkinter 来做简单的窗口程序. frame 练习.
chapter: 2
title: Frame 框架
date: 2016-11-3
post-headings:
  - Frame 部件
author: 潘雨 (Mr_Pan)
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk10_frame.py){:target="_blank"}


这一次的效果将会像下面的图片一样.

{% include tut-image.html image-name="2-09-01.jpg" %}





{% include assign-heading.html %}

Frame 是一个在 Windows 上分离小区域的部件, 它能将 Windows 分成不同的区,然后存放不同的其他部件.
同时一个 Frame 上也能再分成两个 Frame, Frame 可以认为是一种容器.


```python
###定义一个`label`显示`on the window`
tk.Label(window, text='on the window').pack()

###在`window`上创建一个`frame`
frm = tk.Frame(window)
frm.pack()

###在刚刚创建的`frame`上创建两个`frame`，我们可以把它理解成一个大容器里套了一个小容器，即`frm`上有两个`frame` ，`frm_l`和`frm_r`

frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)

###这里是控制小的`frm`部件在大的`frm`的相对位置，此处`frm_l`就是在`frm`的左边，`frm_r`在`frm`的右边
frm_l.pack(side='left')
frm_r.pack(side='right')

###这里的三个label就是在我们创建的frame上定义的label部件，还是以容器理解，就是容器上贴了标签，来指明这个是什么，解释这个容器。
tk.Label(frm_l, text='on the frm_l1').pack()##这个`label`长在`frm_l`上，显示为`on the frm_l1`
tk.Label(frm_l, text='on the frm_l2').pack()##这个`label`长在`frm_l`上，显示为`on the frm_l2`
tk.Label(frm_r, text='on the frm_r1').pack()##这个`label`长在`frm_r`上，显示为`on the frm_r1`
```

再补充一下 Tkinter 的[必备步骤](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk10_frame.py){:target="_blank"},
整个框架的全部代码就完美了.

