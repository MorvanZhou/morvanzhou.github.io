---
youku_id: XMjk5NDcxNDcyOA
youtube_id: ozSdqrN-kFQ
bilibili_id: 15985546
title: Natural Evolution Strategy
publish-date: 2017-08-28
thumbnail: "/static/thumbnail/evolutionary-algorithm/33es.jpg"
chapter: 3
description: "Natural ES 后面简称 NES, 应该就是算一种用适应度诱导的梯度下降法,
如果要我用一句话来概括 NES: 生宝宝, 用好宝宝的梯度辅助找到前进的方向"
post-headings:
  - 要点
  - NES算法
  - 进化啦
---


学习资料:
  * [本节的全部代码](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Evolution%20Strategy/Natural%20Evolution%20Strategy%20(NES){:target="_blank"}.py)
  * [我制作的 什么是进化策略 动画简介]({% link _tutorials/machine-learning/ML-intro/5-02-evolution-strategy.md %})
  * 论文 [Natural evolution strategies](http://www.jmlr.org/papers/volume15/wierstra14a/wierstra14a.pdf){:target="_blank"}

 {% include assign-heading.html %}

如果你想对进化策略有一个快速了解, [这个几分钟的短动画]({% link _tutorials/machine-learning/ML-intro/5-02-evolution-strategy.md %})是个很好的方式.

Natural ES 后面简称 NES, 应该就是算一种用适应度诱导的梯度下降法,
**如果要我用一句话来概括 NES: 生宝宝, 用好宝宝的梯度辅助找到前进的方向**

本节要实践的内容提前看:

{% include tut-image.html image-name="3-3-0.gif" %}





 {% include assign-heading.html %}

{% include tut-image.html image-name="3-3-1.png" %}

宝宝们的梯度是这个 ![gradient](/static/results/evolutionary-algorithm/3-3-2.png)
加上这些宝宝们的 fitness ![fitness](/static/results/evolutionary-algorithm/3-3-3.png), 用梯度乘以 fitness 就是说, 加大力度往带来好 fitness 的梯度下降.
所以之后的宝宝们就会越来越多的下降到最优点啦. 那么我们要梯度下降的参数则是那些正态分布的均值和均方差.

提到梯度下降, 哈哈, 那么那些 scipy, Tensorflow 都可以考虑用一用. 这个教程中将会使用到
Tensorflow 来完成这种梯度下降的做法. 如果你对 Tensorflow 感兴趣, 我也有[一套 Tensorflow 的教程](https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/){:target="_blank"}哦~

NES 的方法其实和强化学习中 [Policy Gradient]({% link _tutorials/machine-learning/reinforcement-learning/5-1-policy-gradient-softmax1.md %}) 的方法非常接近.
简单来概括一下它们的不同: 在行为的策略上, PG 是扰动 Action, 不同的 action 带来不同的 reward, 通过 reward 大小对应上 action 来计算 gradient, 再反向传递 gradient. 但是 ES 是扰动 神经网络中的 Parameters, 不同的 parameters 带来不同的 reward, 通过 reward 大小对应上 parameters 来按比例更新原始的 parameters.

 {% include assign-heading.html %}

Tensorflow 是神经网络模块, 虽然我们今天不拿它来做神经网络, 但是首先还是需要搭建一个计算图纸,
之后再往图纸里面灌数据. 不断自动梯度下降, 提升参数. 关于正态分布, 我们从 tf 中 import `MultivariateNormalFullCovariance`.
之前提出的要学习的变量包括均值和均方差, 但是到了多变量的正态分布, 我们要学习的就是协方差矩阵 Covariance matrix.
如果不太了解 Covariance matrix, 你就把他想象成要学习的均方差就行, 意思差不多.

```python
import tensorflow as tf
from tensorflow.contrib.distributions import MultivariateNormalFullCovariance

mean = tf.Variable(tf.random_normal([2, ], 13., 1.), dtype=tf.float32)
cov = tf.Variable(5. * tf.eye(DNA_SIZE), dtype=tf.float32)
mvn = MultivariateNormalFullCovariance(loc=mean, covariance_matrix=cov)
make_kid = mvn.sample(N_POP)
```

我们用 `mean`, `cov` 当作要学的变量, 放入 `MultivariateNormalFullCovariance` 中.
这时的 `mvn` 就是这个多变量正态分布啦. 采样的时候呢, 我们就能用 `mvn.sample(N_POP)`.
记住, `make_kid` 目前只是在计算图纸上的功能, 还没被运行, 之后调用的时候才被运行.

{% include google-in-article-ads.html %}

接下来搭建一些计算图纸上其他的东西, `tfkids_fit` 是将要被传入到计算图纸中的 fitness 值.
`tfkids` 是之前 `make_kid` 采样出来的宝宝 DNA 们. 神经网络中有一个东西叫做误差, 有时候叫做 `loss` 或者 `cost`,
通过误差反向传递, 我们就能更新前面的 `Variable` 变量了. 为了变成 tf 形式, 之前的算法中 (梯度*fitness),
就相当于 `mvn.log_prob(tfkids)*tfkids_fit`.

```python
tfkids_fit = tf.placeholder(tf.float32, [N_POP, ])
tfkids = tf.placeholder(tf.float32, [N_POP, DNA_SIZE])
loss = -tf.reduce_mean(mvn.log_prob(tfkids)*tfkids_fit)         # log prob * fitness
train_op = tf.train.GradientDescentOptimizer(LR).minimize(loss) # compute and apply gradients for mean and cov
```

在 Tensorflow 中, 初始化自变量还有一步(必须):

```python
sess = tf.Session()
sess.run(tf.global_variables_initializer())
```

最后我们就能调用主循环来提升参数准确性了.

```python
for g in range(N_GENERATION):
    kids = sess.run(make_kid)
    kids_fit = get_fitness(kids)
    sess.run(train_op, {tfkids_fit: kids_fit, tfkids: kids})    # update distribution parameters
```

这节内容如果看不太懂的话, 应该是还不是很了解 Tensorflow 的使用方法, 强烈推荐看看我的 [Tensorflow 教程](https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/){:target="_blank"}, 简单明了.

可视化的代码我没有在文章中体现, 如果想详细看看如何可视化, 请看到我的 [Github](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Evolution%20Strategy/Natural%20Evolution%20Strategy%20(NES){:target="_blank"}.py).

下次我们来看看[遗传算法和进化策略+神经网络的牛逼应用]({% link _tutorials/machine-learning/evolutionary-algorithm/4-01-neuro-evolution.md %}).
