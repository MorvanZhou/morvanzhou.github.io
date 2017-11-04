---
youku_id: XMjc0NTg5Nzk3Ng
youtube_id: wnKgOd3NdzA
bilibili_id: 15997678
title: Why Pytorch?
description: "PyTorch 是 Torch 在 Python 上的衍生. 因为 Torch 是一个使用 Lua
语言的神经网络库, Torch 很好用, 但是 Lua 又不是特别流行, 所有开发团队将 Lua 的 Torch 移植到了更流行的语言 Python 上.
是的 PyTorch 一出生就引来了剧烈的反响. 为什么呢?
很简单, 我们就看看有谁在用 PyTorch 吧."
publish-date: 2017-05-05
thumbnail: "/static/thumbnail/torch/1_why.jpg"
chapter: 1
post-headings:
  - 为什么用 PyTorch
  - 神经网络在做什么
  - PyTorch 和 Tensorflow
---

学习资料:
  * [什么是神经网络 短视频]({% link _tutorials/machine-learning/ML-intro/2-1-NN.md %})
  * [PyTorch 官网](http://pytorch.org/){:target="_blank"}



{% include assign-heading.html %}

[PyTorch](http://pytorch.org/){:target="_blank"} 是 [PyTorch](http://pytorch.org/){:target="_blank"} 在 Python 上的衍生. 因为 [PyTorch](http://pytorch.org/){:target="_blank"} 是一个使用 [PyTorch](http://pytorch.org/){:target="_blank"}
语言的神经网络库, Torch 很好用, 但是 Lua 又不是特别流行, 所有开发团队将 Lua 的 Torch 移植到了更流行的语言 Python 上.
是的 PyTorch 一出生就引来了剧烈的反响. 为什么呢?

很简单, 我们就看看有谁在用 PyTorch 吧.

{% include tut-image.html image-name="1-1-1.png" %}

可见, 著名的 Facebook, twitter 等都在使用它, 这就说明 PyTorch 的确是好用的, 而且是值得推广.

而且如果你知道 [Numpy](http://www.numpy.org/){:target="_blank"}, PyTorch 说他就是在神经网络领域可以用来替换 numpy 的模块.


{% include assign-heading.html %}

神经网络在学习拟合线条(回归):

{% include tut-image.html image-name="1-1-2.gif" %}

神经网络在学习区分数据(分类):

{% include tut-image.html image-name="1-1-3.gif" %}


{% include assign-heading.html %}

据 PyTorch 自己介绍, 他们家的最大优点就是建立的神经网络是动态的, 对比静态的 Tensorflow, 他能更有效地处理一些问题, 比如说 RNN 变化时间长度的输出.
而我认为, 各家有各家的优势和劣势, 所以我们要以中立的态度. 两者都是大公司,
Tensorflow 自己说自己在分布式训练上下了很大的功夫, 那我就默认 Tensorflow 在这一点上要超出 PyTorch,
但是 Tensorflow 的静态计算图使得他在 RNN 上有一点点被动 (虽然它用其他途径解决了), 不过用 PyTorch 的时候, 你会对这种动态的 RNN 有更好的理解.

而且 Tensorflow 的高度工业化, 它的底层代码... 你是看不懂的.
PyTorch 好那么一点点, 如果你深入 API, 你至少能比看 Tensorflow 多看懂一点点 PyTorch 的底层在干嘛.

最后我的建议就是:

* 如果你是学生, 随便选一个学, 或者稍稍偏向 PyTorch, 因为写代码的时候应该更好理解. 懂了一个模块, 转换 Tensorflow 或者其他的模块都好说.
* 如果是上班了, 跟着你公司来, 公司用什么, 你就用什么, 不要脱群.


