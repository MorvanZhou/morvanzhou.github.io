---
youku_id: XMzEzMTAyOTEyNA
youtube_id: ap8wCYPwz6c
bilibili_id: 15982670
chapter: 4
title: 怎么样用 TeamViewer 和 VNC 从远程控制电脑
publish-date: 2017-10-16
thumbnail: /static/thumbnail/linux-basic/4-04.jpg
post-headings:
  - Teamviewer
  - VNC
  - 用 Mac 连接 VNC
  - 用 Windows 连接 VNC
  - 用 Linux 连接 VNC
description: "VNC 或者 Teamviewer 这种工具都是提供你一个可以远程图像化桌面的方式. 他们都是第三方软件.
比如下方是我用 Mac 通过局域网来远程操控可视化的 Linux 界面."
---

VNC 或者 Teamviewer 这种工具都是提供你一个可以远程图像化桌面的方式. 他们都是第三方软件.
比如下方是我用 Mac 通过局域网来远程操控可视化的 Linux 界面.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/linux-basic/04-04-01.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

接下来我们就来介绍 Teamviewer 和 VNC 这两款工具.


{% include assign-heading.html %}

Teamviewer 其实已经发展得很成熟了. 它是一个跨平台的远程操控软件. Windows, MacOS, Linux, 手机都可以下载使用.
它会通过外网, 将你的被控制电脑桌面投影到你的控制电脑上. 不过的流畅度, 速度大大取决于你的网速. 如果你是想做一个小规模, 控制局域网内(电脑都在同一个路由下)的电脑.
我觉得还是 VNC 快一点, 因为它不走外网. 当然, 最快的还是 SSH 啦, 都不用输出图像, 直接代码控制而已. 如果你对 SSH 的方式感兴趣, 这里有我制作的几节入门教程:

* [从 Mac 或 Linux 远程 ssh 控制 Linux]({% link _tutorials/others/linux-basic/4-01-ssh-from-linux-or-mac.md %})
* [从 Windows 远程 ssh 控制 Linux]({% link _tutorials/others/linux-basic/4-02-ssh-from-windows.md %})
* [从手机远程 ssh Linux]({% link _tutorials/others/linux-basic/4-03-ssh-from-phone.md %})

