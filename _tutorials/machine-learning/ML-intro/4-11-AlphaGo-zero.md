---
youku_id: XMzEwNDMxODAwMA
youtube_id: tABt4fdmaFg
bilibili_id: 15986543
title: AlphaGo Zero 为什么更厉害?
description: "2016 年, AlphaGo 第一版发表在了 Nature 自然杂志上, 这可是牛逼得不要不要的期刊, 如果有谁能发表一篇期刊去Nature, 哈哈, 保证他下半生衣食无忧. 而如今刚过去一年, Google DeepMind 又在 Nature 上发表了一篇 AlphaGo 的改进版, AlphaGo zero, 同样的围棋 AI, 竟然在自然杂志上发了两次! 赞叹他们的实力呀! 要弄懂 AlphaGo zero, 首先我们得弄懂 AlphaGo 是怎样战胜人类的.
AlphaGo 战胜过欧洲冠军樊麾, 韩国九段棋手李世石, 近期的比赛中又赢了世界冠军柯洁, 种种迹象表明, 人类已经失守最拿手的围棋了. 这些围棋高手一个个都表示 AlphaGo 走到了他们想不到的地方, 战胜了人类的生物极限, 不会感觉疲惫等等. 的确, 这就是机器相比人类的一个绝大优势. 那 AlphaGo 又是怎么在策略上战胜人类的呢? 很简单, 它会做计划."
publish-date: 2017-10-23
chapter: 4
thumbnail: /static/thumbnail/ML-intro/alphago.png
post-headings:
  - AlphaGo 引发轰动
  - 蒙特卡洛树搜索
  - 神经网络
  - AlphaGo Zero
---

