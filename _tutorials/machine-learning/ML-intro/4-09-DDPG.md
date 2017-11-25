---
youku_id: XMjY5NTAyNDU2OA
youtube_id: 3e6pfzux1x0
bilibili_id: 15990727
title: Deep Deterministic Policy Gradient (DDPG)
description: "今天我们会来说说强化学习中的一种actor critic 的提升方式 Deep Deterministic Policy Gradient (DDPG), DDPG 最大的优势就是能够在连续动作上更有效地学习.
它吸收了 Actor critic 让 Policy gradient 单步更新的精华, 而且还吸收让计算机学会玩游戏的 DQN 的精华, 合并成了一种新算法,
叫做 Deep Deterministic Policy Gradient. 那 DDPG 到底是什么样的算法呢, 我们就拆开来分析,
我们将 DDPG 分成 Deep  和 Deterministic Policy Gradient, 然后 Deterministic Policy Gradient 又能被细分为 Deterministic 和 Policy Gradient,
接下来, 我们就开始一个个分析啦."
publish-date: 2017-04-08
chapter: 4
thumbnail: /static/thumbnail/ML-intro/DDPG.png
post-headings:
  - 拆分细讲
  - Deep 和 DQN
  - Deterministic Policy Gradient
  - DDPG 神经网络
---

学习资料:
  * [强化学习教程]({% link _table-contents/machine-learning/reinforcement-learning.html %})
  * [强化学习模拟程序](https://www.youtube.com/watch?v=G5BDgzxfLvA&list=PLXO45tsB95cLYyEsEylpPvTY-8ErPt2O_){:target="_blank"}
  * [DDPG Python 教程]({% link _tutorials/machine-learning/reinforcement-learning/6-2-DDPG.md %})
  * [强化学习实战]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})
  * 论文 [Continuous control with deep reinforcement learning](https://arxiv.org/abs/1509.02971){:target="_blank"}

今天我们会来说说强化学习中的一种actor critic 的提升方式 Deep Deterministic Policy Gradient (DDPG), DDPG 最大的优势就是能够在连续动作上更有效地学习.

**注: 本文不会涉及数学推导. 大家可以在很多其他地方找到优秀的数学推导文章.**

 {% include assign-heading.html %}


{% include tut-image.html image-name="ddpg1.png" %}


它吸收了 [Actor-Critic]({% link _tutorials/machine-learning/ML-intro/4-08-AC.md %}) 让
[Policy gradient]({% link _tutorials/machine-learning/ML-intro/4-07-PG.md %}) 单步更新的精华,
而且还吸收让计算机学会玩游戏的 [DQN]({% link _tutorials/machine-learning/ML-intro/4-06-DQN.md %}) 的精华,
合并成了一种新算法, 叫做 Deep Deterministic Policy Gradient. 那 DDPG 到底是什么样的算法呢, 我们就拆开来分析,  我们将 DDPG 分成 ‘Deep’  和 ‘Deterministic Policy Gradient’, 然后 ‘Deterministic Policy Gradient’ 又能被细分为  ‘Deterministic’ 和 ‘Policy Gradient’, 接下来, 我们就开始一个个分析啦.


 {% include assign-heading.html %}

{% include tut-image.html image-name="ddpg2.png" %}

Deep 顾名思义, 就是走向更深层次,  我们在 DQN 的影片当中提到过, 使用一个记忆库和两套结构相同, 但参数更新频率不同的神经网络能有效促进学习.  那我们也把这种思想运用到 DDPG 当中, 使 DDPG 也具备这种优良形式. 但是 DDPG 的神经网络形式却比 DQN 的要复杂一点点.


 {% include assign-heading.html %}

{% include tut-image.html image-name="ddpg3.png" %}

Policy gradient 我们也在之前的短片中提到过, 相比其他的强化学习方法, 它能被用来在连续动作上进行动作的筛选 .  而且筛选的时候是根据所学习到的动作分布随机进行筛选, 而 Deterministic 有点看不下去, Deterministic 说: 我说兄弟, 你其实在做动作的时候没必要那么不确定, 那么犹豫嘛, 反正你最终都只是要输出一个动作值, 干嘛要随机, 铁定一点, 有什么不好. 所以 Deterministic 就改变了输出动作的过程,  斩钉截铁的只在连续动作上输出一个动作值.

{% include google-in-article-ads.html %}


 {% include assign-heading.html %}

{% include tut-image.html image-name="ddpg4.png" %}

现在我们来说说 DDPG 中所用到的神经网络. 它其实和我们之前提到的 Actor-Critic 形式差不多, 也需要有基于 策略 Policy 的神经网络 和基于 价值 Value 的神经网络, 但是为了体现 DQN 的思想, 每种神经网络我们都需要再细分为两个, Policy Gradient 这边,  我们有估计网络和现实网络,  估计网络用来输出实时的动作, 供 actor 在现实中实行. 而现实网络则是用来更新价值网络系统的. 所以我们再来看看价值系统这边,  我们也有现实网络和估计网络, 他们都在输出这个状态的价值, 而输入端却有不同,  状态现实网络这边会拿着从动作现实网络来的动作加上状态的观测值加以分析,  而状态估计网络则是拿着当时 Actor 施加的动作当做输入.在实际运用中, DDPG 的这种做法的确带来了更有效的学习过程.

