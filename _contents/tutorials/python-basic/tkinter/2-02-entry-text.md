---
youku_id: XMTYwNzAwNTY0NA
youtube_id: lVcM_V3KqOE
description: 使用 python 和 tkinter 来做简单的窗口程序. entry 和 text 练习.
chapter: 2
title: Entry & Text 输入, 文本框
date: 2016-11-3
author: 郭锡锋
post-headings:
  - 窗口主体框架
  - 窗口内容（窗口上的控件）
  - 测试一下
---
{% assign post-heading-count = -1 %}
学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk3_entry_text.py)


{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>

每一个tkinter应用的主体框架都包含以下几部分：

- 主窗口: `window`，及主窗口的一些基本属性（标题、大小）
- 让窗口活起来：`window.mainloop()`

```python
import tkinter as tk

window = tk.Tk()
window.title('my window')

##窗口尺寸
window.geometry('200x200')

##显示出来
windo.mainloop()
```

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>

创建按钮分别触发两种情况

```python
b1 = tk.Button(window,text="insert point",width=15,height=2,command=insert_point)
b1.pack()

b2 = tk.Button(window,text="insert end",command=insert_end)
b2.pack()
```

创建输入框entry，用户输入任何内容都显示为*

```python
e = tk.Entry(window,show='*')
e.pack()
```

创建一个文本框用于显示

```python
t = tk.Text(window,height=2)
t.pack()
```

定义触发事件时的函数（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）

```python
def insert_point():
    var = e.get()
    t.insert('insert',var)

def insert_end():
    var = e.get()
    t.insert('end',var)
```

窗口界面

<img class="course-image" src="/static/results/tkinter/2-02-01.png">

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>

第一次：在entry中输入`tkinter`，在text中输入`0000`并将光标定位在中间位置，点击`insert point`

<img class="course-image" src="/static/results/tkinter/2-02-02.png">

第二次：点击`insert end`

<img class="course-image" src="/static/results/tkinter/2-02-03.png">
