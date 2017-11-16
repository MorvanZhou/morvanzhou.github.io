---
youku_id: XMTg0MjE3NzE1Ng
youtube_id: obbH1hGB5GI
bilibili_id: 16378055
description: "我们先要确定要把哪个文件夹里的文件进行管理. 比如说我桌面上的一个叫 gitTUT 的文件夹.
然后在 Terminal (Windows 的 git bash) 中把当前目录调到这个文件夹 gitTUT,
我的做法是这样"
chapter: 2
title: 第一个版本库 Repository
publish-date: 2016-11-30

thumbnail: /static/thumbnail/git/2-01.jpg
post-headings:
  - 创建版本库 (init)
  - 添加文件管理 (add)
  - 提交改变 (commit)
  - 流程图
---





{% include assign-heading.html %}

我们先要确定要把哪个文件夹里的文件进行管理. 比如说我桌面上的一个叫 `gitTUT` 的文件夹.
然后在 Terminal (Windows 的 git bash) 中把当前目录调到这个文件夹 `gitTUT`,
我的做法是这样: 

```shell
$ cd ~/Desktop/gitTUT
```

为了更好地使用 git, 我们同时也记录每一个施加修改的人. 这样人和修改能够对应上.
所以我们在 git 中添加用户名 `user.name` 和 用户 email `user.email`:

```shell
$ git config --global user.name "Morvan Zhou"

$ git config --global user.email "mz@email.com"
```

然后我们就能在这个文件夹中建立 git 的管理文件了:

```shell
$ git init
# Initialized empty Git repository in /Users/MorvanZhou/Desktop/gitTUT/.git/
```

因为这个文件夹中还没有任何的文件, 它返回出来一句话告诉我们已经建立了一个空的 git 管理库.

{% include assign-heading.html %}

通常我们执行 `$ ls` 就能看到文件夹中的所有文件, 不过 git 创建的管理库文件 `.git` 是被隐藏起来的.
所以我们要执行这一句才能看到被隐藏的文件:

```shell
$ ls -a
# .	..	.git
```

建立一个新的 `1.py` 文件:

```shell
$ touch 1.py
```

现在我们能用 `status` 来查看版本库的状态:

```shell
$ git status

# 输出
On branch master    # 在 master 分支

Initial commit

Untracked files:    
  (use "git add <file>..." to include in what will be committed)

	1.py        # 1.py 文件没有被加入版本库 (unstaged)

nothing added to commit but untracked files present (use "git add" to track)
```

现在 `1.py` 并没有被放入版本库中 (unstaged), 所以我们要使用 `add` 把它添加进版本库 (staged):

```shell
$ git add 1.py

# 再次查看状态 status
$ git status

# 输出
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   1.py    # 版本库已识别 1.py (staged)
```

如果想一次性添加文件夹中所有未被添加的文件, 可以使用这个:

```shell
$ git add .
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

我们已经添加好了 `1.py` 文件, 最后一步就是提交这次的改变, 并在 `-m` 自定义这次改变的信息:

```shell
$ git commit -m "create 1.py"

# 输出
[master (root-commit) 6bd231e] create 1.py
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 1.py
```

{% include assign-heading.html %}

整个上述过程可以被这张 git 官网上的流程图直观地表现:

{% include tut-image.html image-name="2-1-1.png" %}
