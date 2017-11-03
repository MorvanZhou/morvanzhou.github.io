---
youku_id: XMzExNzAzODg5Ng
youtube_id: 04xmnJT5dcE
bilibili_id: 15980889
chapter: 1
title: 给你的 Ubuntu 安装软件
publish-date: 2017-10-11
thumbnail: /static/thumbnail/linux-basic/1-04.jpg
post-headings:
  - 使用 Ubuntu 自带的 app 管理器
  - 中文输入
  - 其他方式安装
description: "其实在 Ubuntu 上, 已经有很多安装好的 app 了. 比如已经有火狐浏览器(Firefox), 可替代 Windows Office 的办公套件 (LibreOffice) 等等.
不过你仍然可以继续安装你需要的软件 app. "
---

学习资料:
* [Ubuntu 自己的功能简介](https://www.ubuntu.com/desktop/features){:target="_blank"}


其实在 Ubuntu 上, 已经有很多安装好的 app 了. 比如已经有火狐浏览器(Firefox), 可替代 Windows Office 的办公套件 (LibreOffice) 等等.
不过你仍然可以继续安装你需要的软件 app.

{% include tut-image.html image-name="01-04-01.png" %}




{% include assign-heading.html %}


{% include tut-image.html image-name="01-04-02.png" %}

你可以直接在左上角的图标中搜索 "software", 就能找到 Ubuntu 自带的一个 App store. 这可跟 MacOS 的 App store 像极了!
闲着没事无聊, 你就能在里面找找需要的软件. 大多数主流的 App 都能找到.

{% include tut-image.html image-name="01-04-03.png" %}

下图是 Apple 的 App store, 有木有! 像不像! 以前用 Apple, 现在是无缝转接 Linux 呀.

{% include tut-image.html image-name="01-04-04.png" %}

所以你缺什么软件, 直接上 App store 先找找, 安装就好了.





{% include assign-heading.html %}

我们用的是中文, 所以有时候还得有个中文输入法就好. 这个你可以在 Setting 中进行设置.
如果想直接使用系统里面的中文输入, 你要做的就是在 `Region & Language` 里添加一个中文输入就行.

{% include tut-image.html image-name="01-04-05.png" %}
{% include tut-image.html image-name="01-04-051.png" %}
{% include tut-image.html image-name="01-04-052.png" %}

接着在 `Region & Language` 下面有一个 `Manage Installed Languages` 里的 "install/remove language" 添加一个 Chinese 就好了.

{% include tut-image.html image-name="01-04-06.png" %}

然后使用的时候, 在右上角的菜单栏里面就可以选择不同的输入法了 (切换方法 Home+space, 或者按 linux 的说法 super+space).

在国内, 很多人喜欢搜狗输入法(我也喜欢), 所以我这里有个搜狗输入法的[下载链接](https://pinyin.sogou.com/linux/?r=pinyin){:target="_blank"}.
还有这里的[官方安装说明](https://pinyin.sogou.com/linux/help.php){:target="_blank"}.




{% include google-in-article-ads.html %}

{% include assign-heading.html %}

很多时候, 你也会发现, Linux 的 App 安装是用代码来实现的. 如果你熟了, 你会觉得用代码来安装才是 Linux 的魅力.

所以有时候你在 Ubuntu 的 App store 找不到合适的软件, 但是网上却有非官方的, 但是你需要的软件. 很多情况下, 你会使用 Terminal, 用代码来安装 App.
找到 Terminal 的方式很简单, 直接在左上角搜 "Terminal" 就好了.

{% include tut-image.html image-name="01-04-07.png" %}

然后在窗口里输入这么一句话:

```shell
$ sudo apt-get install 你的App名字
```

比如我想安装一个浏览器, 名字叫 "chromium-browser" 我就要在 terminal 中输入

```shell
$ sudo apt-get install chromium-browser
```

做好心理准备, 如果你越深入 Linux, 使用代码处理事情的情况就越多. 这里为用代码来学 Linux 开了头,
后面的教学, 我们就来深入了解有哪些好用的代码, 让你完全控制你的电脑~

