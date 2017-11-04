---
youku_id: XMTcxMTExNjA5Mg
youtube_id: tI9AbaBfnPc
bilibili_id: 15997789
title: 激励函数 (Activation Function)
description: 今天我们会来聊聊现代神经网络中 必不可少的一个组成部分, 激励函数, activation function. 激励函数也就是为了解决我们日常生活中不能用线性方程所概括的问题.
chapter: 3
post-headings:
  - 非线性方程
  - 激励函数
  - 常用选择
---

学习资料:
  * Theano 激励函数 [教程]({% link _tutorials/machine-learning/theano/2-4-activation.md %})
  * Tensorflow 激励函数 [教程]({% link _tutorials/machine-learning/tensorflow/2-6-activation.md %})
  * PyTorch 激励函数 [教程]({% link _tutorials/machine-learning/torch/2-03-activation.md %})


今天我们会来聊聊现代神经网络中 必不可少的一个组成部分, 激励函数, activation function.

**注: 本文不会涉及数学推导. 大家可以在很多其他地方找到优秀的数学推导文章.**

 {% include assign-heading.html %}

我们为什么要使用激励函数? 用简单的语句来概括. 就是因为, 现实并没有我们想象的那么美好, 它是残酷多变的. 哈哈, 开个玩笑, 不过激励函数也就是为了解决我们日常生活中 不能用线性方程所概括的问题. 好了,我知道你的问题来了. 什么是线性方程 (linear function)?

{% include tut-image.html image-name="active1.png" %}

说到线性方程, 我们不得不提到另外一种方程, 非线性方程 (nonlinear function). 我们假设, 女生长得越漂亮, 越多男生爱. 这就可以被当做一个线性问题. 但是如果我们假设这个场景是发生在校园里. 校园里的男生数是有限的, 女生再漂亮, 也不可能会有无穷多的男生喜欢她. 所以这就变成了一个非线性问题.再说..女生也不可能是无穷漂亮的. 这个问题我们以后有时间私下讨论.

{% include tut-image.html image-name="active2.png" %}

然后我们就可以来讨论如何在神经网络中达成我们描述非线性的任务了. 我们可以把整个网络简化成这样一个式子. Y = Wx, W 就是我们要求的参数, y 是预测值, x 是输入值. 用这个式子, 我们很容易就能描述刚刚的那个线性问题, 因为 W 求出来可以是一个固定的数. 不过这似乎并不能让这条直线变得扭起来 , 激励函数见状, 拔刀相助, 站出来说道: “让我来掰弯它!”.





 {% include assign-heading.html %}


{% include tut-image.html image-name="active3.png" %}

这里的 AF 就是指的激励函数. 激励函数拿出自己最擅长的”掰弯利器”, 套在了原函数上 用力一扭, 原来的 Wx 结果就被扭弯了.

其实这个 AF, 掰弯利器, 也不是什么触不可及的东西. 它其实就是另外一个非线性函数. 比如说relu, sigmoid, tanh. 将这些掰弯利器嵌套在原有的结果之上, 强行把原有的线性结果给扭曲了. 使得输出结果 y 也有了非线性的特征. 举个例子, 比如我使用了 relu 这个掰弯利器, 如果此时 Wx 的结果是1, y 还将是1, 不过 Wx 为-1的时候, y 不再是-1, 而会是0.

你甚至可以创造自己的激励函数来处理自己的问题, 不过要确保的是这些激励函数必须是可以微分的, 因为在 backpropagation 误差反向传递的时候, 只有这些可微分的激励函数才能把误差传递回去.

{% include google-in-article-ads.html %}


 {% include assign-heading.html %}

{% include tut-image.html image-name="active4.png" %}

想要恰当使用这些激励函数, 还是有窍门的. 比如当你的神经网络层只有两三层, 不是很多的时候, 对于隐藏层, 使用任意的激励函数, 随便掰弯是可以的, 不会有特别大的影响. 不过, 当你使用特别多层的神经网络, 在掰弯的时候, 玩玩不得随意选择利器. 因为这会涉及到梯度爆炸, 梯度消失的问题. 因为时间的关系, 我们可能会在以后来具体谈谈这个问题.

最后我们说说, 在具体的例子中, 我们默认首选的激励函数是哪些. 在少量层结构中, 我们可以尝试很多种不同的激励函数. 在卷积神经网络 Convolutional neural networks 的卷积层中, 推荐的激励函数是 relu. 在循环神经网络中 recurrent neural networks, 推荐的是 tanh 或者是 relu (这个具体怎么选, 我会在以后 循环神经网络的介绍中在详细讲解).

