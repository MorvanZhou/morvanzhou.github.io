---
youku_id: XMzEzMTEzNjg4NA
youtube_id: p3HfHK3lCzk
bilibili_id: 15982077
chapter: 4
title: 怎么样从手机 (Android安卓/IOS苹果) 通过 SSH 远程 Linux
publish-date: 2017-10-16
thumbnail: /static/thumbnail/linux-basic/4-03.jpg
post-headings:
  - 给 Linux 安装 OpenSSH
  - 手机 SSH 的 app
description: "像下面这个 Demo 一样, 如果有时候身边没有第二台电脑, 我们完全可以用一台手机来控制你的 Linux. 不管是 iPhone 还是 Android 安卓.
他们都会有很多 SSH 的 app 提供下载. 有了这些. 我们躺在床上都能控制电脑啦"
---

像下面这个 Demo 一样, 如果有时候身边没有第二台电脑, 我们完全可以用一台手机来控制你的 Linux. 不管是 iPhone 还是 Android 安卓.
他们都会有很多 SSH 的 app 提供下载. 有了这些. 我们躺在床上都能轻松控制电脑啦~

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/linux-basic/04-01-02.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

所以这个教程对需要远程控制 Linux 的朋友非常有帮助. 能大大提高你的生产率. 并且 SSH 是一种加密的通信通道, 也能保证你的安全.

首先强调一点, 这套"远程"操控的方法实际上也不是真正的远程. 这节的教程教你的方法是在一个局域网内远程操控电脑 (在一个路由器下).
你当然可以把它做成在互联网中的远程操控, 不过技术难度上加了一个等级, 如果你想是想人在公司, 却要操控家里的 Linux, 有一个方便免费的软件 ([TeamViewer](https://www.teamviewer.com){:target="_blank"}) 可以提供你参考.

在家中同一个路由器下, 我们完全可以使用 VNC 或者 SSH 来实现远程操控 (VNC 就是一个将你 Linux 屏幕输出到另一台电脑上的软件, SSH 则是将你现在电脑的 Terminal 链接上 Linux Terminal, 用代码控制 Linux).
使用 SSH 将会更加顺畅 (VNC 输出桌面图像会卡), 所以如果你有能力, 那就尽量使用 SSH 吧. 这节内容, 我们来说说怎么样使用 SSH. 下节内容我们接着说 VNC 和 TeamViewer.



{% include assign-heading.html %}

为了实现 SSH 功能, 你得确定你的 Linux 上有安装了 SSH 服务, 通常可能是没有安装的. 所以我们将要安装一个开源的 SSH 工具, 叫做 OpenSSH, 将你的 Linux 变成一个服务器 (就是像你访问网站一样访问你的 Linux).
在 Linux 上打开你的 Terminal, 然后输入下面这句话安装 openssh-server. `sudo` 是使用管理员权限的意思, 所以回车后它可能要求你输入你用户密码.

```shell
$ sudo apt-get install openssh-server
```

如果你之前没有安装过, terminal 会提示你将要有多少东西被安装, 需要你确认. 确认完了以后, 它将会帮你继续安装.







{% include google-in-article-ads.html %}

{% include assign-heading.html %}

安卓里有很多 ssh 的 app. 苹果肯定也不少. 其实你只要用 "SSH" 搜搜 app store 里面. 里面就会有非常多的可用 app. 我以 "JuiceSSH" 举例.
其他的应该都大同小异.

{% include tut-image.html image-name="04-03-01.png" %}

下载好 "JuiceSSH". 打开你的这个 app, 如果你还没有创建过任何 ssh 链接. 你将需要点击 "Connections",
自己创建一个连接.

{% include tut-image.html image-name="04-03-02.png" %}

下一步中, 我们唯一需要的就是你要连接去, ssh 去的 IP 地址. 在你的 Linux terminal 中输入
`ifconfig` 获得你现在的 IP 地址, 一个以 `inet` 开头的地址, 通常是 192.168.0.xxx
如果你的 `ifconfig` 指令不管用, 说明你还没有安装一个东西,
所以在 terminal 下输入

```shell
$ sudo apt install net-tools
```

就能使用 ifconfig 了.
然后将找到的 ip 地址原封不动的放在 "Address" 这一栏中. 接着点击右上角的那个勾确定添加这个连接.

{% include tut-image.html image-name="04-03-03.png" %}

确定后它会跳出一个窗口, 让你确认你要连接上的电脑是否是你真正要连接上的电脑. 如果你在自己家中的路由器下, 就不用担心, 别人也很难黑得了你. 如果你在一个公用路由下.
你还是得再三检查一下, 免得到时候被黑客攻击.

{% include tut-image.html image-name="04-03-04.png" %}

然后就是输入你 Linux 电脑的用户密码了. 确认后你就能在手机上正常使用 ssh 控制你的 Linux 电脑.

{% include tut-image.html image-name="04-03-05.png" %}

{% include tut-image.html image-name="04-03-06.png" %}

加上前面用 MacOS, Windows 和这节用手机 ssh 去 Linux 的教程, 我相信, 你正开心地倒腾着.
不过有时候你不太适应用 terminal 来操控电脑. 想要用一个可视化的界面更直观的操控 Linux 电脑.
后面要提到的 VNC 和 Teamviewer 就是你要了解的啦~