---
youku_id: XMTkyMDY5MTk2OA
youtube_id: AINrxEjflaM
bilibili_id: 15987194
title: 强化学习方法汇总 (Reinforcement Learning)
description: "了解强化学习中常用到的几种方法,以及他们的区别, 对我们根据特定问题选择方法时很有帮助.
强化学习是一个大家族, 发展历史也不短, 具有很多种不同方法. 比如说比较知名的控制方法 Q learning, Policy gradients, 还有基于对环境的理解的 model-based RL 等等. 接下来我们通过分类的方式来了解他们的区别."
publish-date: 2017-01-06
chapter: 4
thumbnail: /static/thumbnail/ML-intro/RL_methods.png
post-headings:
  - Model-free 和 Model-based
  - 基于概率 和 基于价值
  - 回合更新 和 单步更新
  - 在线学习 和 离线学习
---

学习资料:
  * [强化学习教程]({% link _table-contents/machine-learning/reinforcement-learning.html %})
  * [强化学习模拟程序](https://www.youtube.com/watch?v=G5BDgzxfLvA&list=PLXO45tsB95cLYyEsEylpPvTY-8ErPt2O_){:target="_blank"}
  * [强化学习实战]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})
  * 学习书籍 [Reinforcement learning: An introduction](http://ufal.mff.cuni.cz/~straka/courses/npfl114/2016/sutton-bookdraft2016sep.pdf){:target="_blank"}



了解强化学习中常用到的几种方法,以及他们的区别, 对我们根据特定问题选择方法时很有帮助.
强化学习是一个大家族, 发展历史也不短, 具有很多种不同方法. 比如说比较知名的控制方法 [Q learning]({% link _tutorials/machine-learning/ML-intro/4-03-q-learning.md %}),
[Policy Gradients]({% link _tutorials/machine-learning/ML-intro/4-07-PG.md %}), 还有基于对环境的理解的 model-based RL 等等. 接下来我们通过分类的方式来了解他们的区别.


 {% include assign-heading.html %}

{% include tut-image.html image-name="RLmtd1.png" %}

我们可以将所有强化学习的方法分为理不理解所处环境,如果我们不尝试去理解环境, 环境给了我们什么就是什么. 我们就把这种方法叫做 model-free, 这里的 model 就是用模型来表示环境, 那理解了环境也就是学会了用一个模型来代表环境, 所以这种就是 model-based 方法. 我们想象. 现在环境就是我们的世界, 我们的机器人正在这个世界里玩耍, 他不理解这个世界是怎样构成的, 也不理解世界对于他的行为会怎么样反馈. 举个例子, 他决定丢颗原子弹去真实的世界, 结果把自己给炸死了, 所有结果都是那么现实. 不过如果采取的是 model-based RL, 机器人会通过过往的经验, 先理解真实世界是怎样的, 并建立一个模型来模拟现实世界的反馈, 最后他不仅可以在现实世界中玩耍, 也能在模拟的世界中玩耍 , 这样就没必要去炸真实世界, 连自己也炸死了, 他可以像玩游戏一样炸炸游戏里的世界, 也保住了自己的小命. 那我们就来说说这两种方式的强化学习各用那些方法吧.

Model-free 的方法有很多, 像 [Q learning]({% link _tutorials/machine-learning/ML-intro/4-03-q-learning.md %}),
[Sarsa]({% link _tutorials/machine-learning/ML-intro/4-04-sarsa.md %}),
[Policy Gradients]({% link _tutorials/machine-learning/ML-intro/4-07-PG.md %}) 都是从环境中得到反馈然后从中学习.
而 model-based RL 只是多了一道程序, 为真实世界建模, 也可以说他们都是 model-free 的强化学习, 只是 model-based 多出了一个虚拟环境, 我们不仅可以像 model-free 那样在现实中玩耍,还能在游戏中玩耍, 而玩耍的方式也都是 model-free 中那些玩耍方式, 最终 model-based 还有一个杀手锏是 model-free 超级羡慕的. 那就是想象力.

Model-free 中, 机器人只能按部就班, 一步一步等待真实世界的反馈, 再根据反馈采取下一步行动. 而 model-based, 他能通过想象来预判断接下来将要发生的所有情况. 然后选择这些想象情况中最好的那种. 并依据这种情况来采取下一步的策略, 这也就是 围棋场上 AlphaGo 能够超越人类的原因. 接下来, 我们再来用另外一种分类方法将 强化学习分为基于概率和基于价值.



 {% include assign-heading.html %}


{% include tut-image.html image-name="RLmtd2.png" %}

基于概率是强化学习中最直接的一种, 他能通过感官分析所处的环境, 直接输出下一步要采取的各种动作的概率, 然后根据概率采取行动, 所以每种动作都有可能被选中, 只是可能性不同. 而基于价值的方法输出则是所有动作的价值, 我们会根据最高价值来选着动作, 相比基于概率的方法, 基于价值的决策部分更为铁定, 毫不留情, 就选价值最高的, 而基于概率的, 即使某个动作的概率最高, 但是还是不一定会选到他.

我们现在说的动作都是一个一个不连续的动作, 而对于选取连续的动作, 基于价值的方法是无能为力的. 我们却能用一个概率分布在连续动作中选取特定动作, 这也是基于概率的方法的优点之一. 那么这两类使用的方法又有哪些呢?

比如在基于概率这边, 有 [Policy Gradients]({% link _tutorials/machine-learning/ML-intro/4-07-PG.md %}), 在基于价值这边有
[Q learning]({% link _tutorials/machine-learning/ML-intro/4-03-q-learning.md %}),
[Sarsa]({% link _tutorials/machine-learning/ML-intro/4-04-sarsa.md %}) 等. 而且我们还能结合这两类方法的优势之处, 创造更牛逼的一种方法,
叫做 [Actor-Critic]({% link _tutorials/machine-learning/ML-intro/4-08-AC.md %}), actor 会基于概率做出动作, 而 critic 会对做出的动作给出动作的价值, 这样就在原有的 policy gradients 上加速了学习过程.


{% include google-in-article-ads.html %}


{% include assign-heading.html %}

{% include tut-image.html image-name="RLmtd3.png" %}

强化学习还能用另外一种方式分类, 回合更新和单步更新, 想象强化学习就是在玩游戏, 游戏回合有开始和结束. 回合更新指的是游戏开始后, 我们要等待游戏结束, 然后再总结这一回合中的所有转折点, 再更新我们的行为准则. 而单步更新则是在游戏进行中每一步都在更新, 不用等待游戏的结束, 这样我们就能边玩边学习了.

再来说说方法, Monte-carlo learning 和基础版的 policy gradients 等 都是回合更新制, Qlearning, Sarsa, 升级版的 policy gradients 等都是单步更新制. 因为单步更新更有效率, 所以现在大多方法都是基于单步更新. 比如有的强化学习问题并不属于回合问题.



 {% include assign-heading.html %}

{% include tut-image.html image-name="RLmtd4.png" %}

这个视频的最后一种分类方式是 在线学习和离线学习, 所谓在线学习, 就是指我必须本人在场, 并且一定是本人边玩边学习, 而离线学习是你可以选择自己玩, 也可以选择看着别人玩, 通过看别人玩来学习别人的行为准则, 离线学习 同样是从过往的经验中学习, 但是这些过往的经历没必要是自己的经历, 任何人的经历都能被学习. 或者我也不必要边玩边学习, 我可以白天先存储下来玩耍时的记忆, 然后晚上通过离线学习来学习白天的记忆.那么每种学习的方法又有哪些呢?

最典型的在线学习就是 Sarsa 了, 还有一种优化 Sarsa 的算法, 叫做 Sarsa lambda, 最典型的离线学习就是 Q learning, 后来人也根据离线学习的属性, 开发了更强大的算法, 比如让计算机学会玩电动的 Deep-Q-Network.

这就是我们从各种不同的角度来对比了强化学习中的多种算法.