---
youku_id: XMTY1OTUyNjIzNg
youtube_id: uefJFOaypj8
title: 安装
description: 安装介绍
author: 缘
chapter: 1
post-headings:
  - 安装要求
  - 通用安装法
---
{% assign post-heading-count = -1 %}

学习资料:
  * [英文安装说明](https://github.com/MorvanZhou/tutorials/blob/master/theanoTUT/theano2_install.py)
  * Windows 上的安装 [方法](http://deeplearning.net/software/theano/install_windows.html#install-windows)

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>


1. python 2 >=2.6 or python 3>=3.3
2. Numpy >= 1.7.1  [安装说明]({% link _contents/tutorials/data-manipulation/np-pd/1-2-install.md %})
3. Scipy >= 0.11


{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>


直接复制粘贴下面的命令, 然后在 terminal 当中运行. 如果要使用 GPU 加速运算, 要确保在你的电脑上有 NVIDIA 的 GPU 显卡, 而且能够使用 CUDA 模块.

```shell
# python 2+ 版本
pip install theano

# python 3+ 版本
pip3 install theano
```

如果遇到权限问题, 请在 `pip` 前加一个 `sudo` 如: `sudo pip install theano`.

更详细的Theano安装步骤:

* [Linux ubuntu](http://deeplearning.net/software/theano/install_ubuntu.html#install-ubuntu)
* [Windows](http://deeplearning.net/software/theano/install_windows.html#install-windows)





