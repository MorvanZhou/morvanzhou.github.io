---
youku_id: XMTYxMTIxNzY2NA
youtube_id: 0mwWNHfSu0Y
description: 使用 python 和 tkinter 来做简单的窗口程序. 制作一个简单的登录窗口练习.
chapter: 3
title: 例子 登录窗口3
date: 2016-11-3
post-headings:
  - usr_sign_up 界面
  - sign_to_Mofan_Python() 功能
author: 潘雨 (Mr_Pan)
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/tree/master/tkinterTUT/tk15_login_example){:target="_blank"}


这一次效果图是这样的：
{% include tut-image.html image-name="3-03-01.jpg" %}





{% include assign-heading.html %}


```python
window_sign_up = tk.Toplevel(window)
window_sign_up.geometry('350x200')
window_sign_up.title('Sign up window')
```

这一段首先是创建一个注册的窗口。这里和以往不同的是，多了一个`tk.Toplevel`我们打个比方，就好像我们前面所学
的`frame`一样，就是在编辑的功能下还有很多功能一样，这里就是在主体窗口的`window`上创建一个`Sign up window`窗口。

```python
new_name = tk.StringVar()#将输入的注册名赋值给变量
new_name.set('example@python.com')#将最初显示定为'example@python.com'
tk.Label(window_sign_up, text='User name: ').place(x=10, y= 10)#将`User name:`放置在坐标（10,10）。
entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)#创建一个注册名的`entry`，变量为`new_name`
entry_new_name.place(x=150, y=10)#`entry`放置在坐标（150,10）.

new_pwd = tk.StringVar()
tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
entry_usr_pwd.place(x=150, y=50)

new_pwd_confirm = tk.StringVar()
tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
entry_usr_pwd_confirm.place(x=150, y=90)

# 下面的 sign_to_Mofan_Python 我们再后面接着说
btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mofan_Python)
btn_comfirm_sign_up.place(x=150, y=130)
```

相信大家对这一段代码已经很熟悉了，因为这是大家前面所学过的知识。其实就是像我们平时所见的注册窗口有一样，在`Sign up window`窗口
上添加`new_name`，` new_pwd`， `new_pwd_confirm`，还有最后一个注册按钮。这里便于大家复习，我们将`new_name`这段详细介绍一下（如代码注释）。
到这里就完成了我们这个注册的主要界面用户名，密码，确认密码。效果图如下：

{% include tut-image.html image-name="3-03-02.jpg" %}





{% include assign-heading.html %}


```python
def usr_sign_up():
    def sign_to_Mofan_Python():
        ##以下三行就是获取我们注册时所输入的信息
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        ##这里是打开我们记录数据的文件，将注册信息读出
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)

        ##这里就是判断，如果两次密码输入不一致，则提示`'Error', 'Password and confirm password must be the same!'`
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')

        ##如果用户名已经在我们的数据文件中，则提示`'Error', 'The user has already signed up!'`
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')

        ##最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功`'Welcome', 'You have successfully signed up!'`
        ##然后销毁窗口。
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            ##然后销毁窗口。
            window_sign_up.destroy()
```

这里其实和前面所讲的`login`功能类似，如代码注释。

如果两次密码输入不一致，则提示`'Error', 'Password and confirm password must be the same!'`效果如图：

{% include tut-image.html image-name="3-03-03.jpg" %}


如果用户名已经在我们的数据文件中，则提示`'Error', 'The user has already signed up!'`效果如图：

{% include tut-image.html image-name="3-03-04.jpg" %}


注册成功就是我们一开始展示的效果图。

{% include assign-heading.html %}


到此，我们的这个程序已经完善。这里给大家奉上我们最后的实验成果。

{% include tut-image.html image-name="3-03-05.jpg" %}


