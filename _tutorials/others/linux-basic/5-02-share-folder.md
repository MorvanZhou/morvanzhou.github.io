---
youku_id: XMzEzMTIyNDg0NA
youtube_id: ud1N7P25ZMI
bilibili_id: 15982562
chapter: 5
title: 自己的云计算, 多电脑共享你云端文件
publish-date: 2017-10-30
thumbnail: /static/thumbnail/linux-basic/5-02.jpg
post-headings:
  - 设置分享文件夹
  - Mac 找到云端的分享文件夹
  - Windows 找到云端的分享文件
  - 其他电脑上编辑/运行云端文件
description: "云端计算固然方便, 如果让你的电脑上直接显示云端的文件, 是不是更方便呢? 哈哈, 这次我就来探讨一下可行的方式."
---

云端计算固然方便, 如果让你的电脑上直接显示云端的文件, 是不是更方便呢? 哈哈, 这次我就来探讨一下可行的方式.

假设你的情况是这样:
* 有两台电脑(其中一台是 Linux)
* 电脑们都在同一个局域网 (LAN, 同一个路由器下)
* 想把那台 Linux 当做云端, 做云计算, 又不想来回复制文件
* 能不能把云端的某个文件夹分享到我的本地, 在本地及时修改这个共享文件夹的文件
* 不是云计算也行, 只是想在几台电脑中共享文件

如果你也是这样, 恭喜你, 这个教程非常适合你. 我经常直接在 Mac 上的文件管理器使用 Linux 里的文件.

{% include tut-image.html image-name="05-02-01.png" %}








{% include assign-heading.html %}

我们可以单独创建一个要分享的文件夹, 这样你就知道自己要将哪个文件夹里的文件分享给大家了.
比如说, 在 Linux 的 Home 目录下创建一个 Shared 文件夹. 你可以用鼠标来创建或者直接在 terminal 中输入指令.

```shell
$ mkdir ~/Shared/
```

{% include tut-image.html image-name="05-02-02.png" %}

有了这个 Shared 文件夹以后, 我们来对这个文件夹动手脚. 右键选择 `Local Network Share`,
之后你会跳出来一个 Folder Sharing 的窗口, 在这个窗口中, 勾选 Share this folder.

{% include tut-image.html image-name="05-02-03.png" %}

如果你第一次做这件事, 当你选定的时候, 应该会出现上面那个要求安装东西的窗口, 点击 `install` 就好, 他会帮你安装必要组建.
安装好之后, 还会弹出一个重启 session 的窗口, 重启它. 然后给你的这个文件夹起一个 "响亮" 的名字, 这个名字会出现在其它的电脑上.
所以, 我就起了一个名字叫 "Shared". 哈哈.

{% include tut-image.html image-name="05-02-04.png" %}

最后如果你会在其它电脑上编辑这个 "Shared" 里的文件, 那你就需要勾选 "Allow others to create and delete files in this folder".
我觉得最下面那个选项不要选比较好, 如果选了, 任何在这个局域网内的人都能"玩弄"你的文件. 你肯定不想这样.

这还不够, 在 terminal 中, 我们最好给这个分享文件设置一个密码. 如果有人想要登录这个分享文件, 就需要密码登录.
设置密码的步骤很容易, 你只要在**云端的 terminal** 中输入下面内容, 将分享文件夹的账号密码设置成你 linux 用户的账号密码就好了, 好记又方便.

```shell
$ sudo smbpasswd -a 用户名      # 比如下面我的用户名是 morvan
$ sudo smbpasswd -a morvan
```

之后它会要求你输入用户名的密码, 然后再设置分享的密码 `New SMB password`, 再 `Retype new SMB password`. 完了以后就大功告成,
你就能在其它电脑上找到这个文件夹, 使用这个用户名和密码查看文件啦.










{% include google-in-article-ads.html %}

{% include assign-heading.html %}


Windows 找到共享的文件也非常简单, 只需要找到你的局域网电脑们就好了. 当你打开文件浏览器. 找到 "网络", 或者是"网上邻居"
然后找到你的 Linux 电脑, 输入之前设置的账号密码. 就能查看你共享的 Linux 文件夹啦.

{% include tut-image.html image-name="05-02-08.jpg" %}











{% include assign-heading.html %}


我们已经设置好的云端的共享文件. 接着就是在其他电脑上找到这个共享文件. 我用 MacOS 来演示一遍.
首先你需要找到这个共享的地方. 打开你的 `Finder` 文件管理器, 然后在上面的菜单中找到 `Go`, 点击 `Network`,

{% include tut-image.html image-name="05-02-05.png" %}

然后找到你的计算机名, 我这里是 `MORVAN-LINUX`, 之后点击 `connect as`, 这个意思是说要登录上之前设置好的账号密码.
如果没有经过这一步, 是无法打开 "Shared" 文件夹的.

{% include tut-image.html image-name="05-02-06.png" %}

点击 `connect as` 之后, 我们就按要求填写刚刚的你在 Linux 上设置的账号密码就好.

{% include tut-image.html image-name="05-02-07.png" %}

最后成功登录上, 你就能用这个云端文件夹的内容啦.

{% include tut-image.html image-name="05-02-01.png" %}

现在我就能直接在我的 Mac 上编辑云端的文件, 比如做一个 Python 的项目, 然后 [SSH]({% link _tutorials/others/linux-basic/4-01-ssh-from-linux-or-mac.md %})
去 Linux 云端运行这个写好的文件. 方便又不占你 Mac 的空间.
