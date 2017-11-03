---
youku_id: XMzEyMTA0OTMzMg
youtube_id: Kp6RAGtWCew
bilibili_id: 15981580
chapter: 2
title: Linux 基本指令 nano 和 cat
publish-date: 2017-10-12
thumbnail: /static/thumbnail/linux-basic/2-04.jpg
post-headings:
  - nano
  - cat
description: "这次, 我们想要了解的是在 linux 中, 怎么样观看和编辑文件. nano 和 cat 能帮上你的忙."
---


这次, 我们想要了解的是在 linux 中, 怎么样观看和编辑文件. nano 和 cat 能帮上你的忙.



{% include assign-heading.html %}


`nano` 是 linux 的一款文字编辑工具. 我们可以拿它来做最基本的 terminal 端的文本编辑, 甚至可以写代码~
下面我们用 `touch` 创建一个 Python 脚本. 如果大家不懂 Python 也没关系, 你就知道我们可以拿 `nano` 来编辑文字或者脚本就好了.

{% include tut-image.html image-name="02-04-01.png" %}

然后用 `nano` 执行这个 `t.py` 文件.

```shell
$ nano t.py
```

他就会变成一个文本编辑器, 你在里面可以打上一些脚本, 比如像我这样.

{% include tut-image.html image-name="02-04-02.png" %}

然后按 "Ctrl + x" 来保存和退出. 如果提示你保存, 你就按一下 "y" 键, 然后回车, 你的文件就被保存下来了.

接着如果你在 terminal 中输入这个, 你就能看到 terminal 执行了你的 python 文件.

```shell
$ python t.py
This is a Python script!
```

(写给会 Python 的朋友: Ubuntu 安装好了以后自带 Python2.7 和 Python3.5的)








{% include google-in-article-ads.html %}

{% include assign-heading.html %}

`cat` (catenate) 可以用来显示文件内容, 或者是将某个文件里的内容写入到其他文件里. 我们举例说明.

1 查看文件内容

```shell
$ cat t.py
print("This is a Python script!")
```

2 `>` 将文件的内容放到另一个文件里

```shell
$ cat t.py > t1.py
$ cat t1.py
print("This is a Python script!")
```

3 `>` 将多个文件的内容打包一起放入另一个文件

比如这里我们把 `t.py` 和 `t1.py` 的内容同时放入了 `t2.py`,
如果在显示 `t2.py` 的时候, 它有两行 "print...".

```shell
$ cat t.py t1.py > t2.py
$ cat t2.py
print("This is a Python script!")
print("This is a Python script!")
```

4 `>>` 将内容添加在一个文件末尾

我创建了一个 `t3` 的文件, 文件里写上了 "This is t3". 我们将这个内容添加进 `t2.py` 吧.
使用了 `>>` 会将 `t3` 的内容添加在 `t2.py` 的末尾.

```shell
$ cat t3 >> t2.py
$ cat t2.py
print("This is a Python script!")
print("This is a Python script!")
This is t3.
```


