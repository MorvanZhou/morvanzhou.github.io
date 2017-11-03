---
youku_id: XMzEyMTA2ODY5Mg
youtube_id: bOx-SA5ONqI
bilibili_id: 15982080
chapter: 3
title: Linux 文件权限
publish-date: 2017-10-13
thumbnail: /static/thumbnail/linux-basic/3-01.jpg
post-headings:
  - ls 查看权限
  - chmod 修改权限
  - 一个使用 Python 的技巧
description: "在 Linux 中, 权限是一个非常重要的东西. 无时无刻不影响着你的操作. 就像有时候, 你想去百度云下载一些别人分享的文件,
可是你却发现虽然你能看到文件但是你却不能下载, 这就是一种权限. 在 Linux 中, 这种权限随处可见. 你可以设置, 让别人不能越界."
---


在 Linux 中, 权限是一个非常重要的东西. 无时无刻不影响着你的操作. 就像有时候, 你想去百度云下载一些别人分享的文件,
可是你却发现虽然你能看到文件但是你却不能下载, 这就是一种权限. 在 Linux 中, 这种权限随处可见. 你可以设置, 让别人不能越界.

不过像我这种人, 也就一台电脑, 一个用户, 涉及不到多少权限的问题. 如果你也像我, 只有你自己在用 Linux 的电脑,
主要用它来运行你的代码. 我教你一招修改权限, 方便运行你的 Python 脚本的招数.

这节内容不会涉及过深的权限管理. 我们了解一些基础, 方便你拿你的 Linux 跑机器学习的代码就好. 如果你想扩展学习的话, 网上会有很多教程.



{% include assign-heading.html %}

查看文件权限的方法很简单, 其实之前我们就已经看到过这样的内容了, 如果你还记得. 我们在说 `ls` 指令的时候, 提到过权限问题,
不过到了这节内容我们仔细说说权限. 如果你在 Terminal 中输入图片中的指令.

{% include tut-image.html image-name="03-01-01.png" %}

1 在 Terminal 中查看文件的权限

```shell
$ ls -l
total 16
----rw-r-- 1 morvan morvan 34 Oct 12 09:51 t1.py
-rw----r-- 1 morvan morvan 80 Oct 12 09:57 t2.py
-rw-rw-r-- 1 morvan morvan 12 Oct 12 09:56 t3
-rwxrw-r-- 1 morvan morvan 55 Oct 13 17:28 t.py
```

在这里, 像`-rw-rw-r--`这种, 就是权限的说明. 细节展示在下面的图中. 在下图中,
这串字符得拆成4个部分,

{% include tut-image.html image-name="03-01-02.png" %}

* `Type`: 很多种 (最常见的是 `-` 为文件, `d` 为文件夹, 其他的还有`l`, `n` ... 这种东西, 真正自己遇到了, 网上再搜就好, 一次性说太多记不住的).
* `User`: 后面跟着的三个空是使用 User 的身份能对这个做什么处理 (`r` 能读; `w` 能写; `x` 能执行; `-` 不能完成某个操作).
* `Group`: 一个 Group 里可能有一个或多个 user, 这些权限的样式和 User 一样.
* `Others`: 除了 User 和 Group 以外人的权限.

如果有朋友对 User, group, others 这几个没什么概念的话, 我这里补充一下.
User 一般就是指你, 这个正在使用电脑的人. Group 是一个 User 的集合, 最开始创建新 User 的时候, 他也为这个 User 创建了一个和 User 一样名字的 Group, 这个新 Group 里只有这个 User.
一般来说, 像一个企业部门的电脑, 都可以放在一个 Group 里, 分享了一些共享文件和权限. Others 就是除了上面提到的 User 和 Group 以外的人.

好了, 有了这些理解, 我们拿上面的 `t1.py` 来举例.
我们可以将 `----rw-r--` 拆成 `-` (这是文件), `---`(这个 user 没有任何权限), `rw-` (这个 Group 里可以读,写), `r--` (其他人只能读).


{% include tut-image.html image-name="03-01-03.png" %}

如果我双击这个 `t1.py` 上面就弹出这个说我们权限的窗口.








{% include google-in-article-ads.html %}

{% include assign-heading.html %}

好了, 我们知道了这些权限的问题, 那我们如何改写权限呢? `chmod` (change mode) 就是来干这个的.

通常的修改形式是

```shell
$ chmod [谁][怎么修改] [哪个文件]
```

举个最简单的例子, 现在的 `t1.py` 是 `----rw-r--`, 如果我们想让你(user)有读的能力. 下面这样改就行了.

```shell
$ chmod u+r t1.py
$ ls -l
-r--rw-r-- 1 morvan morvan 34 Oct 12 09:51 t1.py
```

这里的 `u+r` 很形象, User + read, 给 t1.py 这个修改. 所以我们的修改形式就能总结出下面这样.

[谁]
* `u`: 对于 User 修改
* `g`: 对于 Group 修改
* `o`: 对于 Others 修改
* `a`: (all) 对于所有人修改

[怎么修改]
* `+`, `-`, `=`: 作用的形式, 加上, 减掉, 等于某些权限
* `r`, `w`, `x` 或者多个权限一起, 比如 `rx`

[哪个文件]
* 施加操作的文件, 可以为多个

我们再举几个例, 巩固一下.

```shell
-rw----r-- 1 morvan morvan 80 Oct 12 09:57 t2.py
-rw-rw-r-- 1 morvan morvan 12 Oct 12 09:56 t3
-rwxrw-r-- 1 morvan morvan 55 Oct 13 17:28 t.py

$ chmod u-r t2.py
$ ls -l t2.py
--w----r-- 1 morvan morvan 80 Oct 12 09:57 t2.py

$ chmod g+x-w t3
$ ls -l t3
--w-r-xr-- 1 morvan morvan 12 Oct 12 09:56 t3
```

除了上面这些修改形式, 还有一些简化版的形式, 不过我觉得不天天用权限这东西, 了解上面就够了.
如果你想更深的了解, 网上搜搜 "linux 权限 数字表示" 对你会有帮助.




{% include assign-heading.html %}

我不怎么用权限这东西, 但是我却发现给 python 文件添加权限 `x` 还算有用的. 为什么这么说?
因为通常, 如果一个 `.py` 没有 `x` 权限, 在 terminal 中你就需要这样执行:

```shell
$ python3 t.py
This is a Python script!
```

如果你有了 `x` (可执行权限), 你运行这个文件可以直接这样打:

```shell
$ ./t.py
This is a Python script!
```

如果你天天要运行这个脚本, 每次运行的时候少几个字还是挺好的. 如果你决定要这样做, 你在这个 Python 脚本的开头还需要加一句话.

```python
#!/usr/bin/python3        # 这句话是为了告诉你的电脑执行这个文件的时候用什么来加载

print("This is a Python script!")
```
