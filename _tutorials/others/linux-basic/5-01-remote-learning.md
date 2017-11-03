---
youku_id: XMzEzMTEzMDI3Ng
youtube_id: SST5xl4SVA8
bilibili_id: 15982592
chapter: 5
title: 自己的云计算, 把 Linux 当成你的云计算平台
publish-date: 2017-10-16
thumbnail: /static/thumbnail/linux-basic/5-01.jpg
post-headings:
  - 搭建 Linux 系统
  - 云端运行
  - 文件传输
  - 做 gym 的强化学习注意事项
description: "前面的内容都是为了这次的内容做的铺垫. 所以到了这节, 你已经学会了 Linux 的基本使用,
远程操控. 而现在网上有很多云计算平台. 是不是也想着拥有一个自己的云计算平台? 其实只要你手中有两台电脑, 你就能自己给搭建出一个云计算平台.
其中的原理是什么呢? 无非就是自己在一台电脑上开发, 然后将开发好的代码放在云端运算. 其实也就是一种远程控制的原理."
---

前面的内容都是为了这次的内容做的铺垫. 所以到了这节, 你已经学会了 Linux 的基本使用,
远程操控. 而现在网上有很多云计算平台. 是不是也想着拥有一个自己的云计算平台? 其实只要你手中有两台电脑, 你就能自己给搭建出一个云计算平台.
其中的原理是什么呢? 无非就是自己在一台电脑上开发, 然后将开发好的代码放在云端运算. 其实也就是一种远程控制的原理.

比如我有一台 Mac, 但我不想让我的 Mac 进行大规模运算, 原因如下:
* Mac 本来计算能力就弱
* 用 Mac 运算的时候肯定会卡, 但是我又想做其他东西, 太卡了不方便

手边若有一个计算能力强的 Linux, 大喜. 立马把它转成一个云计算平台~

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/linux-basic/04-01-01.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

接下来我们就来介绍具体的步骤应该是怎样.






{% include assign-heading.html %}

手动搭建一个以 Linux 为中心的云计算系统可以选择以下几种方式.

* 底层 SSH 操控 (MacOS/Linux) ([我的教程]({% link _tutorials/others/linux-basic/4-01-ssh-from-linux-or-mac.md %}))
* 底层 SSH 操控 (Windows) ([我的教程]({% link _tutorials/others/linux-basic/4-02-ssh-from-windows.md %}))
* VNC / TeamViewer 远程桌面 ([我的教程]({% link _tutorials/others/linux-basic/4-04-teamviewer-vnc.md %}))

如果你对上面的方法感兴趣, 推荐仔细观看上面几个教程. 把 Linux 搭建成一个服务器 server. 搭建方法, 在这几个教程中都有提到.

对于接下来的内容, 我会基于 SSH 的方法进行讲解, 因为如果你有了 VNC 或者 Teamviewer, 你能看见发生了什么, 这会很好办.
不过用 SSH 的好处就是, 快! 运行快! 传文件快!







{% include google-in-article-ads.html %}

{% include assign-heading.html %}

接下来我们举例来讲解, 假如我在操控端 (如 Mac) 写代码. 在我的 `Desktop` 文件夹下写好了一个 Python 脚本 `machine_learning.py`.
但是我想拿 Mac 来做点其他事, 不想让这个脚本在我的 Mac 上"发光发热", 那么我们就 ssh 远程推送到旁边空闲的 Linux 去运算吧.

比如这个 Python 脚本是这样的.

```python
import platform
a = 0
for i in range(9999):
    a += i
print("Finish job, result=%i" % a)
print("This is", platform.system())
```

然后[这个教程]({% link _tutorials/others/linux-basic/4-01-ssh-from-linux-or-mac.md %})一样,
在云端的 Linux 的 terminal 中输入 `ifconfig`, 找到我的 IP 是 `192.168.0.114`. 注意, 你的 IP 不一定和我的一样.
你需要自己确定. 然后确定你的云端 Linux 的用户名, 也就是你 Terminal 中 `@` 字符前面的名字. 我的是 `morvan`.
这个文件在我 Mac 的 Desktop 上. 我要在 Linux 云端运行的话, 就是下面这个命令.