如果要用图像化的方式控制电脑, 首先我们从最方便的说起. [TeamViewer 的官网](https://www.teamviewer.com){:target="_blank"}提供了很多下载安装方式.

{% include tut-image.html image-name="04-04-02.png" %}

你可以根据你的系统选择, 而且如果是家用, 它就是免费的, 只有企业用才是收费.

他的程序界面是这样的, 功能其实很完善, 左面是一些你自己的信息, 你可以提供这些信息给你的朋友, 要他们控制这台电脑.
中间的区域是你可以利用朋友发来的信息来控制朋友的电脑. 右边的区域是你自己的管理区域, 你可以用一个账号管理你想连接的电脑.
这样非常方便.

{% include tut-image.html image-name="04-04-03.png" %}

不过就像之前说的. 这种远程控制是基于互联网的, 万一你网速不好, 而且你只想在局域网里用, 卡到想死的心都有.
所以这种情况你就可以考虑 VNC.





{% include google-in-article-ads.html %}

{% include assign-heading.html %}

其实 VNC 是一种软件的统称. 只要你的 Linux 架设好了一个服务器 (Server) 的 VNC, 客户端, 比如你的 Mac, 手机, 只要安装任何一种 VNC 客户端软件就能链接上服务器端的电脑啦.
如果你手头有一个 Raspberry Pi (树莓派), 会用 VNC 对你很实用.
那么首先, 我们就来设置这个服务器端的 VNC 吧. 打开你的 Linux 电脑, 打开 Terminal. 输入:

```shell
$ sudo apt-get install x11vnc
```

确认你的 Linux 用户密码, 就能安装这个最常用的 x11vnc 软件啦. 这个软件的使用, 设置非常简单.
安装好后, 最好给你的 x11vnc 设置一个密码. 我不设密码时, 用 Mac 还登不上, 一定要设完密码,用密码登录 Linux 的 VNC server 才能上.

所以设置密码的过程就是在你的 Linux Terminal 输入下面这样, 然后它会提示你要输入你要的密码, 这个密码是用来连接 VNC 的时候, 登录用的.

```shell
$ x11vnc -storepasswd

Enter VNC password:
Verify password:
Write password to /home/morvan/.vnc/passwd?  [y]/n y
Password written to: /home/morvan/.vnc/passwd
```

设置好之后, 在你的 Linux terminal 中输入下面指令, 要求用密码形式来开启 VNC 的 server.

```shell
$ x11vnc -usepw
```

**如果你使用的是 ubuntu 17.10, 截止至目前 (2017年10月27日) 对于 VNC 还有一个 bug 没有修复.
所以 17.10 版本的 Ubuntu 如果你尝试上面的方式发生下面这种问题, 你就要尝试一下我接下来说的方法了.**

```shell
X Error of failed request: BadMatch (invalid parameter attributes)
  Major opcode of failed request: 73 (X_GetImage)
  Serial number of failed request: 41
  Current serial number in output stream: 41
```

首先这个问题, 我查了很久, 最后发现是新版 ubuntu 的桌面显示升级了, 好像是变成3D, 然后以前的 2D 形式的 x11vnc 都不支持.
所以我们要换一种形式的桌面. 首先要做的就是 logout 你的电脑. 在桌面右上角, 选着你的用户, 然后 logout.

{% include tut-image.html image-name="04-04-031.png" %}

然后再选择不同的桌面方式 (Xorg) 登录 ubuntu. 这样一来, 如果再重复上面的 x11vnc 启动方式, 你就不会报错了.

{% include tut-image.html image-name="04-04-032.jpeg" %}

最后, 如果出现频繁跳出 x11vnc 的现象, 尝试在开启 x11vnc 的时候直接输入这个参数, 让它永远运行.

```shell
$ x11vnc -usepw -forever
```






{% include assign-heading.html %}

开启完之后, 使用 Mac 来连接 Linux 的 VNC 很方便, 在 Mac 中, 有一个软件叫 Screen Sharing.
打开它, 如果你 Linux 在局域网的 IP 地址(可以在 Linux 中输入 `ifconfig` 查到). 点 Connect,
最后输入你刚刚设置的 VNC 密码, 就能连上啦

{% include tut-image.html image-name="04-04-04.png" %}

{% include tut-image.html image-name="04-04-05.png" %}

{% include tut-image.html image-name="04-04-06.png" %}







{% include google-in-article-ads.html %}

{% include assign-heading.html %}

至于 Windows 呢, 其实有很多选项, 我们已经在 Linux 端设置好了一个 VNC server. 在 Windows 端, 我们需要的只是一个 VNC client.
而有很多软件可以实现 VNC client 这个功能.
我在下面列举一些:

* [TightVNC](http://www.tightvnc.com/){:target="_blank"} (免费)
* [RealVNC](https://www.realvnc.com/){:target="_blank"} (免费)

RealVNC 有两种选项, 一个是 [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/){:target="_blank"}, 用来做 client 端的(控制).
一个是 [VNC connect](https://www.realvnc.com/en/connect/download/vnc/){:target="_blank"}, 用来做 server 端的(被控制).

Client 端的 VNC 操作流程都很简单. 只要求要一个 server 端的 IP 和他的密码就好.






{% include assign-heading.html %}

Linux 的话, 它自带就有一个 VNC 软件. 只要你在右上角搜一下 "VNC", 那个被我圈出来的软件就是一个 Client 端的 VNC.
点开它, 输入 server 端的 IP 和他的密码就好.

{% include tut-image.html image-name="04-04-07.png" %}