学习资料:
  * [强化学习教程]({% link _table-contents/machine-learning/reinforcement-learning.html %})
  * [强化学习实战]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})
  * 论文 [Mastering the game of Go without human knowledge](https://www.nature.com/nature/journal/v550/n7676/full/nature24270.html){:target="_blank"}


{% include tut-image.html image-name="alphago2.png" %}

在2017年10月19日, Google Deepmind 推出了新一代的围棋人工智能 AlphaGo Zero. Alpha狗 zero 被放出的当天,
我的朋友圈, 微博等等社交平台都被刷屏了. 各大社交版面都充斥这 AlphaGo Zero 的新闻. 为什么 AlphaGo Zero 影响力这么大呢, 能在 AI 界炸开了锅? 它和之前几代的 AlphaGo 又有什么不同呢?


**注: 本文不会涉及数学推导. 大家可以在很多其他地方找到优秀的数学推导文章.**

{% include assign-heading.html %}

{% include tut-image.html image-name="alphago3.png" %}

2016 年, AlphaGo 第一版发表在了 Nature 自然杂志上, 这可是牛逼得不要不要的期刊, 如果有谁能发表一篇期刊去Nature, 哈哈, 保证他下半生衣食无忧. 而如今刚过去一年, Google DeepMind 又在 Nature 上发表了一篇 AlphaGo 的改进版, AlphaGo zero, 同样的围棋 AI, 竟然在自然杂志上发了两次! 赞叹他们的实力呀! 要弄懂 AlphaGo zero, 首先我们得弄懂 AlphaGo 是怎样战胜人类的.
AlphaGo 战胜过欧洲冠军樊麾, 韩国九段棋手李世石, 近期的比赛中又赢了世界冠军柯洁, 种种迹象表明, 人类已经失守最拿手的围棋了. 这些围棋高手一个个都表示 AlphaGo 走到了他们想不到的地方, 战胜了人类的生物极限, 不会感觉疲惫等等. 的确, 这就是机器相比人类的一个绝大优势. 那 AlphaGo 又是怎么在策略上战胜人类的呢? 很简单, 它会做计划.



{% include google-in-article-ads.html %}

{% include assign-heading.html %}

{% include tut-image.html image-name="alphago4.png" %}

它能使用这种树形结构来尝试非常多的策略, 每一个树的分支就是一种可能的发展趋势, 可是围棋的下棋趋势被公认比天上的星星还要多, 人类目前的计算机是无法在每一步都尝试这种数不尽的趋势.

{% include tut-image.html image-name="alphago5.png" %}

所以它采用的是一种叫做蒙特卡洛树搜索(Monte Carlo Tree Search)的形式对未知方面进行探索,

{% include tut-image.html image-name="alphago6.png" %}

而这种形式正是在国际象棋AI上所采取的方式, 当时IBM开发的国际象棋人工智能 Deep Blue, 通过这种树形搜索在1997年战胜人类的. 可是同样树形结构在接下来的20年中却没有多大发展, 不然围棋早就被攻克了. 问题在哪里?

{% include tut-image.html image-name="alphago7.png" %}

这是当时用于国际象棋的搜索树结构, 因为国际象棋中可能发生的情况要比围棋少太多, 通过计算机广泛的搜索, 是完全可行的. 但是在围棋中, 同样的套路并不适用, 所以 DeepMind 团队放弃广泛的搜索, 取而代之的是深度搜索, 这种搜索更节省计算资源, 对有限的情况, 分析更加准确. 不过单单有这种树形搜索是远远不够的.






{% include google-in-article-ads.html %}

{% include assign-heading.html %}


{% include tut-image.html image-name="alphago8.png" %}

所以我们还将会加上正在飞速发展的神经网络结构, 用来对当前状态进行评估, 和做决策.

{% include tut-image.html image-name="alphago9.png" %}

一个简单的神经网络包括了三个方面, 接受外界的信息, 比如说一张棋谱, 然后通过神经网络内部的千万个神经节点, 将接收到的信息进行加工处理, 换做我们人类, 这个过程就叫做”理解”. 最后将理解的东西输出, 它可以是下一个要采取的动作, 或者是对当前下棋状态的评估. AlphaGo 中就使用了两套神经网络系统
一个神经网络基于当前的状态给出下一步的动作, 一个神经网络用来评估当前状态是否对我方有利.
使用神经网络配合搜索树来提供好的下棋行为, 将这些好行为作为训练数据反过来训练神经网络, 这样一来一回, 使用[强化学习]({% link _tutorials/machine-learning/ML-intro/4-01-RL.md %})的方法不断训练, 我们的神经网络就能不断的提升自己下棋的能力. 这就是 AlphaGo 能够战胜人类的主要原因.






{% include google-in-article-ads.html %}

{% include assign-heading.html %}

{% include tut-image.html image-name="alphago10.png" %}

可是 AlphaGo 新版本 AlphaGo Zero 为什么被提出, 而且提出后为什么又能引起轩然大波? 很显然, 它肯定比前几个 AlphaGo 好, 首先也是最重要的是, 它完全没有学习过任何人类棋谱.

{% include tut-image.html image-name="alphago11.png" %}

人类学习下棋, 学习前辈们留下来的优秀棋谱是必不可少的, 所以上几个版本的 AlphaGo 也继承了这个思想, 我要从人类那里学习下棋的原则, 有一个好老师, 将会比无师自通方便多了.

{% include tut-image.html image-name="alphago12.png" %}

如果你和这样一个有人类老师的 AlphaGo 交手, 那可能还会在它背后看到人类下棋的影子. 但是 AlphaGo Zero, 完全是一个无师自通的家伙, 和它下棋, 你可能闻到很浓烈的机械味. 从另一方面想, 这样的 AlphaGo 打破了数千年来人类下棋思维的限制, 探索了人类想不到的下棋境界, 学会了一个崭新的下棋方式.

{% include tut-image.html image-name="alphago13.png" %}

在技术层面来说, AlphaGo Zero 使用的不再是两套神经网络系统, 而是将它们融合成一个神经网络系统, 这样做能更有效利用资源, 学习效果更好.

{% include tut-image.html image-name="alphago14.png" %}

而且它不再仅仅使用 GPU, 转而添加了自家的专门为机器学习打造的 TPU, 而且使用的硬件个数也在逐步降低, 然而学习的效果却不断上升.
在短短40天没有老师教的训练中, AlphaGo Zero 超越了他所有的前辈, 在这个时候, 我相信它真正做到了在围棋场上无人能敌了. 最后, 正如 AlphaGo 之父 David Silver 所说, 一个无师自通 AlphaGo 的产生, 并不仅仅意味着我们的 AI 能在围棋场上战胜人类, 放眼未来, 它还意味着, 在更多方面, 我们能用这样的 AI 创造出更多人类历史上的新篇章.
