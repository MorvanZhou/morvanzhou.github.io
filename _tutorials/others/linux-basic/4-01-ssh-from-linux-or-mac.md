---
youku_id: XMzEyMTE0MzY2NA
youtube_id: Jo9OlO5cvn0
bilibili_id: 15981900
chapter: 4
title: 怎么样从 MacOS 或 Linux 通过 SSH 远程 Linux
publish-date: 2017-10-16
thumbnail: /static/thumbnail/linux-basic/4-01.jpg
post-headings:
  - 给 Linux 安装 OpenSSH
  - Mac 或 Linux SSH 去 Linux
  - 省略密码直接登录
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






{% include assign-heading.html %}

现在你的 Linux 是一个可以被 SSH 登录的状态了. 我们先从 MacOS 或者是你另一台 Linux 远程这台 Linux 开始.
因为 MacOS 和 Linux 都是类似的系统, 所以操作起来比 Windows 简单.

我有 Mac, 所以使用 Mac 来 demo 具体操作, 这个操作和你用 Linux 操作 SSH 是一样的. 你只需要打开 Mac 上的 Terminal.
然后输入:

```shell
$ ssh [要控制的用户名]@[它的IP地址]
```

举个例子, 我要用 mac 来操控的 Linux 的用户名叫做 morvan, morvan 这台 linux 的 ip 地址可以这样获取.
首先, 回到要控制的 Linux 上, **确保你操控和被操控的两台电脑连接上了同一个路由器. 然后在你 被操控 电脑的 terminal 上输入这个获取 被操控 电脑的 ip 号码**.

```shell
$ ifconfig
```

如果它提示你没有安装 `ifconfig`, 你就按它的要求安装就好. 输入下面指令就能安装.

```shell
$ sudo apt install net-tools
```

确保 `ifconfig` 能用后, 输入 `ifconfig`, 接着找到以 inet 开头的字样, 这就是你在这个路由下的 ip 地址了. 比如我现在的 ip 是 `192.168.0.114`

```
inet addr:192.168.0.114
```

找好了 ip (`192.168.0.114`), 知道你被操控电脑的用户名 (`morvan`), 现在回到操控电脑的 terminal (我的 Mac).
在 terminal 中输入之前提到的 ssh 开头的命令. 然后它就会要求你输入被操控的 Linux 的用户密码. 很显然, 只有知道密码的人才能登陆你的 Linux,
不然就太容易被黑了.


```shell
$ ssh morvan@192.168.0.114
morvan@192.168.0.114's password:
```

**有可能你在尝试这样直接 ssh 的方式失败. 像我, 刚从16版的 Ubuntu 升级到 17 版, 我的 Mac 由于某些原因不让我 ssh 去 17 版的 Ubuntu,
显示了下面的报错, 后来查了一下, 找到了一个解决方式.**

```shell
ERROR: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
ERROR: @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
ERROR: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
ERROR: IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
ERROR: Someone could be eavesdropping on you right now (man-in-the-middle attack)!
........
ERROR: ECDSA host key for 192.168.0.114 has changed and you have requested strict checking.
ERROR: Host key verification failed.
```

如果你也看到上面这种报错, 直接在你的电脑上 (我的 Mac 上) 的 terminal 运行下面这个:

```shell
$ ssh-keygen -R 要 ssh 去的 ip 比如下面这样
$ ssh-keygen -R 192.168.0.114
```

恢复正常后, 接着再按上面的步骤 ssh 去 Ubuntu. 输入, 确认密码后, 你在操控电脑的 terminal 就会瞬间变成被操控电脑的 terminal 啦. 他会显示这样一些信息证明你登录成功.
现在你就能自由的运用之前所学的 Linux 的指令, 在你的电脑上远程操控 Linux 电脑啦.

```shell
Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-96-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

147 packages can be updated.
53 updates are security updates.

Last login: Sun Oct 15 00:21:56 2017 from 192.168.0.104
morvan@morvan-Latitude-E5550:~$
```








{% include google-in-article-ads.html %}

{% include assign-heading.html %}

不过你还可以更进一步, 现在你每 SSH 登录一次 Linux, 都需要输入密码, 如果你登录次数很频繁, 而却你的密码又设置得很长,
这就非常麻烦. 还好, 我们可以通过提前设置一个"保密协议", 来让你的 Linux 识别出哪些电脑能不用密码登录. 这就是 `public/private rsa key`.

我们将在 Mac 或者 Linux (控制电脑) 上生成一个 `public/private keypair` (共锁和私锁), 然后将共锁(public key) 复制到要被远程的 Linux 上.
这样当你有私锁的控制电脑要远程操控这台有共锁的 Linux, 他会帮你识别配对的. 就不用每次都要输入被远程的电脑密码了.

所以首先我们还是用我的 Mac demo, 在 mac 的 Terminal 上输入指令 `ssh-keygen` 创建共锁和私锁, 它会提示你要保存这些锁的地方.
我们就用它默认的地方比较好. 所以回车确定.

```shell
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/MorvanZhou/.ssh/id_rsa):
```

确定后, 它会弹出下面这个, 要你来确定你是否想要一个保障密码, 如果你确定你的局域网是安全的, 这个都可以不填.
我就不填, 所以我直接回车.

```shell
Enter passphrase (empty for no passphrase):
```

然后它会要求你再次确认, 回车

```shell
Enter same passphrase again:
```

最后, 它会显示类似于这样的东西告诉你, 你的锁都已经生成好了.

```shell
Your identification has been saved in /Users/MorvanZhou/.ssh/id_rsa.
Your public key has been saved in /Users/MorvanZhou/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:yVr3PAPmxVO1lBd7KvqBsBCZSE8mdYce8mjBiUfRDVE MorvanZhou@Morvan
The key's randomart image is:
+---[RSA 2048]----+
|    o=*++*E    o+|
|   ..**++..   .o+|
|    ..=* .    .oo|
|      ooo. . . ..|
|     .. S + = .  |
|       + * B o   |
|      . . + *    |
|           . +   |
|            .    |
+----[SHA256]-----+
```


接着, 我们就要将这个生成好的 "公锁" 给复制去你的 被控制的 Linux. 指令结构还是和上面一样.

```shell
$ ssh-copy-id [被控制的用户名]@[它的ip]
```

我被控制的 Linux 用户叫 morvan, 他的 IP, 我通过了上面描述的方式找到了. 所以我就输入下面这样.
回车后他会要求你输入一次 被控制端电脑的密码.

```shell
$ ssh-copy-id morvan@192.168.0.114

/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/Users/MorvanZhou/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
morvan@192.168.0.114's password:
```

密码正确后, 它将输出, 并告诉你的怎么用 ssh 登录被控制端的电脑.

```shell
Number of key(s) added:        1

Now try logging into the machine, with:   "ssh 'morvan@192.168.0.114'"
and check to make sure that only the key(s) you wanted were added.
```

最后, 我们开开心心地在 Mac/Linux ssh 被控制的电脑吧~ 这次登录的时候没有被要求输入任何密码~

```shell
$ ssh morvan@192.168.0.114

Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-96-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

147 packages can be updated.
53 updates are security updates.

Last login: Mon Oct 16 08:36:26 2017 from 192.168.0.111
```

下一节内容, 我们来看看如何在 Windows 上实现这个 ssh 功能.