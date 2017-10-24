---
youku_id: XMTYwNzAyODE5Mg
youtube_id: mS2kTW-4TLo
description: 使用 python 和 tkinter 来做简单的窗口程序. listbox 练习.
chapter: 2
title: Listbox 列表部件
date: 2016-11-3
author: 郭锡锋
post-headings:
  - 创建主窗口
  - 创建一个label用于显示
  - 创建一个方法用于按钮的点击事件
  - 创建一个按钮
  - 创建一个Listbox和变量var2，并将var2的值赋给Listbox
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/tkinterTUT/tk4_listbox.py){:target="_blank"}

{% include assign-heading.html %}

```python
window = tk.Tk()
window.title('my window')
window.geometry('200x200')
```

{% include assign-heading.html %}

```python
var1 = tk.StringVar()    #创建变量
l =tk.Label(window,bg='yellow',width=4,textvariable=var1)
l.pack()
```

{% include tut-image.html image-name="2-03-01.png" %}

{% include assign-heading.html %}

```python
def print_selection():
    value = lb.get(lb.curselection())   #获取当前选中的文本
    var1.set(value)     #为label设置值
```

{% include assign-heading.html %}

```python
b1 = tk.Button(window, text='print selection', width=15,
              height=2, command=print_selection)
b1.pack()
```

{% include tut-image.html image-name="2-03-02.png" %}

{% include assign-heading.html %}

```python
var2 = tk.StringVar()
var2.set((11,22,33,44)) #为变量设置值

#创建Listbox

lb = tk.Listbox(window, listvariable=var2)  #将var2的值赋给Listbox

#创建一个list并将值循环添加到Listbox控件中
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end', item)  #从最后一个位置开始加入值
lb.insert(1, 'first')       #在第一个位置加入'first'字符
lb.insert(2, 'second')      #在第二个位置加入'second'字符
lb.delete(2)                #删除第二个位置的字符
lb.pack()

#显示主窗口
window.mainloop()
```

{% include tut-image.html image-name="2-03-03.png" %}


