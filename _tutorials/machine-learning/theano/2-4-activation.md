---
youku_id: XMTY2MzkxNDE1Ng
youtube_id: Xm2InCJqFY4
title: Activation function 激励函数
description: Activation function 激励函数是神经网络学习当中必不可少的内容,对于不同种的问题,我们运用到的激励函数也会不同. 大家可以尝试不同种的激励函数看看效果哪种会好.
author: Alice
chapter: 2
date: 2016-11-3
post-headings:
  - 什么是 Activation function
  - 几种常用激活函数
  - 应用场景
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/theanoTUT/theano7_activation_function.py){:target="_blank"}
  * Theano 激励函数选择 [链接](http://deeplearning.net/software/theano/library/tensor/nnet/nnet.html#theano.tensor.nnet.nnet.sigmoid){:target="_blank"}
  * 机器学习-简介系列 [激励函数]({% link _tutorials/machine-learning/ML-intro/3-04-activation-function.md %})


今天讲一下在神经网络中激励函数的作用和如何运作，以及 Theano 中有哪些激励函数。



{% include assign-heading.html %}

首先，什么是 `Activation function`？

在这个视频中有提到 [什么是神经网络]({% link _tutorials/machine-learning/ML-intro/2-1-NN.md %})
如下图，在这三个中间层中，有激活函数，相当于过滤器或者激活器，作用就是会使一些特征被激活 Activate，同时另一些特征不被激活 Deactivate，
例如，当猫的图片数据传递到第一个隐藏层时，在这个激励函数作用下，大于 0 的数据乘以 1 保持原样，小于 0 的数据乘以 0 变为 0，被 `Deactivate`。

{% include tut-image.html image-name="2_4_1.png" %}

有多种激活函数，例如，当传递进来的值越小时，作用后就会越接近 0， 当传递进来的值越大时，作用后就会越接近 1。
还有可以计算线性或者非线性关系的，或者可以计算概率的激活函数。
总而言之，激活函数的作用就是使重要的信息被激励，不重要或者反向的信息不被激励。传进来的值，经过这种变化，得到另一种结果，而这正是我们需要的。


{% include google-in-article-ads.html %}

{% include assign-heading.html %}

Theano 中可以用的激励函数可以在这个 [链接](http://deeplearning.net/software/theano/library/tensor/nnet/nnet.html){:target="_blank"} 中找到。
进入这个链接，以 `theano.tensor.nnet.nnet.sigmoid(x)` 为例。
`Sigmoid` 函数就是可以做到，当输入值小于 0 并且越小时，输出值就会越接近 0， 当输入值大于 0 并且越大时，输出值就会越接近 1。常被用于分类问题中。
还有其他几种拓展函数，例如 `softplus()`，当输入值小于 0 时，输出值接近 0， 当输入值大于 0 时，输出值是非线性的上升关系。可以很好地处理具有非线性的逻辑关系的输入值。
`relu()`， 当输入值小于 0 时，输出值全部等于 0， 当输入值大于 0 时，输出值是线性关系。
常用的有 `softplus()，softmax()，relu()` 这三种，当然还有 `tanh()` 等等。
在实际中可以尝试在不同的神经层中，放入不同的激活函数，尝试得到不同的效果。具体问题具体分析，会发现有些激活函数并不适合当前的问题。


{% include assign-heading.html %}

在隐藏层中，可以用 `relu, tanh, softplus` 等非线性的激活函数。
在分类问题中，可以用 `sigmoid ，softmax` 来求概率。例如选择 N 类中概率最大的那一类作为预测值。
在回归问题中，可以什么激活函数都不用，只用 `linear function`，或者对于 价格，高度 这种非负的变量，可以在输出层用 `relu` 这种非负的激活函数，使输出值非负。
