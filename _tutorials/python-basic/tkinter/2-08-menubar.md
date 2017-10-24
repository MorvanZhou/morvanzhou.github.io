---
youku_id: XMTYwODc0NDEwMA
youtube_id: SaPE553NlrQ
description: 使用 python 和 tkinter 来做简单的窗口程序. 菜单 menubar 练习.
chapter: 2
title: Menubar 菜单
date: 2016-11-3
post-headings:
  - menubar 部件
  - 触发功能
author: 潘雨 (Mr_Pan)
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk9_menubar.py){:target="_blank"}


这一次的效果将会像下面的图片一样.
{% include tut-image.html image-name="2-08-01.png" %}

注意这里的操作系统是苹果的 MacOS, 它的菜单栏位置和 Windows 的不一样.
{% include tut-image.html image-name="2-08-02.png" %}

{% include tut-image.html image-name="2-08-03.png" %}

下面那张图除了 "Cut", "Copy", "Paste" 的选项, 后面的都是 Apple 自己生成的选项, Windows 不会有的.



{% include assign-heading.html %}

下面是我们制作整个菜单栏的流程, 我们先需要加入一个 Menubar 作为整体框架,
然后再在 Menubar 中加一些部件.

```python
##创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
menubar = tk.Menu(window)

##定义一个空菜单单元
filemenu = tk.Menu(menubar, tearoff=0)

##将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='File', menu=filemenu)

##在`File`中加入`New`的小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
##如果点击这些单元, 就会触发`do_job`的功能
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)##同样的在`File`中加入`Open`小菜单
filemenu.add_command(label='Save', command=do_job)##同样的在`File`中加入`Save`小菜单

filemenu.add_separator()##这里就是一条分割线

##同样的在`File`中加入`Exit`小菜单,此处对应命令为`window.quit`
filemenu.add_command(label='Exit', command=window.quit)
```

同样的我们在定义另一个菜单`Edit`也是如此和定义的`File`菜单一样
这里再来看一下效果中比较不一样的菜单就是`File`中的`Import`菜单, 在这个菜单选项中, 我们还能分支出更多的选项.

```python
submenu = tk.Menu(filemenu)##和上面定义菜单一样，不过此处实在`File`上创建一个空的菜单
filemenu.add_cascade(label='Import', menu=submenu, underline=0)##给放入的菜单`submenu`命名为`Import`
submenu.add_command(label="Submenu1", command=do_job)##这里和上面也一样，在`Import`中加入一个小菜单命令`Submenu1`
```






{% include assign-heading.html %}

```python
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter+=1
```

这里的功能就是没触发一次命令，counter就会+1，在label上的显示就会从
do 0 ,do 1 , do 2...
再补充一下 Tkinter 的[必备步骤](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk9_menubar.py){:target="_blank"},
整个框架的全部代码就完美了.