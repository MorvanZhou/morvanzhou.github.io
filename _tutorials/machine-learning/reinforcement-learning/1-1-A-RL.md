---
youku_id: XMTg5MjI0MTQ1Ng
youtube_id: NVWBs7b3oGk
bilibili_id: 15987015
title: 什么是 强化学习 (Reinforcement Learning)
description: "强化学习是机器学习大家族中的一大类, 使用强化学习能够让机器学着如何在环境中拿到高分, 表现出优秀的成绩.
而这些成绩背后却是他所付出的辛苦劳动, 不断的试错, 不断地尝试, 累积经验, 学习经验. 强化学习是一类算法, 是让计算机实现从一开始什么都不懂, 脑袋里没有一点想法, 通过不断地尝试, 从错误中学习, 最后找到规律, 学会了达到目的的方法. 这就是一个完整的强化学习过程. 实际中的强化学习例子有很多. 比如近期最有名的 Alpha go, 机器头一次在围棋场上战胜人类高手, 让计算机自己学着玩经典游戏 Atari, 这些都是让计算机在不断的尝试中更新自己的行为准则, 从而一步步学会如何下好围棋, 如何操控游戏得到高分. 既然要让计算机自己学, 那计算机通过什么来学习呢?"
chapter: 1
thumbnail: /static/thumbnail/ML-intro/what_is_RL.png
post-headings:
  - 从无到有
  - 虚拟老师
  - 对比监督学习
  - RL 算法们
ref-path: _tutorials/machine-learning/ML-intro/4-01-RL.md
---


{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}