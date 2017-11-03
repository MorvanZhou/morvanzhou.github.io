---
youku_id: XMjk2MzAwMjYyMA
youtube_id: 7R3bnpv5q9k
bilibili_id: 15982794
title: 进化算法 简介
description: "进化 Evolution, 可以说是人类历史上伟大的发现之一. 适者生存, 不适者淘汰, 达尔文的进化理论让我们见识到了自己是怎么来的.
那, 现在想象一下, 如果你的程序也能进化, 也用适者生存, 不适者淘汰的原则生长出一个牛逼的物种,
是不是很开心, 是不是很激动! 反正这就是我为什么会对这类算法特别感兴趣的原因之一了."
publish-date: 2017-08-12
thumbnail: "/static/thumbnail/evolutionary-algorithm/11ea.jpg"
chapter: 1
post-headings:
  - 要点
  - 大神们都拿它做了些什么
  - 算法们
  - 这个教程的内容
---



学习资料:

* [我制作的 什么是遗传算法 动画简介]({% link _tutorials/machine-learning/ML-intro/5-01-genetic-algorithm.md %})
* [我制作的 什么是进化策略 动画简介]({% link _tutorials/machine-learning/ML-intro/5-02-evolution-strategy.md %})
* [我制作的 什么是神经进化 动画简介]({% link _tutorials/machine-learning/ML-intro/5-03-neuro-evolution.md %})

{% include assign-heading.html %}



"进化" Evolution, 可以说是人类历史上伟大的发现之一. 适者生存, 不适者淘汰, 达尔文的进化理论让我们见识到了自己是怎么来的.
那, 现在想象一下, 如果你的程序也能进化, 也用适者生存, 不适者淘汰的原则生长出一个牛逼的物种,
是不是很开心, 是不是很激动! 反正这就是我为什么会对这类算法特别感兴趣的原因之一了.


{% include assign-heading.html %}

在 Youtube 上, 一搜就能搜到很多关于 Evolution Algorithm (之后简称为 EA) 的实验短片.
我截取了几个给大家看看, 后面也附上他们的链接. 如果你能翻墙, 也能看看他们有趣的实验.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/evolutionary-algorithm/4-1-0.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

这些是上面实验的部分链接 ( [马里奥](https://www.youtube.com/watch?v=qv6UVOQ0F44){:target="_blank"}, [马里奥](https://www.youtube.com/watch?v=qv6UVOQ0F44){:target="_blank"},
 [微生物进化](https://www.youtube.com/watch?v=2kupe2ZKK58){:target="_blank"})

如果你提起兴趣了, 恭喜你, 你离学会这些又进了一步. 接着看看我为大家尽心准备的教程,
相信大家就能迅速上手. 如果大家觉得真的学习到了东西, 我做的东西对你的学习生活有所帮助.
希望大家也能[支持我](https://morvanzhou.github.io/support/){:target="_blank"}做出更好, 更简单易懂的教程.
如果没有大家之前的支持, 这一系列进化算法的教程也出不来~ 感谢~

{% include assign-heading.html %}


EA 包括了很多种类的算法, 但是这些算法的精髓都是围绕着达尔文的进化理论, 虽然有一些发展到后面, 有点偏离的这个轨道, 不过他们都是受这个的启蒙.
在 [wiki](https://en.wikipedia.org/wiki/Evolutionary_algorithm){:target="_blank"}上, EA 包括了:

* 遗传算法 (Genetic Algorithm)
* 进化策略 (Evolution strategy)
* 神经进化 (Neuroevolution)
* Genetic programming
* ...

在这一系列的教程中我们会着重讲解比较著名的 遗传算法 (Genetic Algorithm), 进化策略 (Evolution strategy) 和
神经进化 (Neuroevolution). 看看在多种多样的问题中, 他们是如何自由穿梭.
尤其是之后, 我们还会涉及到强化学习的内容. 如果大家有了解我做过的 [强化学习教程](https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/){:target="_blank"},
在后续教程中我们就来看看能挑战当今流行的强化学习的 "进化方法".

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

在这个教程中, 我们会用实践的方式, 手把手教你如何在电脑里进化. 让你也能动手实践, 更好的理解消化知识点.

比如用 OpenAI gym 来[训练你的小机器人]({% link _tutorials/machine-learning/evolutionary-algorithm/4-04-evolution-strategy-reinforcement-learning.md %}).

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/evolutionary-algorithm/4-4-0.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

用简单的代码, 可视化各种进化算法的本质. 比如[这个]({% link _tutorials/machine-learning/evolutionary-algorithm/2-01-genetic-algorithm.md %}).

{% include tut-image.html image-name="2-1-0.gif" %}

旅行商人的[最短路劲]({% link _tutorials/machine-learning/evolutionary-algorithm/2-03-genetic-algorithm-travel-sales-problem.md %})问题:

{% include tut-image.html image-name="2-3-0.gif" %}

[配对句子]({% link _tutorials/machine-learning/evolutionary-algorithm/2-02-genetic-algorithm-match-phrase.md %})问题:

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/evolutionary-algorithm/2-2-0.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

结合了梯度下降的原则的[进化算法]({% link _tutorials/machine-learning/evolutionary-algorithm/3-03-evolution-strategy-natural-evolution-strategy.md %}):

{% include tut-image.html image-name="3-3-0.gif" %}

等等等等. 我们就来慢慢理解消化啦~