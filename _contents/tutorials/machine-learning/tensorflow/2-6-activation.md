---
youku_id: XMTU5NjA2MTk0MA
youtube_id: 6gbGCxBGxZA
description: Tensorflow 的神经网络 里面处理较为复杂的问题时都会需要运用激励函数 activation function, 影片里说到了什么是激励函数,和在 Tensorflow 中有哪些是可以直接调用的激励函数.同时也介绍了在神经网络中激励函数处在哪个位置.
author : 商晋
chapter: 2
title: 激励函数 Activation Function
date: 2016-11-3
post-headings:
  - 快速了解
---
{% assign post-heading-count = -1 %}

学习资料:
  * Tensorflow 提供的一些 [激励函数](https://www.tensorflow.org/versions/0.6.0/api_docs/python/nn.html)
  * 机器学习-简介系列 [激励函数]({% link _contents/tutorials/machine-learning/ML-intro/3-04-activation-function.md %})
  * 为 TF 2017 打造的[新版可视化教学代码](https://github.com/MorvanZhou/Tensorflow-Tutorial)

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>

欢迎回来！这节课我们学习 Tensorflow 中的 `activation function` .

激励函数运行时激活神经网络中某一部分神经元，将激活信息向后传入下一层的神经系统。激励函数的实质是非线性方程。
Tensorflow 的神经网络 里面处理较为复杂的问题时都会需要运用激励函数 `activation function` 。
详细介绍请前往 "机器学习-简介系列" [激励函数]({% link _contents/tutorials/machine-learning/ML-intro/3-04-activation-function.md %})

