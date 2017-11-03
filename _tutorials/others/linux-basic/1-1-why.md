---
youku_id: XMzA5OTU1MzY3Mg
youtube_id: c8STJnGZPLQ
bilibili_id: 15976434
chapter: 1
title: Why Linux?
publish-date: 2017-10-11
thumbnail: /static/thumbnail/linux-basic/1-01.jpg
post-headings:
  - 为什么 Linux 是免费的
  - 比 Windows 更安全
  - 老电脑别丢 用 Linux 让它活起来
  - 安装方便简单
description: Linux 是一个开放式的系统, 而且最重要的是! 它是免费的!!免费的!!免费的!!最重要的事说三遍. 正因为他的免费, 开源, 大量的牛逼程序员涌入了 Linux, 他们在使用 Linux 的同时共同维护和更新着这个系统.
---

首先我想提一下我为什么做 Linux 的教程. 网站是"莫烦 Python", 按理说应该是做和 Python 有关的东西, 不过 Linux 是所有程序员应该了解的一个系统.
如果你做机器学习什么的, 很多时候你会发现, 一些模块, 比如 Tensorflow, Pytorch, 都是 Linux 支持最好. 为什么呢? 下面就有介绍啦.

而且我更想把这个 Linux 教程做成一个为机器学习方面的辅助. 因为很多时候, 机器学习的开发是基于 Linux 的, 所以 Linux 的一些使用技巧就必不可少.
在这个教程中, 我将提到 Linux 的一些基本使用原则和如何用它来辅助你训练机器学习, 神经网络, 强化学习. 下面就是我日常中使用 Mac 远程操控 Linux 的一个 demo.
至于为什么要弄远程呢, 原因很简单, 因为 Linux 的硬件比 Mac 好, 用 Mac 来编写文件, Linux 来训练, 合理分配资源.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/linux-basic/04-01-01.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>



{% include assign-heading.html %}

Linux 是一个开放式的系统, 而且最重要的是! 它是

**免费的!!**
**免费的!!**
**免费的!!**

最重要的事说三遍. 正因为他的免费, 开源, 大量的牛逼程序员涌入了 Linux, 他们在使用 Linux 的同时共同维护和更新着这个系统.
所以 Linux 的精髓就是, **永远开源** (哈哈, 和我做教程有着异曲同工之处, 这也是我为什么开始用 Linux 的原因).

{% include tut-image.html image-name="01-01-01.png" %}


相比 MacOS, 你得买一台昂贵的 Apple 电脑才能拥有, 或者 Windows 系统, 他每次升级你都得另掏腰包. 何必呢?

我们有时候仅仅只需要一台电脑, 他们能打打代码, 运行程序, 写写文档 (Linux 有类似于 Word/Excel 的软件), 上个网之类的. 与其花钱去买系统,
还不如就用个免费好用的 Linux 系统.





{% include assign-heading.html %}

为什么一个开源的系统会更安全? 为什么一个大家都能修改的系统会比一个封锁的系统更安全?

{% include tut-image.html image-name="01-01-02.jpg" %}

我们就从新闻说起, 你听说过一些比较著名的病毒吧, 比如[熊猫烧香病毒](https://baike.baidu.com/item/%E7%86%8A%E7%8C%AB%E7%83%A7%E9%A6%99){:target="_blank"},
[WannaCry](https://baike.baidu.com/item/WannaCry){:target="_blank"}吧.
他们都针对哪种电脑? 没错, 是 Windows! 为什么? 原因很简单, 太多人用 Windows 了, 企业, 政府, 银行等等. 做一个 Windows 的病毒往往比其他的有赚头多了.

而 Linux 的病毒, 非常少. 而且依赖于内部的一些安全机制, 使得 Linux 成为一个比较好的 "抗病毒" 系统. 如果想要详细了解的话, 这里有一个[知乎问答](https://www.zhihu.com/question/20656827){:target="_blank"}.




{% include google-in-article-ads.html %}



{% include assign-heading.html %}

随着时代的更新, 你是不是发现你身边的老电脑多了起来? 大一入学一台, 工作以后一台, 这样都有两台了. 旧电脑往往很多新程序带不起, 或者运行慢.
我们何不装个 Linux 让它重新活起来. 特别是想想, 家里的老人是不是不太懂电脑, 用电脑也不会做些什么事情, 上上网看看剧就好了, 给他们装个 Linux 多好. 简单好用.

{% include tut-image.html image-name="01-01-03.png" %}

Linux 的内核文件相对是算少的, 所以整个系统不用占你多少空间. 我就有这么一台大一入学的笔记本, 到现在已经有8年了. 原本 Windows 7 系统, 可是一运行就卡.
我装上了个 Ubuntu (一种比较流行的 Linux 分支), 电脑瞬间运行"光速", 上网什么都不卡了. (很多大学妹子不是觉得上网看剧卡嘛, 给她装个 Linux, 还显得你高大上了).



{% include assign-heading.html %}

{% include tut-image.html image-name="01-01-04.jpg" %}

Linux 的安装非常简单, 只要你有一台电脑, 不管它是不是笔记本或台式, 或者以前运行的是 Windows, 现在你都能给他装上 Linux.
你甚至都能装一个双系统, 保留以前的老系统, 开机的时候切换 Windows 和 Linux 来挑选你要使用的系统.
如果你已经蠢蠢欲动了, 就来看看我们下节内容, [安装一个 Linux 到你的电脑吧]({% link _tutorials/others/linux-basic/1-2-install.md %}).