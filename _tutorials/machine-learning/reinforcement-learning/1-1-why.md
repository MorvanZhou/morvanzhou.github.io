---
youku_id: XMTg5MjM2ODgwOA
youtube_id: o5fjkcM_lHs
bilibili_id: 15987274
chapter: 1
title: 为什么用强化学习 Why?
publish-date: 2017-01-01
thumbnail: "/static/thumbnail/rl/1_why.jpg"
description: "强化学习 (Reinforcement Learning) 是一个机器学习大家族中的分支, 由于近些年来的技术突破,
和深度学习 (Deep Learning) 的整合, 使得强化学习有了进一步的运用. 比如让计算机学着玩游戏,
AlphaGo 挑战世界围棋高手, 都是强化学习在行的事.
强化学习也是让你的程序从对当前环境完全陌生, 成长为一个在环境中游刃有余的高手."
post-headings:
  - 强化学习介绍
  - 模拟程序提前看
---

学习资料:
  * [有趣的机器学习 播放列表](/tutorials/machine-learning/ML-intro/)
  * [什么是强化学习 短视频]({% link _tutorials/machine-learning/ML-intro/4-01-RL.md %})
  * [强化学习实战]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})


 {% include assign-heading.html %}

强化学习 (Reinforcement Learning) 是一个机器学习大家族中的分支, 由于近些年来的技术突破,
和深度学习 (Deep Learning) 的整合, 使得强化学习有了进一步的运用. 比如让计算机学着玩游戏,
AlphaGo 挑战世界围棋高手, 都是强化学习在行的事.
强化学习也是让你的程序从对当前环境完全陌生, 成长为一个在环境中游刃有余的高手.

这些教程的教学, 不依赖于任何强化学习的 python 模块.
因为强化学习的复杂性, 多样性, 到现在还没有比较好的统一化模块.
不过我们还是能用最基础的方法编出优秀的强化学习程序!

 {% include assign-heading.html %}

以下是我们将要在后续的课程中实现的牛逼的自学程序.

Youtube 的模拟视频都在这里:

[https://www.youtube.com/playlist?list=PLXO45tsB95cLYyEsEylpPvTY-8ErPt2O_](https://www.youtube.com/playlist?list=PLXO45tsB95cLYyEsEylpPvTY-8ErPt2O_){:target="_blank"}.

优酷的模拟视频在这里:

[http://list.youku.com/albumlist/show?id=27485743&ascending=1&page=1](http://list.youku.com/albumlist/show?id=27485743&ascending=1&page=1){:target="_blank"}

下面是其中一些模拟视频:

* Maze

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/reinforcement-learning/maze sarsa_lambda.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>


* Cartpole
<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/reinforcement-learning/cartpole dqn.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

* Mountain car
<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/reinforcement-learning/mountaincar dqn.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>
