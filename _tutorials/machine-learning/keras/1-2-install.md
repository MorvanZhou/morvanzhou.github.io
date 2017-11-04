---
youku_id: XMTc3ODk5NjUyNA
youtube_id: glcqKUzr1ZM
bilibili_id: 16014300
title: Keras 安装
publish-date: 2016-10-29
chapter: 1
description: keras 的最简单安装方法. 安装要保证已经安装过 Numpy 和 Scipy 了, 不然会安装不成功
post-headings:
  - 确认信息
  - pip安装
---


学习资料:
  * [Numpy 安装教程]({% link _tutorials/data-manipulation/np-pd/1-2-install.md %})

{% include assign-heading.html %}

1. 在安装 Keras 之前, 需要确认自己已经安装好了 Numpy 和 Scipy. 可参考我的 [Numpy 安装教程]({% link _tutorials/data-manipulation/np-pd/1-2-install.md %})
2. 因为 Keras 是基于 Tensorflow 或者 Theano 的. 所以可以先自己安装 Tensorflow 或者 Theano. 可参考我的[Tensorflow 安装教程]({% link _tutorials/machine-learning/tensorflow/1-2-install.md %}) 或者 [Theano 安装教程]({% link _tutorials/machine-learning/theano/1-2-install.md %})
3. 安装 Keras. 在你的 Terminal 窗口中输入.

```shell
# 如果你是 python 2+ 版本, 复制下面
pip install keras

# 如果你是 python 3+ 版本, 复制下面
pip3 install keras
```

{% include assign-heading.html %}

如果你在安装过程中遇到了管理员关于 permission 的报错时, 请尝试以下方法, 并输入你的密码进行安装:

```shell
# 如果你是 python 2+ 版本, 复制下面
sudo pip install keras

# 如果你是 python 3+ 版本, 复制下面
sudo pip3 install keras
```
