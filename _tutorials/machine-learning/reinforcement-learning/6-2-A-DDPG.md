---
youku_id: XMjY5NTAyNDU2OA
youtube_id: 3e6pfzux1x0
bilibili_id: 15990727
title: 什么是 Deep Deterministic Policy Gradient (DDPG)
description: "今天我们会来说说强化学习中的一种actor critic 的提升方式 Deep Deterministic Policy Gradient (DDPG), DDPG 最大的优势就是能够在连续动作上更有效地学习.
它吸收了 Actor critic 让 Policy gradient 单步更新的精华, 而且还吸收让计算机学会玩游戏的 DQN 的精华, 合并成了一种新算法,
叫做 Deep Deterministic Policy Gradient. 那 DDPG 到底是什么样的算法呢, 我们就拆开来分析,
我们将 DDPG 分成 Deep  和 Deterministic Policy Gradient, 然后 Deterministic Policy Gradient 又能被细分为 Deterministic 和 Policy Gradient,
接下来, 我们就开始一个个分析啦."
chapter: 6
thumbnail: /static/thumbnail/ML-intro/DDPG.png
post-headings:
  - 拆分细讲
  - Deep 和 DQN
  - Deterministic Policy Gradient
  - DDPG 神经网络
ref-path: _tutorials/machine-learning/ML-intro/4-09-DDPG.md
---


{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}