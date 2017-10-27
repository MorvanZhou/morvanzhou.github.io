---
youku_id: XMTYxMTEyNDIyNA
youtube_id: 3yVR0H5lhso
description: 使用 python 和 tkinter 来做简单的窗口程序. 制作一个简单的登录窗口练习.
chapter: 3
title: 例子 登录窗口1
date: 2016-11-3
post-headings:
  - 界面创建
  - 触发功能
author: 潘雨 (Mr_Pan)
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/tree/master/tkinterTUT/tk13_login_example){:target="_blank"}


这一次效果图是这样的：

{% include tut-image.html image-name="3-01-01.jpg" %}

都是前面熟悉的参数。为了防止大家忘记，特意加上代码注释。





{% include assign-heading.html %}

```python
# welcome image
canvas = tk.Canvas(window, height=200, width=500)#创建画布
image_file = tk.PhotoImage(file='welcome.gif')#加载图片文件
image = canvas.create_image(0,0, anchor='nw', image=image_file)#将图片置于画布上
canvas.pack(side='top')#放置画布（为上端）
```

这里创建的就是我们效果图中的`welcome`, 如果你想使用和我一样的 welcome 的图片, 你可以在[这里](/static/results/tkinter/3-01-02.gif)下载。

```python
# user information
tk.Label(window, text='User name: ').place(x=50, y= 150)#创建一个`label`名为`User name: `置于坐标（50,150）
tk.Label(window, text='Password: ').place(x=50, y= 190)

var_usr_name = tk.StringVar()#定义变量
var_usr_name.set('example@python.com')#变量赋值'example@python.com'
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)#创建一个`entry`，显示为变量`var_usr_name`即图中的`example@python.com`
entry_usr_name.place(x=160, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')#`show`这个参数将输入的密码变为`***`的形式
entry_usr_pwd.place(x=160, y=190)
```

这里就是创建我们熟悉的登录界面，就是常见的用户名，密码。

```python
# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)#定义一个`button`按钮，名为`Login`,触发命令为`usr_login`
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)
```

这里定义的就是我们的登录按钮。








{% include assign-heading.html %}

```python
def usr_login():
    pass
def usr_sign_up():
    pass
```

本节我们只是把登录的界面做出来，并没有对触发功能详细的去定义。等下节会继续完善这个例子。
再补充一下 Tkinter 的[必备步骤](https://github.com/MorvanZhou/tutorials/tree/master/tkinterTUT/tk13_login_example){:target="_blank"},
整个框架的全部代码就完美了.