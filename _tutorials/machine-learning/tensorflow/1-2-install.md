---
youku_id: XMTg0MjcwMDc0NA
youtube_id: EXsn02rMWX8
bilibili_id: 16001888
description: 安装 Tensorflow 时需要注意的几点
chapter: 1
title: Tensorflow 安装
publish-date: 2016-11-30
thumbnail: /static/thumbnail/tf/tf2-install.jpg
date: 2016-11-3
post-headings:
  - 多种安装途径
  - Linux 和 MacOS
  - Windows
  - 测试
  - 更新 Tensorflow
---


学习资料:
  * 官方关于 Tensorflow 安装的 [说明](https://www.tensorflow.org/versions/master/get_started/os_setup.html){:target="_blank"}

安装 Tensorflow 时需要注意的几点:

1. MacOS, Linux, Windows 系统均已支持 Tensorflow
2. 确定你的 python 版本
3. 你的 GPU 是 NVIDIA, 就可以安装 GPU 版本的 Tensorflow; 你的 GPU 不是 NVIDIA 也没有关系, 安装 CPU 版本的就好了.

{% include assign-heading.html %}

Tensorflow 的安装方式很多. 比如官网提供的:

* [Pip 安装](https://www.tensorflow.org/versions/master/get_started/os_setup.html#pip-installation){:target="_blank"}
* [Virtualenv 安装](https://www.tensorflow.org/versions/master/get_started/os_setup.html#virtualenv-installation){:target="_blank"}
* [Anaconda 安装](https://www.tensorflow.org/versions/master/get_started/os_setup.html#anaconda-installation){:target="_blank"}
* [Docker 安装](https://www.tensorflow.org/versions/master/get_started/os_setup.html#docker-installation){:target="_blank"}
* [从安装源 安装](https://www.tensorflow.org/versions/master/get_started/os_setup.html#installing-from-sources){:target="_blank"}

这节内容使用 pip 在每个系统的安装方式:


{% include assign-heading.html %}

本文将提到第一种最简单的安装方式, pip 安装.
使用 pip 安装的时候要确保你的 pip 已经存在于你的电脑中. 如果还没有安装 pip. 
你可以在 Terminal 窗口中运行这个, 升级必要的组件:

```shell
# Ubuntu/Linux 64-位 系统的执行代码:
$ sudo apt-get install python-pip python-dev

# Mac OS X 系统的执行代码:
$ sudo easy_install --upgrade pip
$ sudo easy_install --upgrade six
```

<h5 id="LM-CPU">CPU 版</h5>

激动人心的时刻到了, Tensorflow (0.12之后) 做了更新, 绕过了复杂的安装步骤, 如果你只需要安装
CPU 版本的 Tensorflow, 运行下面这个就好了:

```shell
# python 2+ 的用户:
$ pip install tensorflow

# python 3+ 的用户:
$ pip3 install tensorflow
```

注意: 你需要8.1或更高版的 `pip` 才能顺利安装.

<h5 id="LM-GPU">GPU 版</h5>

Tensorflow 已经不再支持 mac 的 GPU 版了, 下面是 Linux 安装 GPU 版的说明.
说先安装 NVIDIA CUDA 必要组建.

```shell
$ sudo apt-get install libcupti-dev
```

然后确保你的 linux 上 pip 是可用的, 接着我们可以直接通过pip 安装:

```shell
$ sudo apt-get install python-pip python-dev   # for Python 2.7
$ sudo apt-get install python3-pip python3-dev # for Python 3.n
```

然后选择你想要cpu 或者 gpu 版本.

```shell
$ pip install tensorflow      # Python 2.7; CPU support (no GPU support)
$ pip3 install tensorflow     # Python 3.n; CPU support (no GPU support)
$ pip install tensorflow-gpu  # Python 2.7;  GPU support
$ pip3 install tensorflow-gpu # Python 3.n; GPU support
```





{% include google-in-article-ads.html %}

{% include assign-heading.html %}

tf 在 windows 的官方[安装说明](https://www.tensorflow.org/install/install_windows){:target="_blank"}
, 其实就简单的方法就是装个 [Anaconda](https://www.continuum.io/downloads){:target="_blank"}, 省了你安装这安装那, 不知道还有什么没安装的烦恼.
如果你喜欢用 pip 安装, 通过西面这个途径就好了.


安装前的检查:

* 目前只支持 **Python 3.5/3.6 (64bit)** 版本
* 你有安装 numpy (没有的话,请看这里[numpy 安装教程]({% link _tutorials/data-manipulation/np-pd/1-2-install.md %}))

接下来惊心动魄啦! 在 command 窗口中执行

```shell
# CPU 版的
C:\> pip3 install --upgrade tensorflow

# GPU 版的
C:\> pip3 install --upgrade tensorflow-gpu
```

**注意**

* Windows 运行 Tensorflow 如果遇到这个报错:

```
Error importing tensorflow.  Unless you are using bazel,
you should not try to import tensorflow from its source directory;
please exit the tensorflow source tree, and relaunch your python interpreter
from there.
```

不要惊慌, 尝试下载安装 [Windows 的 Microsoft Visual C++ 2015 redistributable update 3 64 bit](https://www.visualstudio.com/downloads/){:target="_blank"}.
就能解决这个问题.

* 或者在 Windows 运行的时候出现了如下报错, 你需要安装 [Windows 的 Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/confirmation.aspx?id=48145){:target="_blank"} 就能成功解决问题.

```
ImportError: No module named '_pywrap_tensorflow_internal'
```







{% include assign-heading.html %}

然后打开你的 python 编辑器, 输入

```python
import tensorflow
```

运行脚本来检查一下是否有正确安装.


{% include assign-heading.html %}

最后, 如果你需要升级 Tensorflow 的版本, 推荐的方式是:

根据你的 python 版本, 在 terminal 中删除原有的版本

```shell
# 如果你是 Python 2, 请复制下面
pip uninstall tensorflow

# 如果你是 Python 3, 请复制下面
pip3 uninstall tensorflow
```

然后重复这个安装教程的步骤, 从头安装新版本.
