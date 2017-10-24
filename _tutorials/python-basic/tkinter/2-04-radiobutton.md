---
youku_id: XMTYwODA4MDIyMA
youtube_id: nun-fQIJsZE
chapter: 2
title: Radiobutton 选择按钮
date: 2016-11-3
description: "这次我们会讲到 radiobutton, 就是我们常常看到的单选按钮, tkinter 来实现这个功能非常简单"
post-headings:
  - radiobutton 部件
  - 触发功能
author: 潘雨（Mr_Pan）
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk5_radiobutton.py){:target="_blank"}


这一次的效果将会像下面的图片一样.

{% include tut-image.html image-name="2-04-01.png" %}

如果选择了某个选项, 效果就会如下.

{% include tut-image.html image-name="2-04-02.png" %}

{% include tut-image.html image-name="2-04-03.png" %}


{% include assign-heading.html %}

首先我们需要定义一个 `var` 用来将 radiobutton 的值和 Label 的值联系在一起.
然后创建一个radiobutton部分:

```python
var = tk.StringVar()
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

r1 = tk.Radiobutton(window, text='Option A',
                    variable=var, value='A',
                    command=print_selection)
r1.pack()
```

其中`variable=var`, `value='A'`的意思就是，当我们鼠标选中了其中一个选项，把value的值`A`放到变量var中，然后赋值给`variable`





{% include assign-heading.html %}

我们将定义一个功能, 用来对选择的 radiobutton 进行操作.
`print_selection` 功能就是选择了某个 radiobutton 后我们会在屏幕上打印的选项.

```python
def print_selection():
    l.config(text='you have selected ' + var.get())
```

当触发这个函数功能时，我们的 `label` 中就会显示 `text` 所赋值的字符串即 'you have selected',
后面则是我们所选中的选项 `var.get()`就是获取到变量 `var` 的值，
举个例子就是我们一开始所做的将选项 "option A" 选中时的值以 "A" 放入 `var` 中，
所以获取的也就是A 即如果我们这时候选中 "option A" 选项，label显示的值则是 "you have selected A".

再补充一下 Tkinter 的[必备步骤](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk5_radiobutton.py){:target="_blank"},
整个框架的全部代码就完美了.



