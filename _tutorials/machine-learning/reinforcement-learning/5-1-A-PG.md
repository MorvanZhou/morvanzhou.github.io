---
youku_id: XMjY0NDkzMDg0MA
youtube_id: cw0USSxeEzw
bilibili_id: 15989997
title: 什么是 Policy Gradients
description: "今天我们会来说说强化学习家族中另一类型算法, 叫做 Policy Gradients.强化学习是一个通过奖惩来学习正确行为的机制. 家族中有很多种不一样的成员,  有学习奖惩值, 根据自己认为的高价值选行为, 比如 Q learning, Deep Q Network, 也有不通过分析奖励值,  直接输出行为的方法, 这就是今天要说的 Policy Gradients 了.  甚至我们可以为 Policy  Gradients 加上一个神经网络来输出预测的动作. 对比起以值为基础的方法, Policy Gradients 直接输出动作的最大好处就是, 它能在一个连续区间内挑选动作, 而基于值的, 比如 Q-learning, 它如果在无穷多的动作中计算价值, 从而选择行为, 这, 它可吃不消."
chapter: 5
thumbnail: /static/thumbnail/ML-intro/PG.png
post-headings:
  - 和以往的强化学习方法不同
  - 更新不同之处
  - 具体更新步骤
ref-path: _tutorials/machine-learning/ML-intro/4-07-PG.md
---


{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}