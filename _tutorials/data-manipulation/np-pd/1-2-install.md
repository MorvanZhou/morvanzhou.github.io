---
youku_id: XMTU4NjM5NzgyNA
youtube_id: JauGYB-Bzuw
bilibili_id: 16378954
title: Numpy 和 Pandas 安装
description: 简单易懂的Numpy 和 Pandas 的安装教学 (Windows, MacOS, Linux)
author: abner
date: 2016-11-3
chapter: 1
post-headings:
  - numpy 安装
  - pandas安装
---


学习资料:
  * Windows 安装的英文说明 [链接](http://stackoverflow.com/questions/2817869/error-unable-to-find-vcvarsall-bat){:target="_blank"}
  * Visual studio [下载地址](https://www.visualstudio.com/en-us/downloads/download-visual-studio-vs.aspx){:target="_blank"}


{% include assign-heading.html %}

Numpy 的安装文件地址是[这里](https://sourceforge.net/projects/numpy/files/NumPy/){:target="_blank"}。里面有不同版本，有开发者版本和稳定版本。同时根据不同的系统选择不同的版本进行下载。

也可以通过命令安装：

**MacOS**

```shell
# 使用 python 3+:
pip3 install numpy

# 使用 python 2+:
pip install numpy
```

如果遇到管理员权限问题, 请在 `pip` 前加上 `sudo`. 比如 `sudo pip install numpy`

**Windows**

可能会遇到各种问题，可以查看一下这个[安装说明](http://stackoverflow.com/questions/2817869/error-unable-to-find-vcvarsall-bat){:target="_blank"}。

**Linux Ubuntu & Debian**

在终端 terminal 执行:

```shell
sudo apt-get install python-numpy
```


{% include google-in-article-ads.html %}

{% include assign-heading.html %}

安装 pandas 有各种的安装方式。

**Mac**

```shell
# 使用 python 3+:
pip3 install pandas

# 使用 python 2+:
pip install pandas
```

同样, 如果遇到管理员权限问题, 请在 `pip` 前加上 `sudo`. 比如 `sudo pip install pandas`

**Windows**

如果你能顺利安装 numpy, 那 pandas 也可以用和 Mac 一样的方式安装.

**Linux Ubuntu & Debian**

在终端 terminal 执行:

```shell
sudo apt-get install python-pandas
```