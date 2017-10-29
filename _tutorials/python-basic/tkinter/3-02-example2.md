---
youku_id: XMTYxMTE0NjM1Mg
youtube_id: E9REgHVes6c
description: 使用 python 和 tkinter 来做简单的窗口程序. 制作一个简单的登录窗口练习.
chapter: 3
title: 例子 登录窗口2
date: 2016-11-3
post-headings:
  - 触发的 usr_login 功能
author: 潘雨 (Mr_Pan)
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/tree/master/tkinterTUT/tk14_login_example){:target="_blank"}



这一次效果图是这样的：

{% include tut-image.html image-name="3-02-01.jpg" %}






{% include assign-heading.html %}

```python
##这两行代码就是获取用户输入的`usr_name`和`usr_pwd`
usr_name = var_usr_name.get()
usr_pwd = var_usr_pwd.get()

##这里设置异常捕获，当我们第一次访问用户信息文件时是不存在的，所以这里设置异常捕获。
##中间的两行就是我们的匹配，即程序将输入的信息和文件中的信息匹配。
try:
    with open('usrs_info.pickle', 'rb') as usr_file:
        usrs_info = pickle.load(usr_file)
except FileNotFoundError:
 ##这里就是我们在没有读取到`usr_file`的时候，程序会创建一个`usr_file`这个文件，并将管理员
 ##的用户和密码写入，即用户名为`admin`密码为`admin`。
    with open('usrs_info.pickle', 'wb') as usr_file:
        usrs_info = {'admin': 'admin'}
        pickle.dump(usrs_info, usr_file)

```

这一部分就是将用户输入的用户名和密码获取到，和我们保存在`usr_file`中的数据对比。针对正确的密码和错误的密码分别对待.

```python
#如果用户名和密码与文件中的匹配成功，则会登录成功，并跳出弹窗`how are you?`加上你的用户名。
if usr_name in usrs_info:
    if usr_pwd == usrs_info[usr_name]:
        tk.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
    ##如果用户名匹配成功，而密码输入错误，则会弹出'Error, your password is wrong, try again.'
    else:
        tk.messagebox.showerror(message='Error, your password is wrong, try again.')
else:   # 如果发现用户名不存在
    is_sign_up = tk.messagebox.askyesno('Welcome',
                           'You have not sign up yet. Sign up today?')
    # 提示需不需要注册新用户
    if is_sign_up:
        usr_sign_up()
```

下面是用户名存在但是一个密码正确, 一个密码错误.

{% include tut-image.html image-name="3-02-01.jpg" %}

{% include tut-image.html image-name="3-02-02.jpg" %}



下面是用户不存在, 提示需不需要注册一个新的用户.

{% include tut-image.html image-name="3-02-03.jpg" %}

因为本节只是定义`usr_sign_up`并没有实质功能，所以选择之后没有太大变化。
这一部分就是匹配的主要内容，如果匹配成功，就会登录进去，否则就会失败。


本节主要是详细介绍登录功能，下节会继续完善注册命令。
最后在把上一节做好的界面补充就可以了。本节全套代码在莫烦的 [github](https://github.com/MorvanZhou/tutorials/tree/master/tkinterTUT/tk14_login_example){:target="_blank"} 中可以找到.
