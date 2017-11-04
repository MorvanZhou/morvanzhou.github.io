---
youku_id: XMjc0ODAxNDYwMA
youtube_id: yqo9-lWTdOk
bilibili_id: 15998151
title: 快速搭建法
publish-date: 2017-05-06
thumbnail: "/static/thumbnail/torch/3-3_nn_fast.jpg"
chapter: 3
description: "Torch 中提供了很多方便的途径, 同样是神经网络, 能快则快, 我们看看如何用更简单的方式搭建同样的回归神经网络.
我们先看看之前写神经网络时用到的步骤. 我们用 net1 代表这种方式搭建的神经网络.
"
post-headings:
  - 要点
  - 快速搭建
---


学习资料:
  * [本节的全部代码](https://github.com/MorvanZhou/PyTorch-Tutorial/blob/master/tutorial-contents/303_build_nn_quickly.py){:target="_blank"}
  * [我制作的 什么是神经网络 动画简介]({% link _tutorials/machine-learning/ML-intro/2-1-NN.md %})
  * [PyTorch 官网](http://pytorch.org/){:target="_blank"}

{% include assign-heading.html %}

Torch 中提供了很多方便的途径, 同样是神经网络, 能快则快, 我们看看如何用更简单的方式搭建同样的回归神经网络.




{% include google-in-article-ads.html %}

{% include assign-heading.html %}

我们先看看之前写神经网络时用到的步骤. 我们用 `net1` 代表这种方式搭建的神经网络.

```python
class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)
        self.predict = torch.nn.Linear(n_hidden, n_output)

    def forward(self, x):
        x = F.relu(self.hidden(x))
        x = self.predict(x)
        return x

net1 = Net(1, 10, 1)   # 这是我们用这种方式搭建的 net1
```

我们用 class 继承了一个 torch 中的神经网络结构, 然后对其进行了修改, 不过还有更快的一招, 用一句话就概括了上面所有的内容!

```python
net2 = torch.nn.Sequential(
    torch.nn.Linear(1, 10),
    torch.nn.ReLU(),
    torch.nn.Linear(10, 1)
)
```

我们再对比一下两者的结构:

```python
print(net1)
"""
Net (
  (hidden): Linear (1 -> 10)
  (predict): Linear (10 -> 1)
)
"""
print(net2)
"""
Sequential (
  (0): Linear (1 -> 10)
  (1): ReLU ()
  (2): Linear (10 -> 1)
)
"""
```

我们会发现 `net2` 多显示了一些内容, 这是为什么呢? 原来他把激励函数也一同纳入进去了, 但是 `net1` 中, 激励函数实际上是在 `forward()` 功能中才被调用的.
这也就说明了, 相比 `net2`, `net1` 的好处就是, 你可以根据你的个人需要更加个性化你自己的前向传播过程, 比如(RNN).
不过如果你不需要七七八八的过程, 相信 `net2` 这种形式更适合你.

所以这也就是在我 [github 代码](https://github.com/MorvanZhou/PyTorch-Tutorial/blob/master/tutorial-contents/303_build_nn_quickly.py){:target="_blank"} 中的每一步的意义啦.


