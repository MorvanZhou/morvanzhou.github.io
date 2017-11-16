---
youku_id: XMTg0MjA5NzM3Mg
youtube_id: BMKlINSwEas
bilibili_id: 16378030
description: "安装 git 的方式在每种系统中各不相同, 所以我们分开来说: (Linux 系统, MacOS 系统, Windows 系统)"
chapter: 1
title: Git 安装
publish-date: 2016-11-30

thumbnail: /static/thumbnail/git/1-02.jpg
post-headings:
  - Linux 系统
  - MacOS 系统
  - Windows 系统
---
学习资料:
  * [Git 官网安装说明](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git){:target="_blank"}

安装 git 的方式在每种系统中各不相同, 所以我们分开来说:


图个方便, 也可以直接上 git 的下载页面, 让网站自动识别你的系统, 并提供可用的下载文件:
[https://git-scm.com/downloads](https://git-scm.com/downloads){:target="_blank"}

{% include assign-heading.html %}

使用 Linux 的朋友们, 大家肯定都很熟悉怎么在 Linux 上装东西, 
所以只要找到你的 Terminal, 并输入以下指令就可以啦:

```shell
# 如果你的 Linux 是 Ubuntu:
$ sudo apt-get install git-all

# 如果你的 Linux 是 Fedora:
$ sudo yum install git-all
```

Linux 的更多 distribution 的安装, 请看[这里](https://git-scm.com/download/linux){:target="_blank"}

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

Git 已经为 Mac 用户做好了一个安装包, 我们可以在这里下载并安装 [https://git-scm.com/download/mac](https://git-scm.com/download/mac){:target="_blank"}

{% include tut-image.html image-name="1-2-1.png" %}

{% include assign-heading.html %}

Git 也为 Windows 系统提供了简易的 `.exe` 安装包, 直接从这里下载并安装就可以了: [https://git-scm.com/download/win](https://git-scm.com/download/win){:target="_blank"}

推荐使用默认安装参数, 然后一路`下一步`到底. 
安装好之后, 在你的所有程序中, 将会出现 git 的文件夹, 而且里面会有一个程序叫做
`git bash`. 这个 `git bash` 是 git 在 Windows 上为了方便使用所设置的一个 Unix 的环境.
如果你是 Windows 用户, 之后的教程你也能用这个来学习使用 git.

{% include tut-image.html image-name="1-2-2.png" %}
