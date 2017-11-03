---
youku_id: XMjY0NTA4NzE5Mg
youtube_id: HTONz4ZLGxw
bilibili_id: 15990440
title: 什么是 Actor Critic
description: "今天我们会来说说强化学习中的一种结合体 Actor Critic (演员评判家), 它合并了 以值为基础 (比如 Q learning) 和 以动作概率为基础 (比如 Policy Gradients) 两类强化学习算法.
我们有了像 Q-learning 这么伟大的算法, 为什么还要瞎折腾出一个 Actor-Critic? 原来 Actor-Critic 的 Actor 的前生是 Policy Gradients , 这能让它毫不费力地在连续动作中选取合适的动作, 而 Q-learning 做这件事会瘫痪. 那为什么不直接用 Policy Gradients 呢? 原来 Actor Critic 中的 Critic 的前生是 Q-learning 或者其他的 以值为基础的学习法 , 能进行单步更新, 而传统的 Policy Gradients 则是回合更新, 这降低了学习效率."
chapter: 6
thumbnail: /static/thumbnail/ML-intro/AC.png
post-headings:
  - 为什么要有 Actor 和 Critic
  - Actor 和 Critic
  - 增加单步更新属性
  - 改进版 Deep Deterministic Policy Gradient (DDPG)
ref-path: _tutorials/machine-learning/ML-intro/4-08-AC.md
---


{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}