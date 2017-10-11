---
youku_id:
youtube_id:
chapter: 1
title: 安装 Ubuntu
publish-date: 2017-10-11
thumbnail: /static/thumbnail/linux-basic/1-02.jpg
post-headings:
  - 选一个 Linux distribution
  - 下载 Ubuntu
  - 使用 USB 安装 Ubuntu
  - 正式安装
  - 开机启动 Ubuntu
description: "其实 Linux 不只是一个系统, 他是很多系统的集合, 可以想象成这样, Linux 就是 Android,
而 Android 还有小米的 米UI, 魅族的UI, 锤子的UI, OPPO 的UI 等等.
所以实际上要使用的不是 Linux 本身, 而是 Linux 下面的各种 UI.
而像 Android 那样, 他也有很多 UI. 比如 ubuntu"
---





{% include assign-heading.html %}

其实 Linux 不只是 "一个系统", 他是很多系统的集合, 可以想象成这样, Linux 就是 Android,
而 Android 还有小米的 米UI, 魅族的UI, 锤子的UI, OPPO 的UI 等等.
所以实际上要使用的不是 Linux 本身, 而是 Linux 下面的各种 "UI".
而像 Android 那样, 他也有很多 "UI". 比如:

* [CentOS](https://www.centos.org/)
* [Debian](https://www.debian.org/)
* [Mint](https://linuxmint.com/)
* [Ubuntu](https://www.ubuntu.com/)
* 等等等等

<img class="course-image" src="/static/results/linux-basic/01-02-01.jpg" alt="{{ page.title }}{% increment image-count %}">


在这个教程中, 我们不是为了区分各种 OS 的不同, 而是学着使用它, 所以我们会挑选一个最常用的, 流传最广的 OS 来学习.
这个就是 Ubuntu~ 接着我们就来看如何在原本为 Windows 的电脑安装 Ubuntu 吧.





{% include assign-heading.html %}

首先要做的事, 当然就是跑去人家官网下载啦. 在这里我推荐使用英文版的 Ubuntu, 因为学习 Linux, 我们基本上都是和英文打交道.
所以如果系统本来就是英文的, 将会方便很多. 如果你实在喜欢中文的, 有一款中文的 [Ubuntu 麒麟](http://www.ubuntukylin.com/)系统可以推荐你.
下面是你需要的下载链接:

* [Ubuntu 英文系统](https://www.ubuntu.com/download/desktop) (推荐)
* 或者 [Ubuntu 麒麟 中文系统](http://www.ubuntukylin.com/downloads/)

我推荐英文的, 所以接下来会基于英文的说. 点开链接, 你会看到这个下载页面. 上面写着一些下载要求(通常被忽略). 点击 Download 他通常会带你去一个 donation 的界面.
如果你支持开源, 可以大方地赞助他们, 就像你点击"莫烦 Python"上面的[赞助](/support/)链接一样~

<img class="course-image" src="/static/results/linux-basic/01-02-02.png" alt="{{ page.title }}{% increment image-count %}">

下载好以后 (大概1.6GB), 你会有类似这样的一个文件 `ubuntu-16.04.3-desktop-amd64.iso`. 这就是 Ubuntu 的桌面版安装文件.

接着我们将这个文件加载进一个 USB, 这个很简单.





{% include google-in-article-ads.html %}



{% include assign-heading.html %}

如果你想练习英文能力, 这里是 [Ubuntu 的官方 USB 安装教程](https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-windows?_ga=2.242174530.1746861324.1507700161-1586045268.1507700161#0),
我下面的 USB 安装说明也是基于他们的解说.

USB安装要求:
* 有一个 2GB 或更大的 USB (或移动盘), **注意:你的USB 应该会被清空, 请备份里面的文件**
* 从 Windows 变成 Ubuntu 的比较多, 所以我们准备工作基于 Windows
* 官方推荐 [Rufus](https://rufus.akeo.ie/), 一个将 Ubuntu OS 转到 USB 的免费软件
* 上面已下载好的 Ubuntu 镜像文件

所以我们直接点 [Rufus](https://rufus.akeo.ie/), 然后找到下面的下载链接.

<img class="course-image" src="/static/results/linux-basic/01-02-03.png" alt="{{ page.title }}{% increment image-count %}">

由于Rufus版本的更新, 你看到的可能和这张图有点不同, 不过通常选第一个下载链接就好了. 安装好 Rufus 之后, 按照下面步骤.

* 打开 Rufus
* 插好你的 USB
* Rufus 会在 "Device" 这个地方显示你的 USB
* 如果没有显示你的 USB 名字, 点击它, 会有下拉菜单, 然后选你的 USB

<img class="course-image" src="/static/results/linux-basic/01-02-04.png" alt="{{ page.title }}{% increment image-count %}">

在 *Partition scheme and target system type* 选 **MBR partition scheme for UEFI**.
然后在 *Create a bootable disk using* 后面点击那个图标, 选择你下载好的类似于这样 `ubuntu-16.04.3-desktop-amd64.iso` 的文件.


<img class="course-image" src="/static/results/linux-basic/01-02-05.png" alt="{{ page.title }}{% increment image-count %}">

<img class="course-image" src="/static/results/linux-basic/01-02-06.png" alt="{{ page.title }}{% increment image-count %}">


{% include google-in-article-ads.html %}

其他的设置就不要更改了, 直接点击 **start**, 你会看到这个窗口, 然后点击那个 Recommended 选项, 最后点 OK 就行.

<img class="course-image" src="/static/results/linux-basic/01-02-07.png" alt="{{ page.title }}{% increment image-count %}">

大功告成, 最后等进度条跑完就好了.




{% include assign-heading.html %}

完成上面的步骤, 接下来就是安装 Ubuntu 了.

<img class="course-image" src="/static/results/linux-basic/01-02-08.png" alt="{{ page.title }}{% increment image-count %}">

首先把你刚弄好的 USB 插在电脑上, 然后重启电脑, 通常你需要修改一下电脑的启动项顺序 "BIOS". 其实这个很简单, 你去网上搜搜 "你电脑的牌子+BIOS" 就会找到你在启动时需要按什么键才能设置启动项了.
比如说我在戴尔或联想上需要按 F2, 有些电脑不同 (可能是 F12), 所以要查一下. 什么时候按(**狂按**) F2? 当你的电脑开机出现下面界面的时候就要按(**狂按**)了.

<img class="course-image" src="/static/results/linux-basic/01-02-09.jpg" alt="{{ page.title }}{% increment image-count %}">

<img class="course-image" src="/static/results/linux-basic/01-02-10.jpg" alt="{{ page.title }}{% increment image-count %}">

然后你会看到类似下面的界面(不是所有电脑都这样, 你的可能不同, 但是基本内容都类似). 使用键盘的左右建调整到 "BOOT" 的 tag 上, 然后使用上下键选到你的 USB
(通常写着 USB 或者 Removable 的字). 然后使用"+-"键调整它的位置, 将它调到第一个. 最后 F10 保存设置, 退出.

<img class="course-image" src="/static/results/linux-basic/01-02-11.png" alt="{{ page.title }}{% increment image-count %}">

之后再重启, 你的电脑就会使用你的 USB 启动, 然后跳到这个界面. 你看得没错, 在安装之前, 你甚至可以在 USB 上直接运行这个系统. Linux 牛逼吧, 给你最高的体验感.
不想体验的话, 你就直接点 install 安装就好.

<img class="course-image" src="/static/results/linux-basic/01-02-12.png" alt="{{ page.title }}{% increment image-count %}">

接着, 全部选了吧, 省得以后自己还要安装.

<img class="course-image" src="/static/results/linux-basic/01-02-13.png" alt="{{ page.title }}{% increment image-count %}">

接着, 你要有个抉择, 是想装个双系统呢? 还是想清除之前的系统, 然后电脑里只有 Ubuntu 系统.

* 选 **Install Ubuntu alongeside Windows 7** 就是装双系统.
* 选 **Erase disk and install Ubuntu** 就是清除老系统再装 (危险动作).

<img class="course-image" src="/static/results/linux-basic/01-02-14.png" alt="{{ page.title }}{% increment image-count %}">

你如果选了 **Install Ubuntu alongeside Windows 7**, 接下来就是这个界面, 你将要选择要分配多少空间给 Ubuntu 系统. 只需要拖动中间的分割线就能分配空间大小了.
然后确定安装就好.

<img class="course-image" src="/static/results/linux-basic/01-02-15.jpg" alt="{{ page.title }}{% increment image-count %}">

最后就是设置一些你的时区, 账号, 密码等, 都很容易了, 大家都能自己搞定.

当你看到这个的时候, 就大功告成啦.

<img class="course-image" src="/static/results/linux-basic/01-02-16.png" alt="{{ page.title }}{% increment image-count %}">


{% include assign-heading.html %}

如果你选的是装成双系统, 每次开机的时候, 你会看到这样一个界面, 让你来选择要启动哪个系统. 你可以选 ubuntu 或者 Windows.
方便简单吧.

<img class="course-image" src="/static/results/linux-basic/01-02-17.jpg" alt="{{ page.title }}{% increment image-count %}">
