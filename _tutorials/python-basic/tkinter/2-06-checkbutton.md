---
youku_id: XMTYwODE4NDc0NA
youtube_id: WJHHDXSES-0
description: 使用 python 和 tkinter 来做简单的窗口程序. 选择按钮 checkbutton 练习.
chapter: 2
title: Checkbutton 勾选项
date: 2016-11-3
post-headings:
  - Checkbutton部件
  - 触发功能
author: 潘雨 (Mr_Pan)
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk7_checkbutton.py){:target="_blank"}


运行之后的效果将会像下面的图片一样，此时不作任何操作.

{% include tut-image.html image-name="2-06-01.jpg" %}

如果只选中第一个选项，即图中的python, 效果就会如下.

{% include tut-image.html image-name="2-06-02.jpg" %}

如果只选中第二个选项，即图中的c++, 效果就会如下.

{% include tut-image.html image-name="2-06-03.jpg" %}

如果两个选项都选中, 效果就会如下.

{% include tut-image.html image-name="2-06-04.jpg" %}

如果两个选项都不选中, 效果就会如下.

{% include tut-image.html image-name="2-06-05.jpg" %}


{% include assign-heading.html %}

```python
var1 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                    command=print_selection)
c1.pack()
```

参数`onvalue`和前面讲的部件`radiobutton`中的value相似，
当我们选中了这个checkbutton，`onvalue`的值1就会放入到`var1`中，
然后var1将其赋值给参数`variable`，`offvalue`用法相似，但是`offvalue`是在没有选中这个checkbutton时，`offvalue`的值1放入var1，然后赋值给参数`variable`
这是创建一个checkbutton部件，以此类推，可以创建多个checkbutton



{% include assign-heading.html %}

```python
def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):   #如果选中第一个选项，未选中第二个选项
        l.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1): #如果选中第二个选项，未选中第一个选项
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):  #如果两个选项都未选中
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')             #如果两个选项都选中
```

相对于前面学过的 `print_selection`，这一段比较长，其实功能差不多，只不过加了`if...elif...else`来选择控制而已即如代码注释，`config`在前面已经讲过就是将参数`text`的值显示，这里的`var1.get() == 1`
就是前面所说的var1获得的变量`onvalue=1`，`var1.get() == 0`即是`var1`获得的变量`offvalu=0`同理`var2`也是如此。

再补充一下 Tkinter 的[必备步骤](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk7_checkbutton.py){:target="_blank"},
整个框架的全部代码就完美了.