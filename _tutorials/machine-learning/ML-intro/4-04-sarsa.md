---
youku_id: XMjI1NjY5MTk4OA
youtube_id: AANzrFOQIiM
bilibili_id: 15988106
title: Sarsa
description: "今天我们会来说说强化学习中一个和 Q learning 类似的算法, 叫做 Sarsa. 在强化学习中 Sarsa 和 Q learning 及其类似, 这节内容会基于之前我们所讲的 Q learning. 所以还不熟悉 Q learning 的朋友们, 请前往我制作的 Q learning 简介 (知乎专栏). 我们会对比 Q learning, 来看看 Sarsa 是特殊在哪些方面. 和上次一样, 我们还是使用写作业和看电视这个例子. 没写完作业去看电视被打, 写完了作业有糖吃.
"
publish-date: 2017-01-13
chapter: 4
thumbnail: /static/thumbnail/ML-intro/Sarsa_thumbnail.png
post-headings:
  - Sarsa 决策
  - Sarsa 更新行为准则
  - 对比 Sarsa 和 Q-learning 算法
---

学习资料:
  * [强化学习教程]({% link _table-contents/machine-learning/reinforcement-learning.html %})
  * [强化学习模拟程序](https://www.youtube.com/watch?v=G5BDgzxfLvA&list=PLXO45tsB95cLYyEsEylpPvTY-8ErPt2O_){:target="_blank"}
  * [Q-learning 简介视频]({% link _tutorials/machine-learning/ML-intro/4-03-q-learning.md %})
  * [Sarsa Python 教程]({% link _tutorials/machine-learning/reinforcement-learning/3-1-tabular-sarsa1.md %})
  * [强化学习实战]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})
  * 学习书籍 [Reinforcement learning: An introduction](http://ufal.mff.cuni.cz/~straka/courses/npfl114/2016/sutton-bookdraft2016sep.pdf){:target="_blank"}



今天我们会来说说强化学习中一个和 Q learning 类似的算法, 叫做 Sarsa.

**注: 本文不会涉及数学推导. 大家可以在很多其他地方找到优秀的数学推导文章.**

{% include tut-image.html image-name="s1.png" %}

在强化学习中 Sarsa 和 [Q learning]({% link _tutorials/machine-learning/ML-intro/4-03-q-learning.md %}) 及其类似, 这节内容会基于之前我们所讲的 Q learning. 所以还不熟悉 Q learning 的朋友们, 请前往我制作的 Q learning 简介 (知乎专栏). 我们会对比 Q learning, 来看看 Sarsa 是特殊在哪些方面. 和上次一样, 我们还是使用写作业和看电视这个例子. 没写完作业去看电视被打, 写完了作业有糖吃.

 {% include assign-heading.html %}

{% include tut-image.html image-name="s2.png" %}

Sarsa 的决策部分和 [Q learning]({% link _tutorials/machine-learning/ML-intro/4-03-q-learning.md %}) 一模一样, 因为我们使用的是 Q 表的形式决策, 所以我们会在 Q 表中挑选值较大的动作值施加在环境中来换取奖惩. 但是不同的地方在于 Sarsa 的更新方式是不一样的.



{% include assign-heading.html %}


{% include tut-image.html image-name="s3.png" %}

同样, 我们会经历正在写作业的状态 s1, 然后再挑选一个带来最大潜在奖励的动作 a2, 这样我们就到达了 继续写作业状态 s2, 而在这一步, 如果你用的是 Q learning, 你会观看一下在 s2 上选取哪一个动作会带来最大的奖励, 但是在真正要做决定时, 却不一定会选取到那个带来最大奖励的动作, Q-learning 在这一步只是估计了一下接下来的动作值. 而 Sarsa 是实践派, 他说到做到, 在 s2 这一步估算的动作也是接下来要做的动作. 所以 Q(s1, a2) 现实的计算值, 我们也会稍稍改动, 去掉maxQ, 取而代之的是在 s2 上我们实实在在选取的 a2 的 Q 值. 最后像 Q learning 一样, 求出现实和估计的差距 并更新 Q 表里的 Q(s1, a2).


{% include google-in-article-ads.html %}


{% include assign-heading.html %}

{% include tut-image.html image-name="s4.png" %}

从算法来看, 这就是他们两最大的不同之处了. 因为 Sarsa 是说到做到型, 所以我们也叫他 on-policy, 在线学习, 学着自己在做的事情. 而 Q learning 是说到但并不一定做到, 所以它也叫作 Off-policy, 离线学习. 而因为有了 maxQ, Q-learning 也是一个特别勇敢的算法.

{% include tut-image.html image-name="s5.png" %}

为什么说他勇敢呢, 因为 Q learning 机器人 永远都会选择最近的一条通往成功的道路, 不管这条路会有多危险. 而 Sarsa 则是相当保守, 他会选择离危险远远的, 拿到宝藏是次要的, 保住自己的小命才是王道. 这就是使用 Sarsa 方法的不同之处.