---
youku_id: XMTYxMDU1NTAyOA
youtube_id: Hj5sTDW-xqg
description: 使用 python 和 tkinter 来做简单的窗口程序. 弹出通知 messagebox 练习.
chapter: 2
title: messagebox 弹窗
date: 2016-11-3
post-headings:
  - messagebox部件
author: 潘雨 (Mr_Pan)
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk11_msgbox.py){:target="_blank"}



{% include assign-heading.html %}

其实这里的`messagebox`就是我们平时看到的弹窗。
我们首先需要定义一个触发功能，来触发这个弹窗
这里我们就放上以前学过的`button`按钮

```python
tk.Button(window, text='hit me', command=hit_me).pack()
```

通过触发功能，调用`messagebox`

```python
def hit_me():
   tk.messagebox.showinfo(title='Hi', message='hahahaha')
```

这里点击`button`按钮就会弹出提示对话窗

{% include tut-image.html image-name="2-10-01.jpg" %}

下面给出几种形式

```python
tk.messagebox.showinfo(title='',message='')#提示信息对话窗
tk.messagebox.showwarning()#提出警告对话窗
tk.messagebox.showerror()#提出错误对话窗
tk.messagebox.askquestion()#询问选择对话窗
```

如果给出如下定义就是打印出我们所选项对应的值

```python
def hit_me():
   print(tk.messagebox.askquestion(title='Hi', message='hahahaha'))
```

效果图

{% include tut-image.html image-name="2-10-02.jpg" %}

同样创建方法都是一样的形式，视频当中所给出的几种即

```python
    print(tk.messagebox.askquestion())#返回yes和no
    print(tk.messagebox.askokcancel())#返回true和false
    print(tk.messagebox.askyesno())#返回true和false
    print(tk.messagebox.askretrycancel())#返回true和false
```

再补充一下 Tkinter 的[必备步骤](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk11_msgbox.py){:target="_blank"},
整个框架的全部代码就完美了.