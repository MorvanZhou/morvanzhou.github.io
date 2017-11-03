---
youku_id: XMzEzMDkxMTUyNA
youtube_id: RkqVvzlY6V0
bilibili_id: 15982085
chapter: 4
title: 怎么样从 Windows 通过 SSH 远程 Linux
publish-date: 2017-10-16
thumbnail: /static/thumbnail/linux-basic/4-02.jpg
post-headings:
  - 给 Linux 安装 OpenSSH
  - Windows SSH 软件 PuTTY
description: "使用 ssh 远程操作 Linux 我觉得是我用得最多的一种形式了. 我有一台 MacBook pro,
但是我的 Linux 电脑硬件稍微好一点. 所以我很多时候是在 Mac 上写代码, 用 Apple 的朋友你懂的, 它的屏幕的确不错,
写起代码来眼睛舒服. 下面的视频就是我通常在做的事情. 甚至有时候你好能用手机来控制 Linux!!! 牛逼吧!"
---

使用 ssh 远程操作 Linux 我觉得是我用得最多的一种形式了. 我有一台 MacBook pro,
但是我的 Linux 电脑硬件稍微好一点. 所以我很多时候是在 Mac 上写代码, 用 Apple 的朋友你懂的, 它的屏幕的确不错,
写起代码来眼睛舒服. 下面的视频就是我通常在做的事情.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/linux-basic/04-01-01.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

甚至有时候你好能用手机来控制 Linux!!! 牛逼吧!

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/linux-basic/04-01-02.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>


所以这个教程对需要远程控制 Linux 的朋友非常有帮助. 能大大提高你的生产率. 并且 SSH 是一种加密的通信通道, 也能保证你的安全.


首先强调一点, 这套"远程"操控的方法实际上也不是真正的远程. 这节的教程教你的方法是在一个局域网内远程操控电脑 (在一个路由器下).
你当然可以把它做成在互联网中的远程操控, 不过技术难度上加了一个等级, 如果你想是想人在公司, 却要操控家里的 Linux, 有一个方便免费的软件 ([TeamViewer](https://www.teamviewer.com){:target="_blank"}) 可以提供你参考.

在家中同一个路由器下, 我们完全可以使用 VNC 或者 SSH 来实现远程操控 (VNC 就是一个将你 Linux 屏幕输出到另一台电脑上的软件, SSH 则是将你现在电脑的 Terminal 链接上 Linux Terminal, 用代码控制 Linux).
使用 SSH 将会更加顺畅 (VNC 输出桌面图像会卡), 所以如果你有能力, 那就尽量使用 SSH 吧. 这节内容, 我们来说说怎么样使用 SSH. 之后的内容我们接着说 VNC 和 TeamViewer.



{% include assign-heading.html %}

为了实现 SSH 功能, 你得确定你的 Linux 上有安装了 SSH 服务, 通常可能是没有安装的. 所以我们将要安装一个开源的 SSH 工具, 叫做 OpenSSH, 将你的 Linux 变成一个服务器 (就是像你访问网站一样访问你的 Linux).
在 Linux 上打开你的 Terminal, 然后输入下面这句话安装 openssh-server. `sudo` 是使用管理员权限的意思, 所以回车后它可能要求你输入你用户密码.

```shell
$ sudo apt-get install openssh-server
```

如果你之前没有安装过, terminal 会提示你将要有多少东西被安装, 需要你确认. 确认完了以后, 它将会帮你继续安装.







{% include google-in-article-ads.html %}

{% include assign-heading.html %}

在 Windows 上, SSH 不像 Linux 和 MacOS 那样常用, 而且 Windows 的系统内核也和 Linux 不太一样.
所以我们用一个软件来实现 SSH 比较合适. PuTTY 是一个开源, 免费, 而且常被使用的 SSH 软件. 首先, 我们得下载这个软件.

[PuTTY 下载页面](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html){:target="_blank"}

在这个下载界面中, 你会看到类似这样的界面, 确认你 Windows 电脑是多少位的 (32-bit 或 64-bit), 然后选择一个适合你电脑的 `.msi` 安装包.

{% include tut-image.html image-name="04-02-01.png" %}

安装好之后, 在开始菜单中找到 PuTTY, 并打开 PuTTY, 你会看到下面这样. 然后在 "Host name (or IP address)" 那填上被控制的 Linux 的 IP.
获取被控制 Linux IP 的方法就是在这台 Linux 的 terminal 上输入:

```shell
$ ifconfig
```

如果它提示你没有安装 `ifconfig`, 你就按它的要求安装就好. 输入下面指令就能安装.

```shell
$ sudo apt install net-tools
```

确保 `ifconfig` 能用后, 输入 `ifconfig`, 然后找和 `inet addr` 有关的那一串 IP 地址. 之后将这个 IP 地址输入到你的 PuTTY 的 "Host name (or IP address)" 位置.
默认情况下, 是不用修改 port 的数值的.

{% include tut-image.html image-name="04-02-02.png" %}

点击 Open 按钮, 你就能登录 Linux 啦, 它还会跳出一个小窗, 让你确认这台电脑是不是你要链接的电脑. 如果你在自己家的局域网内,就不用担心安全问题,
直接点 Yes 就好.

{% include tut-image.html image-name="04-02-03.png" %}

最后你需要输入 Linux 的用户密码作为确认. 然后就能顺利开始在 Windows 上操控 Linux 啦.
这里我用 Windows 操控了一下我的 Raspberry Pi, 树莓派. 一个微型电脑的 Terminal.

{% include tut-image.html image-name="04-02-04.png" %}



