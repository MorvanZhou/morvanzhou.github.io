---
youku_id: XMTg0MjcwMDc0NA
youtube_id: EXsn02rMWX8
description: 安装 Tensorflow 时需要注意的几点
chapter: 1
title: 安装
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
{% assign post-heading-count = -1 %}

学习资料:
  * 官方关于 Tensorflow 安装的 [说明](https://www.tensorflow.org/versions/master/get_started/os_setup.html)

安装 Tensorflow 时需要注意的几点:

1. MacOS, Linux, Windows 系统均已支持 Tensorflow
2. 确定你的 python 版本
3. 你的 GPU 是 NVIDIA, 就可以安装 GPU 版本的 Tensorflow; 你的 GPU 不是 NVIDIA 也没有关系, 安装 CPU 版本的就好了.

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>

Tensorflow 的安装方式很多. 比如官网提供的:

* [Pip 安装](https://www.tensorflow.org/versions/master/get_started/os_setup.html#pip-installation)
* [Virtualenv 安装](https://www.tensorflow.org/versions/master/get_started/os_setup.html#virtualenv-installation)
* [Anaconda 安装](https://www.tensorflow.org/versions/master/get_started/os_setup.html#anaconda-installation)
* [Docker 安装](https://www.tensorflow.org/versions/master/get_started/os_setup.html#docker-installation)
* [从安装源 安装](https://www.tensorflow.org/versions/master/get_started/os_setup.html#installing-from-sources)

这节内容使用 pip 在每个系统的安装方式:


{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>

本文将提到第一种最简单的安装方式, pip 安装.
使用 pip 安装的时候要确保你的 pip 已经存在于你的电脑中. 如果还没有安装 pip. 
你可以在 Terminal 窗口中运行这个:

```shell
# Ubuntu/Linux 64-位 系统的执行代码:
$ sudo apt-get install python-pip python-dev

# Mac OS X 系统的执行代码:
$ sudo easy_install pip
$ sudo easy_install --upgrade six
```

<h5 id="LM-CPU">CPU 版</h5>

激动人心的时刻到了, Tensorflow (0.12) 刚刚做了更新, 绕过了复杂的安装步骤, 如果你只需要安装
CPU 版本的 Tensorflow, 运行下面这个就好了:

```shell
# python 2+ 的用户:
$ pip install tensorflow

# python 3+ 的用户:
$ pip3 install tensorflow
```

注意: 你需要8.1或更高版的 `pip` 才能顺利安装.

<h5 id="LM-GPU">GPU 版</h5>

但是 如果你想安装 GPU 版的 Tensorflow, 你要在下面找一个适合你版本的安装文件, 并在 terminal 中执行: 

```shell
# Ubuntu/Linux 64-bit, CPU only, Python 2.7
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.0rc0-cp27-none-linux_x86_64.whl

# Ubuntu/Linux 64-bit, GPU enabled, Python 2.7
# Requires CUDA toolkit 8.0 and CuDNN v5. For other versions, see "Installing from sources" below.
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.0rc0-cp27-none-linux_x86_64.whl

# Mac OS X, CPU only, Python 2.7:
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.12.0rc0-py2-none-any.whl

# Mac OS X, GPU enabled, Python 2.7:
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/gpu/tensorflow_gpu-0.12.0rc0-py2-none-any.whl

# Ubuntu/Linux 64-bit, CPU only, Python 3.4
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.0rc0-cp34-cp34m-linux_x86_64.whl

# Ubuntu/Linux 64-bit, GPU enabled, Python 3.4
# Requires CUDA toolkit 8.0 and CuDNN v5. For other versions, see "Installing from sources" below.
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.0rc0-cp34-cp34m-linux_x86_64.whl

# Ubuntu/Linux 64-bit, CPU only, Python 3.5
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.0rc0-cp35-cp35m-linux_x86_64.whl

# Ubuntu/Linux 64-bit, GPU enabled, Python 3.5
# Requires CUDA toolkit 8.0 and CuDNN v5. For other versions, see "Installing from sources" below.
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.0rc0-cp35-cp35m-linux_x86_64.whl

# Mac OS X, CPU only, Python 3.4 or 3.5:
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.12.0rc0-py3-none-any.whl

# Mac OS X, GPU enabled, Python 3.4 or 3.5:
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/gpu/tensorflow_gpu-0.12.0rc0-py3-none-any.whl
```

最后, 根据自己的 python 版本, 在 terminal 中执行以下语句:

```shell
# 如果你是 Python 2, 请复制下面
$ sudo pip install --upgrade $TF_BINARY_URL

# 如果你是 Python 3, 请复制下面
$ sudo pip3 install --upgrade $TF_BINARY_URL
```

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>

tf 0.12 版的英文[安装说明](https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html#pip-installation-on-windows)

安装前的检查:

* 目前只支持 **Python 3.5 (64bit)** 版本
* 你有安装 numpy (没有的话,请看这里[numpy 安装教程]({% link _contents/tutorials/data-manipulation/np-pd/1-2-install.md %}))

接下来惊心动魄啦! 在 command 窗口中执行

```shell
# CPU 版的
C:\> pip install tensorflow

# GPU 版的
C:\> pip install tensorflow-gpu
```

**注意** Windows 运行 Tensorflow 如果遇到这个报错:

```
Error importing tensorflow.  Unless you are using bazel,
you should not try to import tensorflow from its source directory;
please exit the tensorflow source tree, and relaunch your python interpreter
from there.
```

不要惊慌, 尝试下载安装 [Windows 的 Microsoft Visual C++ 2015 redistributable update 3 64 bit](https://www.visualstudio.com/downloads/).
就能解决这个问题.

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>

然后打开你的 python 编辑器, 输入

```python
import tensorflow
```

运行脚本来检查一下是否有正确安装.


{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>

最后, 如果你需要升级 Tensorflow 的版本, 推荐的方式是:

根据你的 python 版本, 在 terminal 中删除原有的版本

```shell
# 如果你是 Python 2, 请复制下面
pip uninstall tensorflow

# 如果你是 Python 3, 请复制下面
pip3 uninstall tensorflow
```

然后重复这个安装教程的步骤, 从头安装新版本.
