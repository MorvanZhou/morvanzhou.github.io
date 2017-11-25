---
youku_id: XMjI1OTczMjQ3Mg
youtube_id: PANBb46qiYI
bilibili_id: 15988394
title: Sarsa(lambda)
description: "今天我们会来说说强化学习中基于 Sarsa 的一种提速方法, 叫做 sarsa-lambda. 通过上个视频的介绍, 我们知道这个 Sarsa 的算法是一种在线学习法, on-policy. 但是这个 lambda 到底是什么. 其实吧, Sarsa 是一种单步更新法, 在环境中每走一步, 更新一次自己的行为准则, 我们可以在这样的 Sarsa 后面打一个括号, 说他是 Sarsa(0), 因为他等走完这一步以后直接更新行为准则. 如果延续这种想法, 走完这步, 再走一步, 然后再更新, 我们可以叫他 Sarsa(1). 同理, 如果等待回合完毕我们一次性再更新呢, 比如这回合我们走了 n 步, 那我们就叫 Sarsa(n). 为了统一这样的流程, 我们就有了一个 lambda 值来代替我们想要选择的步数, 这也就是 Sarsa(lambda) 的由来. 我们看看最极端的两个例子, 对比单步更新和回合更新, 看看回合更新的优势在哪里."
publish-date: 2017-01-13
chapter: 4
thumbnail: /static/thumbnail/ML-intro/Sarsa-lambda_thumbnail.png
post-headings:
  - Sarsa(n)
  - 单步更新 and 回合更新
  - 有时迷茫
  - Lambda 含义
  - Lambda 取值
---

学习资料:
  * [强化学习教程]({% link _table-contents/machine-learning/reinforcement-learning.html %})
  * [强化学习模拟程序](https://www.youtube.com/watch?v=G5BDgzxfLvA&list=PLXO45tsB95cLYyEsEylpPvTY-8ErPt2O_){:target="_blank"}
  * [Sarsa 简介视频]({% link _tutorials/machine-learning/ML-intro/4-04-sarsa.md %})
  * [Sarsa(lambda) Python 教程]({% link _tutorials/machine-learning/reinforcement-learning/3-3-tabular-sarsa-lambda.md %})
  * [强化学习实战]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})
  * 学习书籍 [Reinforcement learning: An introduction](http://ufal.mff.cuni.cz/~straka/courses/npfl114/2016/sutton-bookdraft2016sep.pdf){:target="_blank"}


今天我们会来说说强化学习中基于 Sarsa 的一种提速方法, 叫做 sarsa-lambda.

**注: 本文不会涉及数学推导. 大家可以在很多其他地方找到优秀的数学推导文章.**


 {% include assign-heading.html %}


{% include tut-image.html image-name="sl1.png" %}

通过上个视频的介绍, 我们知道这个 [Sarsa]{% link _tutorials/machine-learning/ML-intro/4-04-sarsa.md %})) 的算法是一种在线学习法, on-policy. 但是这个 lambda 到底是什么. 其实吧, Sarsa 是一种单步更新法, 在环境中每走一步, 更新一次自己的行为准则, 我们可以在这样的 Sarsa 后面打一个括号, 说他是 Sarsa(0), 因为他等走完这一步以后直接更新行为准则. 如果延续这种想法, 走完这步, 再走一步, 然后再更新, 我们可以叫他 Sarsa(1). 同理, 如果等待回合完毕我们一次性再更新呢, 比如这回合我们走了 n 步, 那我们就叫 Sarsa(n). 为了统一这样的流程, 我们就有了一个 lambda 值来代替我们想要选择的步数, 这也就是 Sarsa(lambda) 的由来. 我们看看最极端的两个例子, 对比单步更新和回合更新, 看看回合更新的优势在哪里.



 {% include assign-heading.html %}

{% include tut-image.html image-name="sl2.png" %}

虽然我们每一步都在更新, 但是在没有获取宝藏的时候, 我们现在站着的这一步也没有得到任何更新, 也就是直到获取宝藏时, 我们才为获取到宝藏的上一步更新为: 这一步很好, 和获取宝藏是有关联的, 而之前为了获取宝藏所走的所有步都被认为和获取宝藏没关系. 回合更新虽然我要等到这回合结束, 才开始对本回合所经历的所有步都添加更新, 但是这所有的步都是和宝藏有关系的, 都是为了得到宝藏需要学习的步, 所以每一个脚印在下回合被选则的几率又高了一些. 在这种角度来看, 回合更新似乎会有效率一些.



 {% include assign-heading.html %}

{% include tut-image.html image-name="sl3.png" %}

我们看看这种情况, 还是使用单步更新的方法在每一步都进行更新, 但是同时记下之前的寻宝之路. 你可以想像, 每走一步, 插上一个小旗子, 这样我们就能清楚的知道除了最近的一步, 找到宝物时还需要更新哪些步了. 不过, 有时候情况可能没有这么乐观. 开始的几次, 因为完全没有头绪, 我可能在原地打转了很久, 然后才找到宝藏, 那些重复的脚步真的对我拿到宝藏很有必要吗? 答案我们都知道. 所以Sarsa(lambda)就来拯救你啦.



{% include google-in-article-ads.html %}

 {% include assign-heading.html %}

{% include tut-image.html image-name="sl4.png" %}

其实 lambda 就是一个衰变值, 他可以让你知道离奖励越远的步可能并不是让你最快拿到奖励的步, 所以我们想象我们站在宝藏的位置, 回头看看我们走过的寻宝之路, 离宝藏越近的脚印越看得清, 远处的脚印太渺小, 我们都很难看清, 那我们就索性记下离宝藏越近的脚印越重要, 越需要被好好的更新. 和之前我们提到过的 奖励衰减值 gamma 一样, lambda 是脚步衰减值, 都是一个在 0 和 1 之间的数.



 {% include assign-heading.html %}

{% include tut-image.html image-name="sl5.png" %}

当 lambda 取0, 就变成了 Sarsa 的单步更新, 当 lambda 取 1, 就变成了回合更新, 对所有步更新的力度都是一样. 当 lambda 在 0 和 1 之间, 取值越大, 离宝藏越近的步更新力度越大. 这样我们就不用受限于单步更新的每次只能更新最近的一步, 我们可以更有效率的更新所有相关步了.