```shell
$ ssh morvan@192.168.0.114 python3 < ~/Desktop/machine_learning.py

Finish job, result=49985001
This is Linux
```

注意这和我们之前用 SSH 类似, 不过这次我们加了一个 python 文件给服务器端. 这个文件的转换方式就用 `<` 来代替.
而且因为这是一个 Python3 文件, 所以我在 ip 后面写的是用 `python3` 在云端执行本地的这个文件.






{% include assign-heading.html %}

如果是有很多的 Python 文件怎么办呢? 有时候 Python 文件是一环扣一环, 这个文件里调用了那个文件的东西.
这时我们就能先全部复制所有必须文件去 Linux 的缓存区 或者 桌面, 然后再使用 ssh 在 Linux 云端的运行传送过去的文件.

比如我现在需要两个 Python 文件才能运行, `b.py` 如下:

```python
# This is b.py
def inner_func():
    print("This is a function in b")
```

还有一个 `a.py` 需要调用 `b.py` 才能运行.

```python
# This is a.py
from b import inner_func
inner_func()
```

接着我们要做的就是将这两个文件先复制去 Linux 云端, 然后在云端运行 `a.py`. 下面所有的操作都是在本地执行的, 我们没有跑去云端打代码.
输入 `scp` (secure copy), 加密传输复制 `~/Desktop/{a,b}.py` 在我桌面上的 `a.py` 和 `b.py` 两个文件到 云端`morvan@192.168.0.114`的桌面
`~/Desktop`

```shell
$ scp ~/Desktop/{a,b}.py morvan@192.168.0.114:~/Desktop

a.py                                          100%   37     6.3KB/s   00:00
b.py                                          100%   54     8.9KB/s   00:00
```

{% include tut-image.html image-name="05-01-01.png" %}

执行的话, 和上面的步骤有点不一样, 在本地用 ssh 去云端, 但是 ssh 的时候同时发送一条指令去执行 `a.py`.
这条指令我们用 `""` 给框起来, 说明是要发送去云端再执行的指令.

```shell
$ ssh morvan@192.168.0.114 "python3 ~/Desktop/a.py"

This is a function in b
```

同样, 如果你在云端的程序会产生一些结果文件, 我假设 `b.py` 是在云端运行完 `a.py` 而产生的新文件, 而我在本地电脑需要这个产生的文件.
我可以直接用 `scp` 的方式将这个 `b.py` 复制回来. 所以你会发现, `scp` 前一个参数是从哪开始复制, 后一个参数是复制去哪.
这样完了以后, 在我的 Mac 桌面上就产生了一个 `result` 文件.

```shell
$ scp morvan@192.168.0.114:~/Desktop/b.py ~/Desktop/result
```


这样一来一回, 我们总结一下走过的流程.

* 本地有要运行的文件
* 单个文件的话可以直接 ssh 去云端运行
* 多个文件可以先复制去云端, 然后在 ssh 运行
* 如果在云端有产生文件, 可以用 scp 复制回来






{% include google-in-article-ads.html %}

{% include assign-heading.html %}

如果你云计算的是强化学习, 而且有时候会要使用 gym 模块来模拟, 有一个事情需要注意.
如果不注意, 你有可能运行 python 会出错.

这个问题是, 如果你 ssh 在云端执行一个会打开窗口程序的指令, 比如用 ssh 在云端打开浏览器等,
默认是不允许的. 你必须设置一下这个参数. 比如我要打开 Firefox 浏览器窗口.
那么在 `firefox` 指令前, 需要加上 `export DISPLAY=:0`, 并用 `;` 隔开, 标明执行的先后顺序.

```shell
$ ssh morvan@192.168.0.114 "export DISPLAY=:0; firefox"
```

所以这个问题在强化学习中也存在, 如果你在强化学习的代码中有打开视窗的操作, 比如下面这句话会将 gym 模块的环境显示在屏幕上.


```python
# 在你的强化学习Python脚本中
env.render()
```

那么你就要用上面描述的方法执行这个脚本. 如果碰到类似的需要打开视窗的时候, 都需要这样做.

```shell
$ ssh morvan@192.168.0.114 "export DISPLAY=:0; python3 reinforcement_learning.py"
```